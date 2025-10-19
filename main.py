
def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet!\n")
    else:
        print("\n📋 Current To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "🕓"
            print(f"{i}. {task['title']} {status}")
        print()

def add_task(tasks):
    title = input("✏️ Enter a new task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!\n")

def complete_task(tasks):
    show_tasks(tasks)
    num = input("Enter the number of the task you completed: ")
    if num.isdigit() and 0 < int(num) <= len(tasks):
        tasks[int(num) - 1]["done"] = True
        print("🎉 Task marked as completed!\n")
    else:
        print("❌ Invalid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    num = input("Enter the number of the task to delete: ")
    if num.isdigit() and 0 < int(num) <= len(tasks):
        removed = tasks.pop(int(num) - 1)
        print(f"🗑️ Task deleted: {removed['title']}\n")
    else:
        print("❌ Invalid number.\n")

def main():
    tasks = []
    while True:
        print("=== To-Do List Manager ===")
        print("1️⃣ Show tasks")
        print("2️⃣ Add task")
        print("3️⃣ Complete task")
        print("4️⃣ Delete task")
        print("5️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option.\n")

if __name__ == "__main__":
    main()
