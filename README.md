# Extrator de Dados de XML de NF-e
Este repositório contém um script em Python para automatizar a extração de dados de produtos a partir de múltiplos arquivos XML de Notas Fiscais Eletrônicas (NF-e). O script consolida todas as informações em um único arquivo Excel, com a lista de produtos ordenada alfabeticamente.

📝 Descrição
Muitas vezes, empresas precisam consolidar as informações dos produtos recebidos de diversos fornecedores. Fazer isso manualmente, abrindo cada XML, é um processo lento e sujeito a erros.

Este script resolve esse problema ao:

Ler todos os arquivos .xml de uma pasta de entrada.

Extrair informações detalhadas de cada produto dentro das notas fiscais.

Identificar o perfil tributário de cada item (Simples Nacional, Tributado, Substituição Tributária, etc.).

Consolidar todos os produtos em uma única lista.

Salvar o resultado em um arquivo Excel (.xlsx), com os produtos ordenados em ordem alfabética para fácil consulta e análise.

✨ Funcionalidades
Leitura em Lote: Processa um número ilimitado de arquivos XML de uma só vez.

Extração Detalhada: Coleta dados essenciais como Nome do Produto, Quantidade, Valor Unitário, Valor Total, CFOP e CEST.

Análise Tributária Simplificada: Identifica e rotula o perfil tributário do ICMS de cada produto.

Consolidação Automática: Agrupa produtos de diferentes notas em um único local.

Organização: Ordena a lista final de produtos alfabeticamente para facilitar a visualização.

Exportação para Excel: Gera um arquivo .xlsx limpo e pronto para ser utilizado.

🚀 Pré-requisitos
Antes de começar, você precisará ter o seguinte instalado:

Python 3.x

As bibliotecas Python pandas e openpyxl.

⚙️ Instalação
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
(Ou simplesmente baixe o arquivo .py para uma pasta no seu computador).

Instale as dependências:
Abra o seu terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias:

Bash

pip install pandas openpyxl
🛠️ Configuração
Antes de executar o script, você precisa configurar os caminhos das pastas de entrada e saída. Abra o arquivo .py em um editor de texto e altere as seguintes linhas:

Python

# --- Configurações ---
# ATENÇÃO: Aponte esta pasta para onde estão os seus arquivos .XML
PASTA_DE_ENTRADA = r'C:\Caminho\Para\Sua\Pasta\De\XMLs'

# ATENÇÃO: Aponte para a pasta onde o arquivo Excel final será salvo
PASTA_DE_SAIDA = r'C:\Caminho\Para\Salvar\O\Excel'

# Nome do arquivo Excel de saída (opcional)
ARQUIVO_DE_SAIDA_EXCEL = 'LISTA_XML_PRODUTOS_ORDENADOS.xlsx'
# --------------------
PASTA_DE_ENTRADA: Coloque o caminho completo da pasta onde você armazena os arquivos XML que deseja processar.

PASTA_DE_SAIDA: Coloque o caminho completo da pasta onde o arquivo Excel gerado será salvo.

▶️ Como Usar
Prepare os arquivos: Coloque todos os seus arquivos de NF-e (.xml) na pasta que você definiu em PASTA_DE_ENTRADA.

Execute o script: Abra um terminal ou prompt de comando, navegue até a pasta onde o script está salvo e execute-o com o seguinte comando:

Bash

python seu_script.py
(Substitua seu_script.py pelo nome real do seu arquivo Python).

Verifique o resultado: Após a execução, o script criará o arquivo LISTA_XML_PRODUTOS_ORDENADOS.xlsx na pasta definida em PASTA_DE_SAIDA. O terminal também exibirá o progresso e o status da operação.

📊 Estrutura do Excel de Saída
O arquivo Excel gerado conterá as seguintes colunas, com os dados de todos os produtos ordenados pela coluna Produto:

Coluna	Descrição
Produto	Nome/Descrição do produto.
Quantidade	Quantidade comercial do produto na nota.
Valor Unitário	Valor unitário de comercialização do produto.
Valor Total	Valor total do produto (Quantidade * Valor Unitário).
CFOP	Código Fiscal de Operações e Prestações.
CEST	Código Especificador da Substituição Tributária.
Perfil Tributário	Classificação do imposto (Tributado, ST, Simples Nacional, etc.).
Arquivo de Origem	Nome do arquivo XML de onde o produto foi extraído.

Exportar para as Planilhas
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
