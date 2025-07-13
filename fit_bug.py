def view_tasks():
    try:
        with open("tasks.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("No tasks found.")
