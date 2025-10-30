from flask import Blueprint, request, jsonify
from app.dao.book_dao import BookDAO

book_bp = Blueprint("book", __name__)

@book_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    BookDAO.create(data["title"], data["author_id"])
    return jsonify({"message": "Book created"}), 201

@book_bp.route("/", methods=["GET"])
def list_books():
    books = BookDAO.get_all()
    return jsonify([{"id": b.id, "title": b.title, "author_id": b.author_id} for b in books])
