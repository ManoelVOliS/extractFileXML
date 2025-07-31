import os
import xml.etree.ElementTree as ET
import pandas as pd

# --- Configurações ---
# ATENÇÃO: Aponte esta pasta para onde estão os seus arquivos .XML
PASTA_DE_ENTRADA = r'C:\Users\manoe\OneDrive\Área de Trabalho\XML ENTRADA\novos'

# ATENÇÃO: Aponte para a pasta onde o arquivo Excel final será salvo
PASTA_DE_SAIDA = r'C:\Users\manoe\OneDrive\Área de Trabalho\XML ENTRADA\Produtos ordenados'

# Nome do arquivo Excel de saída
ARQUIVO_DE_SAIDA_EXCEL = 'LISTA_XML_PRODUTOS_ORDENADOS.xlsx'
# --------------------


def extrair_dados_do_xml(caminho_arquivo):
    """
    Lê um único arquivo XML da NF-e e extrai uma lista de produtos com seus dados.
    """
    try:
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
    except ET.ParseError:
        print(f"  -> AVISO: Erro ao ler o arquivo XML '{os.path.basename(caminho_arquivo)}'. Pulando.")
        return []

    # Namespace é essencial para encontrar os elementos no XML da NF-e
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    
    produtos_extraidos = []
    
    # Pega o regime tributário do emitente para definir o perfil corretamente
    crt_element = root.find('.//nfe:emit/nfe:CRT', ns)
    crt = crt_element.text if crt_element is not None else ''

    # Itera sobre cada item (<det>) da nota fiscal
    for det in root.findall('.//nfe:det', ns):
        # Bloco de informações do produto
        prod_info = det.find('nfe:prod', ns)
        if prod_info is None: continue

        # Extração dos dados principais
        nome_produto = prod_info.find('nfe:xProd', ns).text
        cfop = prod_info.find('nfe:CFOP', ns).text
        qtd = float(prod_info.find('nfe:qCom', ns).text)
        v_unit = float(prod_info.find('nfe:vUnCom', ns).text)
        v_total = float(prod_info.find('nfe:vProd', ns).text)
        
        # A tag CEST pode não existir, então verificamos antes de pegar o valor
        cest_element = prod_info.find('nfe:CEST', ns)
        cest = cest_element.text if cest_element is not None else "Não informado"

        # --- Lógica para identificar o Perfil Tributário ---
        perfil_tributario = "Não identificado"
        imposto_info = det.find('nfe:imposto', ns)
        if imposto_info is not None:
            icms_group = imposto_info.find('nfe:ICMS', ns)
            if icms_group is not None:
                cst_element = icms_group.find('.//nfe:CST', ns)
                csosn_element = icms_group.find('.//nfe:CSOSN', ns)

                if cst_element is not None: # Regime Normal
                    cst = cst_element.text
                    if cst == '00': perfil_tributario = "Tributado Normal"
                    elif cst == '20': perfil_tributario = "Tributado 020 (Redução)"
                    elif cst in ['10', '30', '60', '70']: perfil_tributario = "Substituição Tributária"
                elif csosn_element is not None: # Simples Nacional
                     perfil_tributario = "Simples Nacional" # Simplificado

        # Adiciona os dados extraídos à lista
        produtos_extraidos.append({
            'Produto': nome_produto,
            'Quantidade': qtd,
            'Valor Unitário': v_unit,
            'Valor Total': v_total,
            'CFOP': cfop,
            'CEST': cest,
            'Perfil Tributário': perfil_tributario,
            'Arquivo de Origem': os.path.basename(caminho_arquivo)
        })
        
    return produtos_extraidos


def consolidar_xmls_e_ordenar():
    """
    Função principal que lê todos os XMLs, consolida e ordena alfabeticamente.
    """
    lista_de_todos_os_produtos = []
    
    if not os.path.isdir(PASTA_DE_ENTRADA):
        print(f"ERRO: A pasta de entrada não foi encontrada: '{PASTA_DE_ENTRADA}'")
        return

    arquivos_xml = [f for f in os.listdir(PASTA_DE_ENTRADA) if f.lower().endswith('.xml')]

    if not arquivos_xml:
        print("Nenhum arquivo .xml foi encontrado na pasta de entrada.")
        return

    print(f"Lendo {len(arquivos_xml)} arquivo(s) .xml...")

    for nome_arquivo in arquivos_xml:
        caminho_arquivo = os.path.join(PASTA_DE_ENTRADA, nome_arquivo)
        # A função agora lê o XML e extrai os dados estruturados
        produtos_do_arquivo = extrair_dados_do_xml(caminho_arquivo)
        
        if produtos_do_arquivo:
            print(f"  -> Arquivo '{nome_arquivo}': {len(produtos_do_arquivo)} produtos encontrados.")
            lista_de_todos_os_produtos.extend(produtos_do_arquivo)
        
    if not lista_de_todos_os_produtos:
        print("\nNenhum produto foi extraído dos arquivos XML.")
        return

    print(f"\nTotal de {len(lista_de_todos_os_produtos)} produtos encontrados. Consolidando e ordenando...")
    
    df = pd.DataFrame(lista_de_todos_os_produtos)
    
    if 'Produto' not in df.columns:
        print("ERRO: A coluna 'Produto' não foi encontrada nos dados extraídos.")
        return
        
    # Ordena a tabela INTEIRA pela coluna 'Produto' em ordem alfabética
    df_ordenado = df.sort_values(by='Produto', ignore_index=True)

    if not os.path.exists(PASTA_DE_SAIDA):
        os.makedirs(PASTA_DE_SAIDA)

    caminho_saida_completo = os.path.join(PASTA_DE_SAIDA, ARQUIVO_DE_SAIDA_EXCEL)
    
    print(f"Salvando o arquivo Excel ordenado: '{caminho_saida_completo}'...")
    df_ordenado.to_excel(caminho_saida_completo, index=False)

    print("\nScript concluído com sucesso!")
    print("A lista final de produtos foi ordenada alfabeticamente e salva em Excel.")

if __name__ == '__main__':
    # Lembre-se de instalar as bibliotecas, se ainda não o fez:
    # No terminal, digite: pip install pandas openpyxl
    consolidar_xmls_e_ordenar()