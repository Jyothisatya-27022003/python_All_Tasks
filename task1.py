# To-Do List Application using Python

# Class to represent a Task
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False  # Default status

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️ Completed" if self.completed else "❌ Not Completed"
        return f"{self.description} - {status}"


# Main Application Class
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = Task(description)
        print(f"✅ Task '{description}' added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.\n")
            return
        print("\n📝 Your Tasks:")
        for task_id, task in self.tasks.items():
            print(f"{task_id}. {task}")
        print()

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completed()
            print(f"✅ Task '{self.tasks[task_id].description}' marked as completed!\n")
        else:
            print("⚠️ Invalid Task ID!\n")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            removed = self.tasks.pop(task_id)
            print(f"🗑️ Task '{removed.description}' deleted successfully!\n")
        else:
            print("⚠️ Invalid Task ID!\n")


# -------------------------
# User Interface (Menu Loop)
# -------------------------
def main():
    todo = ToDoList()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_task_completed(task_id)
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "4":
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please select a number between 1 and 5.\n")


# Run the program
if __name__ == "__main__":
    main()
