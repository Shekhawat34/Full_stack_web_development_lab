def view_tasks():
    with open("nonexistent_file.txt") as f:  # Intentional bug
        print(f.read())
