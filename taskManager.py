# Simple Task Manager

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f'Task "{description}" added successfully!')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f'Task "{self.tasks[task_index].description}" marked as completed.')
        else:
            print("Invalid task index.")

    def show_menu(self):
        while True:
            print("\nTask Manager Menu")
            print("1. Add a New Task")
            print("2. View All Tasks")
            print("3. Mark a Task as Complete")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                description = input("Enter task description: ").strip()
                self.add_task(description)

            elif choice == '2':
                print("\nAll Tasks:")
                self.view_tasks()

            elif choice == '3':
                try:
                    task_index = int(input("Enter the task number to mark as complete: ")) - 1
                    self.mark_task_completed(task_index)
                except ValueError:
                    print("Please enter a valid task number.")

            elif choice == '4':
                print("Exiting Task Manager.")
                break

            else:
                print("Invalid choice. Please try again.")


# Run the Task Manager
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.show_menu()
