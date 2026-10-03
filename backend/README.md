# Backend

API FastAPI organizada em camadas orientadas a objetos:

- `api/`: rotas HTTP e dependencias da API.
- `controllers/`: coordenacao dos casos de uso para a camada HTTP.
- `services/`: regras de negocio.
- `repositories/`: consultas e persistencia.
- `models/`: entidades ORM do SQLAlchemy.
- `schemas/`: contratos de entrada e saida da API.
- `core/`: configuracoes da aplicacao.
- `db/`: engine, sessoes e base declarativa do banco.

## Executar localmente

1. Crie um banco PostgreSQL chamado `hackathon2026` e copie `.env.example` para `.env`.
2. Ajuste `DATABASE_URL` com as credenciais do seu PostgreSQL.
3. Instale as dependencias com `pip install -r requirements.txt`.
4. Inicie a API neste diretorio com `uvicorn app.main:app --reload`.

As tabelas mapeadas sao criadas na inicializacao. A documentacao interativa fica em `/docs`.