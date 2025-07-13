# Example: add_task.py
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
