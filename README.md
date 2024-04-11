# Sistema de Gerenciamento Eletrônico de Documentos (GED) com OCR em Python

Este é um sistema de Gerenciamento Eletrônico de Documentos (GED) desenvolvido em Python, com a capacidade de realizar Reconhecimento Ótico de Caracteres (OCR). Ele visa facilitar o processo de coleta, armazenamento e recuperação de documentos eletrônicos, especialmente em áreas rurais.

## Funcionalidades Principais

- Coleta de documentos por meio de upload de arquivos ou captura de imagem.
- Reconhecimento ótico de caracteres para extrair texto de documentos digitalizados.
- Armazenamento seguro de documentos e metadados associados em um banco de dados.
- Recuperação rápida de documentos com base em critérios de busca.
- Preenchimento automático de formulários com informações extraídas de documentos digitalizados.

## Pré-requisitos

- Python 3.x instalado
- Poetry instalado (para instalar as dependências)

## Instalação

1. Clone este repositório em sua máquina local:

```
git clone https://github.com/F-moreno/projeto-final-ciclo1.git
```

2. Navegue até o diretório do projeto:

```
cd projeto-final-ciclo1
```

3. Instale o Poetry (caso ainda não tenha instalado):

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

4. Ative o Poetry (caso não tenha sido ativado automaticamente):

```
source $HOME/.poetry/env
```

5. Instale as dependências usando o Poetry:

```
poetry install
```

## Como Usar

1. Execute o arquivo `main.py` para iniciar o sistema:

```
python main.py
```

2. Siga as instruções na interface do usuário para utilizar as funcionalidades do sistema.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues relatando problemas ou sugestões de melhorias.

## Colaboradores 

- [André Gloos](https://github.com/AndreGloosRibeiro)
- [Artur malcher](https://github.com/ArturMalcher)
- [Diego Rodrigues](https://github.com/diegoalvarengarodrigues)
- [Fernando Moreno](https://github.com/F-moreno)