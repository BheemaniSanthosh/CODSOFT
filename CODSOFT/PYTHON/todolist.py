class Task:
    def _init_(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def _str_(self):
        status = "completed" if self.completed else "not completed"
        return f"[{status}] {self.description}"

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def update_task(self, index, new_description):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index].description = new_description
            print(f"Updated task {index} to: {new_description}")
        else:
            print(f"Task {index} not found")

    def complete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Completed task {index}")
        else:
            print(f"Task {index} not found")

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

def print_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Complete Task")
    print("4. List Tasks")
    print("5. Exit")

def main():
    todo_list = ToDoList()
    
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter the task index to update: "))
            new_description = input("Enter the new description: ")
            todo_list.update_task(index, new_description)
        elif choice == '3':
            index = int(input("Enter the task index to complete: "))
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()