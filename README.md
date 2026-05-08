# Full-Stack To-Do List

Aplicação completa de gerenciamento de tarefas com cadastro de usuários, autenticação via JWT e CRUD de tarefas por usuário. O frontend é uma SPA em **Vue 3** que consome uma API REST construída com **FastAPI**, ambos orquestrados via Docker Compose com banco **MySQL**.

## Tech Stack

| Camada   | Tecnologia                          |
|----------|-------------------------------------|
| Frontend | Vue 3, Vue Router, Vite            |
| Backend  | FastAPI, Tortoise ORM, Pydantic    |
| Banco    | MySQL 8                            |
| Infra    | Docker, Docker Compose             |

## Estrutura do Projeto

```
├── backend/
│   └── app/
│       ├── controllers/   # Rotas (auth, tasks)
│       ├── core/          # Config e segurança (JWT)
│       ├── dto/           # Schemas de entrada/saída
│       ├── models/        # Modelos ORM (User, Task)
│       ├── repositories/  # Acesso a dados
│       ├── services/      # Regras de negócio
│       └── main.py        # Entrypoint da API
├── frontend/
│   └── src/
│       ├── components/    # Componentes Vue
│       ├── composables/   # Hooks (useAuth, useTasks)
│       ├── services/      # Chamadas HTTP
│       ├── views/         # Páginas
│       └── router/        # Rotas do SPA
└── docker-compose.yml
```

## Como Rodar

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
docker compose up --build
```

| Serviço     | URL                        |
|-------------|----------------------------|
| Frontend    | http://localhost:8080       |
| API         | http://localhost:8000       |
| phpMyAdmin  | http://localhost:8081       |

O banco de dados é criado automaticamente na primeira execução. As tabelas são geradas pelo Tortoise ORM ao iniciar a API.

## Variáveis de Ambiente

Configuradas diretamente no `docker-compose.yml` para desenvolvimento:

| Variável              | Valor padrão                              |
|-----------------------|-------------------------------------------|
| MYSQL_DATABASE        | todolist                                  |
| MYSQL_USER            | todouser                                  |
| MYSQL_PASSWORD        | todopass                                  |
| DATABASE_URL          | mysql://todouser:todopass@db:3306/todolist |

## API Endpoints

- `POST /auth/register` — Cadastro de usuário
- `POST /auth/login` — Login (retorna JWT)
- `GET /tasks` — Listar tarefas do usuário
- `POST /tasks` — Criar tarefa
- `PUT /tasks/{id}` — Atualizar tarefa
- `DELETE /tasks/{id}` — Remover tarefa
