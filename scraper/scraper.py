from app import create_app
import requests
from app.models_goobook import db, BookGoogle

app = create_app()

def scrape_google_books():
    query = "python"
    for i in range(0, 100, 40):
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&startIndex={i}&maxResults=40"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ Failed to fetch data for index {i}")
            continue

        data = response.json()
        items = data.get("items", [])
        if not items:
            print(f"⚠️ No items found for index {i}")
            continue

        for item in items:
            volume_info = item.get("volumeInfo", {})

            title = volume_info.get("title", "")
            authors = ", ".join(volume_info.get("authors", []))
            publisher = volume_info.get("publisher", "")
            published_date = volume_info.get("publishedDate", "")
            isbn_list = volume_info.get("industryIdentifiers", [])
            isbn = isbn_list[0]['identifier'] if isbn_list else ""
            page_count = volume_info.get("pageCount", 0)
            categories = ", ".join(volume_info.get("categories", []))
            average_rating = volume_info.get("averageRating", 0.0)
            thumbnail = volume_info.get("imageLinks", {}).get("thumbnail", "")

            existing = BookGoogle.query.filter_by(title=title, isbn=isbn).first()
            if not existing:
                new_book = BookGoogle(
                    title=title,
                    authors=authors,
                    publisher=publisher,
                    published_date=published_date,
                    isbn=isbn,
                    page_count=page_count,
                    categories=categories,
                    average_rating=average_rating,
                    thumbnail=thumbnail
                )
                db.session.add(new_book)

        db.session.commit()
        print(f"✅ Fetched books {i} to {i+40}")

if __name__ == "__main__":
    with app.app_context():
        scrape_google_books()
