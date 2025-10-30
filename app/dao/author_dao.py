from app.database.db import get_connection
from app.models.author import Author

class AuthorDAO:
    @staticmethod
    def create(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        rows = cursor.fetchall()
        conn.close()
        return [Author(row["id"], row["name"]) for row in rows]
