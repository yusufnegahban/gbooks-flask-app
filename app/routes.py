from flask import Blueprint
from app.models_goobook import BookGoogle

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    books = BookGoogle.query.limit(20).all()
    return "<br>".join([f"{b.title} - {b.authors}" for b in books])

