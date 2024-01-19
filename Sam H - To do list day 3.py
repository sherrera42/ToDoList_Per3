# Name Maksym and Sam
# To do List 
# 1/10/2024

# Functions 

def intro(name, app):
    print("Hello, "+ name +". Welcome to "+ app)
def outro(name, app):
    print("Goodbye, "+ name + ". Thank you for using "+ app)
    
todo_list="Milk, Eggs and Flour"

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task to the to-do list")
    print("2. View the current to-do list")
    print("3. Mark a task as completed")
    print("4. Remove a task from the to-do list")
    print("5. Exit the program")
    print("6. Clear everything from your list")
    print("7. List alphabetically")
    print("8. The number of items in your list")

# Function for adding tasks to your list
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f'Task "{task}" added to the to-do list.')

# Function to view your current list
def view_list(todo_list):
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print(todo_list)

# Function to mark the tasks you have done
def mark_completed(todo_list):
    view_list(todo_list)
    index = int(input("Enter the task number to mark as completed: "))
    
    index = (index) - 1 

    if 0 <= index < len(todo_list): # The len (built in function which returns the length of a an object)is using here to make sure that the number is not bigger than the amount of tasks in a list
            todo_list[index] = f"[X] {todo_list[index]}" # The F{} I learned from this website https://realpython.com/python-f-strings/, its a really good thing if you want to make your code organized and make it shorter by using such functions.
            print("Task marked as completed.")
    else:
            print("Invalid task number.")

# Function to remove task from your list
def remove_task(todo_list):
    view_list(todo_list)
    index = int(input("Enter the task number to remove: "))

    index = (index) - 1 # I made it numeric, where you just choose which task you want to delete, which is much convenient

    if 0 <= index < len(todo_list): # Len I learned from cources when I learned python on my own.
            removed_task = todo_list.pop(index)
            print(f'Task "{removed_task}" removed from the to-do list.')
    else:
            print("Invalid task number.")

# Main program
def main():
    intro("User", "Todo_list")
    todo_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
                add_task(todo_list)
        elif choice == 2:
                view_list(todo_list)
        elif choice == 3:
                mark_completed(todo_list)
        elif choice == 4:
                remove_task(todo_list)
        elif choice == 5:
                print("Exiting the program. Goodbye!")
                outro("User", "Todo_list")
                break
        elif choice == 6:
              todo_list.clear()
        elif choice == 7:
              todo_list.sorted()
        elif choice == 8:
              print("Current number is 3")
        else:
                print("Invalid choice. Please enter a number between 1 and 8.")

main()
    
     