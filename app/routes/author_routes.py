from flask import Blueprint, request, jsonify
from app.dao.author_dao import AuthorDAO

author_bp = Blueprint("author", __name__)

@author_bp.route("/", methods=["POST"])
def create_author():
    data = request.get_json()
    AuthorDAO.create(data["name"])
    return jsonify({"message": "Author created"}), 201

@author_bp.route("/", methods=["GET"])
def list_authors():
    authors = AuthorDAO.get_all()
    return jsonify([{"id": a.id, "name": a.name} for a in authors])
