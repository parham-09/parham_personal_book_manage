def main():

    name = input("enter your name:")
    print(f"welcome", {name})
    

    print("Welcome to Book Manager")
    

    count = int(input("how many enter book:"))
    
    books = []
    

    for i in range(count):
        book_name = input(f"enter book 1{i + 1}: ")
        books.append(book_name)
    
    print("\nلیست کتاب‌های ثبت شده:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")

if __name__ == "__main__":
    main()
