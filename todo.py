# todo.py - Simple CLI To-Do List App

tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Exit")


def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"✅ Task added: {task}")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"🗑️ Removed: {removed}")
        except:
            print("⚠️ Invalid task number.")

def edit_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to edit: "))
            if 1 <= num <= len(tasks):
                print(f"Current task: {tasks[num - 1]}")
                new_task = input("Enter updated task: ")
                tasks[num - 1] = new_task
                print("✏️ Task updated successfully.")
            else:
                print("❌ Task number out of range.")
        except:
            print("⚠️ Invalid input. Please enter a number.")

#Main Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        edit_task()
    elif choice == '5':
        print("👋 Exiting To-Do List. Bye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")

