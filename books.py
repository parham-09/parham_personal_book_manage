import json

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def display_books(books):
    print("\nRegistered books list:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
