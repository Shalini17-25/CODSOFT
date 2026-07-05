tasks = []

def show():
    if not tasks:
        print("No tasks.")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['name']}")

def add():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print("Task added.")

def complete():
    show()
    n = int(input("Enter task number to mark done: "))
    if 1 <= n <= len(tasks):
        tasks[n-1]["done"] = True
        print("Marked done.")
    else:
        print("Invalid number.")

def delete():
    show()
    n = int(input("Enter task number to delete: "))
    if 1 <= n <= len(tasks):
        tasks.pop(n-1)
        print("Deleted.")
    else:
        print("Invalid number.")

while True:
    print("\n1. View  2. Add  3. Complete  4. Delete  5. Exit")
    c = input("Choose: ")
    if c == '1':
        show()
    elif c == '2':
        add()
    elif c == '3':
        complete()
    elif c == '4':
        delete()
    elif c == '5':
        break
    else:
        print("Invalid choice")