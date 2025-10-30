from app.database.db import get_connection
from app.models.book import Book

class BookDAO:
    @staticmethod
    def create(title, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()
        return [Book(row["id"], row["title"], row["author_id"]) for row in rows]
