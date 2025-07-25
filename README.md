# [Nome do seu Projeto - Ex: API de Renegociações Financeiras]

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![License](https://img.shields.io/badge/license-MIT-informational)

Breve descrição de uma ou duas frases sobre o que este projeto faz. Ex: *API RESTful desenvolvida para gerenciar o processo de renegociações financeiras, processando dados de planilhas e expondo endpoints para consulta e manipulação.*

---

## 📋 Tabela de Conteúdos

* [Sobre o Projeto](#-sobre-o-projeto)
* [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [⚙️ Instalação e Configuração](#-instalação-e-configuração)
* [▶️ Executando a Aplicação](#-executando-a-aplicação)
* [🌐 Endpoints da API](#-endpoints-da-api)
* [☁️ Deploy](#-deploy)
* [📄 Licença](#-licença)
* [✍️ Autor](#-autor)

---

## 📖 Sobre o Projeto

Uma descrição mais detalhada do projeto. Explique o problema que ele resolve, suas principais funcionalidades e o contexto em que foi desenvolvido. Se ele consome dados de alguma fonte específica (como planilhas), mencione aqui.

### Principais Funcionalidades

* API RESTful para operações de CRUD (Criar, Ler, Atualizar, Deletar).
* Estrutura de projeto escalável e organizada.
* Conexão com banco de dados SQLite para persistência de dados.
* Validação de dados de entrada usando Pydantic.
* Documentação interativa da API gerada automaticamente (Swagger UI e ReDoc).

---

## 🚀 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Linguagem:** [Python 3.10](https://www.python.org/)
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Servidor ASGI (Desenvolvimento):** [Uvicorn](https://www.uvicorn.org/)
* **Servidor WSGI (Produção):** [Gunicorn](https://gunicorn.org/)
* **Banco de Dados:** [SQLite](https://www.sqlite.org/index.html)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Gerenciamento de Configuração:** [Pydantic Settings](https://docs.pydantic.dev/latest/usage/settings/)

---

## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

**Pré-requisitos:**
* Python 3.10 ou superior
* Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[seu-usuario]/[nome-do-repositorio].git
    cd [nome-do-repositorio]
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto, copiando o arquivo de exemplo `.env.example`.
    ```bash
    # No Windows (usando copy)
    copy .env.example .env

    # No macOS/Linux (usando cp)
    cp .env.example .env
    ```
    Abra o arquivo `.env` e ajuste as configurações se necessário. Para este projeto, a configuração padrão do SQLite deve funcionar imediatamente.

    *(Nota: É uma boa prática criar um arquivo `.env.example` no seu repositório com as chaves necessárias, mas sem os valores sensíveis).*

---

## ▶️ Executando a Aplicação

Com as dependências instaladas e o ambiente configurado, inicie o servidor de desenvolvimento:

```bash
uvicorn src.main:app --reload
```

* A flag `--reload` faz com que o servidor reinicie automaticamente após qualquer alteração no código.

A aplicação estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Documentação Interativa da API

Uma das grandes vantagens do FastAPI é a documentação automática. Acesse um dos links abaixo enquanto a aplicação estiver rodando:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🌐 Endpoints da API

Aqui está uma lista dos principais endpoints disponíveis.

| Método HTTP | Endpoint                  | Descrição                                         |
| :---------- | :------------------------ | :------------------------------------------------ |
| `GET`       | `/`                       | Retorna uma mensagem de boas-vindas.              |
| `GET`       | `/status-banco`           | Verifica o status da conexão com o banco de dados.|
| `POST`      | `/renegociacoes`          | Cria uma nova renegociação.                       |
| `GET`       | `/renegociacoes/{id}`     | Busca uma renegociação específica pelo seu ID.    |
| `GET`       | `/renegociacoes`          | Lista todas as renegociações.                     |
| `PUT`       | `/renegociacoes/{id}`     | Atualiza uma renegociação existente.              |
| `DELETE`    | `/renegociacoes/{id}`     | Deleta uma renegociação.                          |

---

## ☁️ Deploy

Esta aplicação está configurada para deploy contínuo na plataforma **[Render](https://render.com/)**.

O deploy é feito automaticamente a cada `push` para a branch `main`. As configurações principais no ambiente da Render são:

* **Ambiente:** Python 3
* **Comando de Build:** `pip install -r requirements.txt`
* **Comando de Início (Start Command):** `gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app --bind 0.0.0.0:$PORT`

O uso de `gunicorn` é recomendado para produção, e a aplicação é configurada para escutar na porta fornecida pela variável de ambiente `$PORT` da Render.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

------