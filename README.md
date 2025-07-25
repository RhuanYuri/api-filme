# API de Avaliação de Filmes

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![License](https://img.shields.io/badge/license-MIT-informational)

API RESTful para uma plataforma de avaliação de filmes, permitindo que usuários cadastrados comentem, avaliem e favoritem seus filmes preferidos.

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

Esta API é o backend de um sistema de avaliação de filmes. Ela gerencia usuários, filmes, e as interações entre eles, como a publicação de críticas (comentário + nota) e a marcação de filmes como favoritos. A arquitetura foi projetada para ser escalável e de fácil manutenção.

### Principais Funcionalidades

* **Gerenciamento de Usuários:** Cadastro e autenticação de usuários via token (ex: JWT).
* **Listagem de Filmes:** Endpoints para listar filmes disponíveis e ver detalhes de um filme específico.
* **Sistema de Avaliações:** Usuários autenticados podem postar uma crítica (comentário e nota de 1 a 5) para um filme.
* **Sistema de Favoritos:** Usuários podem adicionar ou remover filmes de sua lista pessoal de favoritos.
* **Documentação Interativa:** Interface Swagger UI e ReDoc gerada automaticamente para testes e visualização dos endpoints.

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
    Crie um arquivo `.env` na raiz do projeto, copiando o arquivo de exemplo `.env.example`. Este arquivo pode conter chaves secretas para tokens, por exemplo.
    ```bash
    # No Windows (usando copy)
    copy .env.example .env

    # No macOS/Linux (usando cp)
    cp .env.example .env
    ```

5.  **Inicialize o banco de dados:**
    O banco de dados SQLite será criado e as tabelas serão geradas na primeira vez que a aplicação for executada.

---

## ▶️ Executando a Aplicação

Com as dependências instaladas, inicie o servidor de desenvolvimento:

```bash
uvicorn src.main:app --reload
```

* A flag `--reload` faz com que o servidor reinicie automaticamente após qualquer alteração no código.

A aplicação estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Documentação Interativa da API

Acesse um dos links abaixo enquanto a aplicação estiver rodando para testar os endpoints:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🌐 Endpoints da API

Abaixo estão os principais grupos de endpoints disponíveis.

| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| **Autenticação** | | | |
| `POST` | `/usuarios` | Cria um novo usuário. | Não |
| `POST` | `/token` | Gera um token de acesso para um usuário. | Não |
| **Filmes** | | | |
| `GET` | `/filmes` | Lista todos os filmes disponíveis. | Não |
| `GET` | `/filmes/{filme_id}` | Busca os detalhes de um filme específico. | Não |
| **Avaliações (Comentários e Notas)** | | | |
| `POST` | `/filmes/{filme_id}/avaliacoes` | Posta uma nova avaliação para um filme. | **Sim** |
| `GET` | `/filmes/{filme_id}/avaliacoes` | Lista todas as avaliações de um filme. | Não |
| `DELETE`| `/avaliacoes/{avaliacao_id}` | Deleta uma avaliação (se for o autor). | **Sim** |
| **Favoritos** | | | |
| `POST` | `/usuarios/me/favoritos/{filme_id}` | Adiciona um filme à lista de favoritos do usuário. | **Sim** |
| `GET` | `/usuarios/me/favoritos` | Lista os filmes favoritos do usuário logado. | **Sim** |
| `DELETE`| `/usuarios/me/favoritos/{filme_id}` | Remove um filme da lista de favoritos. | **Sim** |


---

## ☁️ Deploy

Esta aplicação está configurada para deploy contínuo na plataforma **[Render](https://render.com/)**.

O deploy é feito automaticamente a cada `push` para a branch `main`. As configurações principais no ambiente da Render são:

* **Ambiente:** Python 3
* **Comando de Build:** `pip install -r requirements.txt`
* **Comando de Início (Start Command):** `gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app --bind 0.0.0.0:$PORT`

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

