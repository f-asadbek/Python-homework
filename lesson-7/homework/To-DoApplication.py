import json
import csv


class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'No Due Date'}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


class TaskManager:
    def __init__(self, file_format='txt'):
        self.tasks = []
        self.file_format = file_format.lower()
        self.filename = f"tasks.{self.file_format}"
        self.load_tasks()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) or leave blank: ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"

        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new title: ") or task.title
                task.description = input("Enter new description: ") or task.description
                task.due_date = input("Enter new due date (YYYY-MM-DD) or leave blank: ") or task.due_date
                task.status = input("Enter new status (Pending/In Progress/Completed): ") or task.status
                self.save_tasks()
                print("Task updated successfully!\n")
                return
        print("Task not found!\n")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()
        print("Task deleted successfully!\n")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print("No tasks found with that status.")
        else:
            for task in filtered:
                print(task)

    def save_tasks(self):
        if self.file_format == 'txt':
            with open(self.filename, 'w') as f:
                for task in self.tasks:
                    f.write(f"{task.task_id},{task.title},{task.description},{task.due_date or ''},{task.status}\n")
        elif self.file_format == 'json':
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        elif self.file_format == 'csv':
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                for task in self.tasks:
                    writer.writerow(task.to_dict())

    def load_tasks(self):
        try:
            if self.file_format == 'txt':
                with open(self.filename, 'r') as f:
                    for line in f:
                        task_id, title, description, due_date, status = line.strip().split(',')
                        self.tasks.append(Task(task_id, title, description, due_date or None, status))
            elif self.file_format == 'json':
                with open(self.filename, 'r') as f:
                    self.tasks = [Task(**task) for task in json.load(f)]
            elif self.file_format == 'csv':
                with open(self.filename, 'r') as f:
                    reader = csv.DictReader(f)
                    self.tasks = [Task(**row) for row in reader]
        except FileNotFoundError:
            pass  # No tasks file exists yet

    def run(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.filter_tasks()
            elif choice == '6':
                self.save_tasks()
                print("Tasks saved successfully!")
            elif choice == '7':
                self.load_tasks()
                print("Tasks loaded successfully!")
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    file_format = input("Choose file format (txt/json/csv): ")
    manager = TaskManager(file_format)
    manager.run()
