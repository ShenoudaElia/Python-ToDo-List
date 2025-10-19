# Simple To-Do List Manager

# Created for learning purposes in Python



def display_tasks(my_tasks):

  """Display all current tasks"""

  if not my_tasks:

    print("\n📭 No tasks available!\n")

  else:

    print("\n📋 Current To-Do List:")

    for idx, item in enumerate(my_tasks, start=1):

      status = "✅" if item['completed'] else "🕓"

      print(f"{idx}. {item['title']} {status}")

    print()



def add_new_task(my_tasks):

  """Add a new task to the list"""

  title = input("✏️ Enter the new task: ")

  my_tasks.append({"title": title, "completed": False})

  print("Task added successfully!\n")



def mark_task_done(my_tasks):

  """Mark a task as completed"""

  display_tasks(my_tasks)

  num = input("Enter the number of the completed task: ")

  if num.isdigit() and 0 < int(num) <= len(my_tasks):

    my_tasks[int(num) - 1]["completed"] = True

    print("🎉 Task marked as completed!\n")

  else:

    print("❌ Invalid number.\n")



def remove_task(my_tasks):

  """Remove a task from the list"""

  display_tasks(my_tasks)

  num = input("Enter the number of the task to remove: ")

  if num.isdigit() and 0 < int(num) <= len(my_tasks):

    removed = my_tasks.pop(int(num) - 1)

    print(f"🗑️ Task removed: {removed['title']}\n")

  else:

    print("❌ Invalid number.\n")



def main_menu():

  """Main menu to run the program"""

  tasks_list = []

  while True:

    print("=== To-Do List Manager ===")

    print("1️⃣ Show tasks")

    print("2️⃣ Add task")

    print("3️⃣ Complete task")

    print("4️⃣ Delete task")

    print("5️⃣ Exit")

    choice = input("Choose an option: ")



    if choice == "1":

      display_tasks(tasks_list)

    elif choice == "2":

      add_new_task(tasks_list)

    elif choice == "3":

      mark_task_done(tasks_list)

    elif choice == "4":

      remove_task(tasks_list)

    elif choice == "5":

      print("👋 Exiting program. Goodbye!")

      break

    else:

      print("❌ Invalid option.\n")



if __name__ == "__main__":

  main_menu()

