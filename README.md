# 🧬 pokedex-api

![Python](https://img.shields.io/badge/python-^3.13-blue)
![Poetry](https://img.shields.io/badge/poetry-1.8.0+-blueviolet)
![Lint](https://github.com/BrunoSegato/pokedex-api/actions/workflows/lint.yml/badge.svg)
![Tests](https://github.com/BrunoSegato/pokedex-api/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/github/license/BrunoSegato/pokedex-api)
![codecov](https://codecov.io/gh/BrunoSegato/pokedex-api/branch/main/graph/badge.svg)

Projeto de estudo com [FastAPI](https://fastapi.tiangolo.com/) e [PostgreSQL](https://www.postgresql.org/), focado em boas práticas de organização, qualidade de código e automação de tarefas.

---

## 🚀 Tecnologias utilizadas

- ⚙️ Python ^3.13
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🧪 Pytest
- 📦 Poetry
- 📜 Alembic (migrations)
- 🧹 Black, isort, flake8, mypy, bandit
- 🔁 pre-commit
- 🔧 Taskipy

---

## 📦 Instalação

1. Clone o projeto:

```bash
git clone https://github.com/seu-usuario/pokedex-api.git
cd pokedex-api
```

2. Instale as dependências com os grupos de desenvolvimento:

```bash
poetry install --with dev,lint
```

3. (Opcional) Ative os hooks do pre-commit:

```bash
poetry run pre-commit install
```

---

## 🔧 Configuração via `.env`

O projeto utiliza [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) para carregar variáveis de ambiente com validação e tipagem automática.

### Como configurar

1. Copie o arquivo de exemplo `.env.sample` para `.env`:
   ```bash
   cp .env.sample .env
   ```

---

## 🛠️ Comandos úteis

Utilize o [Taskipy](https://github.com/illBeRoy/taskipy) para executar tarefas comuns do projeto:

```bash
poetry run task --help  # lista todos os comandos disponíveis
```

### Comandos disponíveis:

| Comando                     | Descrição                                |
|-----------------------------|------------------------------------------|
| `poetry run task lint`      | Roda `flake8` para verificação de estilo |
| `poetry run task format`    | Aplica `black` e `isort` no código       |
| `poetry run task typecheck` | Verificação de tipos com `mypy`          |
| `poetry run task security`  | Análise de segurança com `bandit`        |
| `poetry run task precommit` | Executa todos os hooks do `pre-commit`   |
| `poetry run task test`      | Executa os testes com `pytest`           |

---

## 📜 Migrations com Alembic

Este projeto utiliza o [Alembic](https://alembic.sqlalchemy.org/) para versionamento e aplicação do schema do banco de dados PostgreSQL.

### Criar uma nova migration

Após modificar os modelos SQLAlchemy:

```bash
poetry run alembic revision --autogenerate -m "descrição da mudança"
```

### Aplicar todas as migrations

```bash
poetry run alembic upgrade head
```

### Rodar migrations em ambiente de testes (usado no CI)

O Alembic é utilizado para subir o schema de teste automaticamente antes dos testes, garantindo que a estrutura do banco esteja sincronizada.

---

## 🧪 Estrutura sugerida do projeto

```
.
├── app/                    # Código principal da API
│   ├── main.py             # Ponto de entrada FastAPI
│   ├── routers/            # Rotas da API
│   └── models/             # Schemas e modelos
├── db/                     # Configurações de banco e migrations
│   ├── migrations/         # Diretório gerado pelo Alembic
├── tests/                  # Testes automatizados
├── pyproject.toml
├── README.md
└── .pre-commit-config.yaml
```

> 💡 Reorganize conforme seu projeto evoluir. Essa estrutura é uma sugestão.

---

## 🧪 Rodando os testes

```bash
poetry run pytest -v
```

Adicione o Pytest ao seu projeto com:

```bash
poetry add --group dev pytest
```

---

## 📌 Requisitos para contribuição

- Python 3.13
- Poetry instalado (`curl -sSL https://install.python-poetry.org | python3 -`)
- Banco PostgreSQL (local ou container)
- Siga o padrão de commit (ex: Conventional Commits)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Referências

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Poetry Docs](https://python-poetry.org/docs/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Taskipy](https://github.com/illBeRoy/taskipy)
