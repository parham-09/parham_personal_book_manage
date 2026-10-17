from books import display_books

def main():

    name = input("enter your name:")
    print("welcome", {name})
    
    count = int(input("How many books do you want to enter? "))
    books = []
    
    for i in range(count):
        book_name = input(f"Enter book {i + 1} name: ")
        books.append(book_name)
    
    display_books(books)

if __name__ == "__main__":
    main()