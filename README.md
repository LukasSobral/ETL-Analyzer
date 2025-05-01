# 💰 ETL Analyzer - Análise de Gastos com FastAPI + Streamlit + PostgreSQL

Este projeto é uma aplicação completa de backend e visualização de dados financeiros pessoais.  
A pipeline executa **upload de CSV com dados de gastos**, realiza **ETL com validação e transformação** e apresenta os dados em um **dashboard interativo com Streamlit**.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) — Backend e upload de arquivos
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM para PostgreSQL
- [Alembic](https://alembic.sqlalchemy.org/) — Migração de banco de dados
- [Streamlit](https://streamlit.io/) — Visualização de dados
- [Pandas](https://pandas.pydata.org/) — Processamento de dados
- [PostgreSQL](https://www.postgresql.org/) — Banco de dados relacional

---

## 📁 Estrutura do Projeto

```
etl-analyzer/
├── app/
│   ├── main.py              # FastAPI com rota de upload
│   ├── config.py            # Carregamento de variáveis de ambiente
│   ├── database.py          # Conexão com PostgreSQL
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Schemas Pydantic
│   └── etl/
│       ├── processor.py     # Processamento e transformação do CSV
│       └── loader.py        # Inserção no banco
├── alembic/                 # Migrações de banco
├── data/                    # CSV de exemplo
├── streamlit_app.py         # Dashboard
├── .env                     # Variáveis de ambiente
├── README.md
└── requirements.txt
```

---

## ⚙️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/etl-analyzer.git
cd etl-analyzer
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados PostgreSQL

Crie um banco chamado `etl_db` e configure seu `.env`:

```
DATABASE_URL=postgresql://postgres:senha@localhost:5432/etl_db
```

### 5. Rode as migrações (ou crie a tabela manualmente)

```bash
alembic upgrade head
```

Ou execute este SQL no seu banco, se necessário:

```sql
CREATE TABLE gastos (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    categoria VARCHAR NOT NULL,
    descricao VARCHAR,
    valor FLOAT NOT NULL,
    tipo VARCHAR NOT NULL,
    forma_pagamento VARCHAR
);
```

---

## 📤 Enviando os dados (API)

Execute a API:

```bash
uvicorn app.main:app --reload
```

Acesse:
```
http://localhost:8000/docs
```

Use a rota `/upload/` para enviar um arquivo `.csv`.

---

## 📊 Acessando o dashboard

```bash
streamlit run streamlit_app.py
```

Acesse no navegador:
```
http://localhost:8501
```

Você verá KPIs de Receita / Despesa, gráficos por categoria e evolução ao longo do tempo.

---

## 📎 Exemplo de CSV aceito

Separado por `;` e com cabeçalho:

```
data;categoria;descricao;valor;tipo;forma_pagamento
10/01/2024;Alimentação;Supermercado;250.5;despesa;Cartão
...
```

---

## 🙌 Créditos

Desenvolvido por [Lucas Sobral de Morais](https://www.linkedin.com/in/lucas-sobrall/) com foco em **boas práticas backend, ETL e visualização de dados**.