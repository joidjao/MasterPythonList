class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book_title_list = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "War and Peace"]
book_author_list = ["George Orwell", "Harper Lee", "F. Scott Fitzgerald", "Herman Melville", "Leo Tolstoy"]

print("\nBook Data:")
for i in range(len(book_title_list)):
    print(f"Title: {book_title_list[i]}, Author: {book_author_list[i]}")
