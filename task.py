import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = []
            print(f"User '{username}' created successfully.")
        else:
            print("User already exists.")

    def add_task(self, username, task, priority=1, due_date=None, category=None):
        if username in self.users:
            task_info = {
                "task": task,
                "priority": priority,
                "due_date": due_date,
                "category": category
            }
            self.users[username].append(task_info)
            print("Task added successfully.")
        else:
            print("User not found.")

    def remove_task(self, username, task_index):
        if username in self.users and task_index < len(self.users[username]):
            del self.users[username][task_index]
            print("Task removed successfully.")
        else:
            print("Invalid user or task index.")

    def display_tasks(self, username):
        if username in self.users:
            tasks = self.users[username]
            if tasks:
                print("Tasks:")
                for i, task_info in enumerate(tasks, start=1):
                    print(f"{i}. {task_info['task']} - Priority: {task_info['priority']}, Due Date: {task_info['due_date']}, Category: {task_info['category']}")
            else:
                print("No tasks.")
        else:
            print("User not found.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.users, file)
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.users = json.load(file)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
...         except json.JSONDecodeError:
...             print("Invalid JSON format.")
... 
... def main():
...     todo_list = TodoList()
...     while True:
...         print("\n1. Add User\n2. Add Task\n3. Remove Task\n4. Display Tasks\n5. Save Tasks\n6. Load Tasks\n7. Exit")
...         choice = input("Enter your choice: ")
... 
...         if choice == '1':
...             username = input("Enter username: ")
...             todo_list.add_user(username)
...         elif choice == '2':
...             username = input("Enter username: ")
...             task = input("Enter task: ")
...             priority = int(input("Enter priority (1-5): "))
...             due_date = input("Enter due date (YYYY-MM-DD): ")
...             category = input("Enter category: ")
...             todo_list.add_task(username, task, priority, due_date, category)
...         elif choice == '3':
...             username = input("Enter username: ")
...             task_index = int(input("Enter task index to remove: ")) - 1
...             todo_list.remove_task(username, task_index)
...         elif choice == '4':
...             username = input("Enter username: ")
...             todo_list.display_tasks(username)
...         elif choice == '5':
...             filename = input("Enter filename to save tasks: ")
...             todo_list.save_tasks(filename)
...         elif choice == '6':
...             filename = input("Enter filename to load tasks: ")
...             todo_list.load_tasks(filename)
...         elif choice == '7':
...             print("Exiting program.")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
...     main()
