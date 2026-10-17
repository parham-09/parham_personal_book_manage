def display_books(books):
    print("\nRegistered books list:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")