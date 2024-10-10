book_authors = {
    'To Kill a Mockingbird' : 'Harper Lee',
    '1984' : 'George Orwell',
    'The Great Gatsby' : 'F. Scott Fitzgerald',
    'Pride and Prejudice' : 'Jane Austen',
    'The Catcher in the Rye' : 'John Green',
    'The Lord of the Rings' : 'J.R.R Tolkien',
    'Moby-Dick' : 'Herman Melville',
    'The Alchemist' : 'Paulo Coelho',
    'War and Peace' : 'Leo Tolstoy',
    'Brave New World' : 'Aldous Huxley',
    'The Diary of a Young Girl' : 'Anne Frank',
    'The Hitchhikers Guide to the Galaxy' : 'Douglas Adams'
}

print("Books and their Authors:", book_authors)

print("Author of the 9th Book:", book_authors['War and Peace'])

book_authors['The Catcher in the Rye'] = 'J.D Salinger'

del book_authors['The Great Gatsby']

print("Last key-value pair:", book_authors)