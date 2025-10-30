from flask import Flask
from app.routes.book_routes import book_bp
from app.routes.author_routes import author_bp
from app.database.db import init_db

app = Flask(__name__)
init_db()

# Registrar rotas
app.register_blueprint(book_bp, url_prefix="/books")
app.register_blueprint(author_bp, url_prefix="/authors")

if __name__ == "__main__":
    app.run(debug=True)
