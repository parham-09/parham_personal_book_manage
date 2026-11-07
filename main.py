from books import load_books, save_books, display_books
import os

admin_mode = input("Enter Admin Mode? (y/n): ")
if admin_mode.lower() == "y":
    entered_password = input("Enter admin password: ")
    correct_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")
    
    if entered_password == correct_password:
        print("Admin Mode activated successfully.")
    else:
        print("Incorrect password.")
else:
    print("Continuing in normal mode.")

def main():
    
    answer = input("Do you want to enter Admin Mode? (y/n): ")
    if answer.lower() == "y":
        password = input("Enter admin password: ")

    name = print("enter your name:")
    print("welcome", {name})
    print("Welcome to Book Manager")

    tasks = load_books()
    if tasks:
        print("Previously registered books:")
        display_books(tasks)
    count = int(input("How many new books do you want to enter? "))
    
    for i in range(count):
        task_name = input("enter a task: ")
        priority = input("enter priority(low/medium/high): ").lower()
        
        task = {
            "name": task_name,
            "priority": priority
        }
        tasks.append(task)

save_books(tasks=save_books)