books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby Dick", "author": "Herman Melville"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"}
]

def print_books():
    print("Books:")
    for book in books:
        print(f"Title: {book.get('title')}, Author: {book.get('author')}")
