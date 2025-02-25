import json
import csv
import os


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class StorageStrategy:
    def save(self, tasks, filename):
        pass

    def load(self, filename):
        pass


class JSONStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, "w") as file:
            json.dump([task.__dict__ for task in tasks], file)

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return [Task(**data) for data in json.load(file)]


class CSVStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["task_id", "title", "description", "due_date", "status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return [Task(**row) for row in reader]


class ToDoManager:
    def __init__(self, storage_strategy):
        self.storage = storage_strategy
        self.tasks = self.storage.load("tasks.txt")

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.storage.save(self.tasks, "tasks.txt")
        print("Tasks saved successfully!")

    def menu(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
                status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                self.add_task(Task(task_id, title, description, due_date, status))
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new title (press Enter to keep current): ") or None
                description = input("Enter new description (press Enter to keep current): ") or None
                due_date = input("Enter new due date (press Enter to keep current): ") or None
                status = input("Enter new status (press Enter to keep current): ") or None
                self.update_task(task_id, title, description, due_date, status)
            elif choice == "4":
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)
            elif choice == "5":
                status = input("Enter status to filter by: ")
                self.filter_tasks(status)
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.tasks = self.storage.load("tasks.txt")
                print("Tasks loaded successfully!")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    storage_type = input("Choose storage format (json/csv): ")
    storage = JSONStorage() if storage_type == "json" else CSVStorage()
    manager = ToDoManager(storage)
    manager.menu()
