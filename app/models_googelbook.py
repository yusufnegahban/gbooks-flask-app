from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookGoogle(db.Model):
    __tablename__ = 'books_google'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    authors = db.Column(db.String(300))
    publisher = db.Column(db.String(200))
    published_date = db.Column(db.String(100))
    isbn = db.Column(db.String(50))
    page_count = db.Column(db.Integer)
    categories = db.Column(db.String(300))
    average_rating = db.Column(db.Float)
    thumbnail = db.Column(db.String(300))



