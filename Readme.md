# Flask DAO SQLite API

Exemplo de API REST com Flask usando padrão DAO e SQLite.

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

# Endpoints
## Autores

POST /authors/ → cria um autor

GET /authors/ → lista autores

## Livros

POST /books/ → cria um livro (precisa de author_id)

GET /books/ → lista livros