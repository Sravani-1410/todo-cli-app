# 📝 To-Do List CLI App (Python)

This is a simple Command Line Interface (CLI) To-Do List application built using Python.  
It allows users to add, view, edit, and delete tasks directly from the terminal.

---

## 📌 Features

- ✅ Add tasks
- 📋 View task list
- 🗑️ Delete tasks by number
- ✏️ Edit existing tasks
- ❎ Exit the app anytime

---

## 💻 Technologies Used

- Python 3.x (Core only – no external libraries)

---

## 🛠️ How to Run

1. Clone the repository:
git clone https://github.com/yourusername/todo-cli-app.git
cd todo-cli-app

markdown
Copy
Edit

2. Run the script:
python todo.py

yaml
Copy
Edit

3. Follow the menu prompts to interact with your task list.

---

## 📂 Example Output

```text
----- TO-DO LIST MENU -----
1. Add Task
2. View Tasks
3. Delete Task
4. Edit Task
5. Exit

Enter your choice: 1
Enter new task: Learn Python
✅ Task added: Learn Python

Enter your choice: 2
📋 Your Tasks:
1. Learn Python
🖊️ Edit Task Example
text
Copy
Edit
Enter your choice (1-5): 4
📋 Your Tasks:
1. Learn Python
2. Finish GitHub Project

Enter task number to edit: 2
Current task: Finish GitHub Project
Enter updated task: Upload resume project
✏️ Task updated successfully.
