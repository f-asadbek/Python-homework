import json
import csv

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTasks:")
    print(f"{'ID':<5} {'Task':<20} {'Completed':<10} {'Priority':<5}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<5}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    tasks = load_tasks(json_filename)

    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

    print(f"\nTasks saved to {csv_filename}")

def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    json_to_csv()


if __name__ == "__main__":
    main()
