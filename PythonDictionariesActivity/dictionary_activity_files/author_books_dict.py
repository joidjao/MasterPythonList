author_books = {
    'J.K Rowling' : 'Harry Potter and Sorcerers Stone',
    'George Orwell' : 'Animal Farm',
    'Jane Austen' : 'Pride and Prejudice',
    'Ernest Hemingway' : 'The Old Man and the Sea',
    'Mark Twain' : 'The Adventures of Tom Sawyer',
    'F. Scott Fitzgerald' : 'The Great Gatsby',
    'Leo Tolstoy' : 'War and Peace',
    'Gabriel Garcia Marquez' : 'One Hundred Years of Solitude',
}

print("Authors and their Famous books:", author_books)

print("Book of Mark Twain:", author_books)

author_books['Leo Tolstoy'] = 'Anna Karenina'

del author_books['F. Scott Fitzgerald']

print("Last key-value pair:", author_books)