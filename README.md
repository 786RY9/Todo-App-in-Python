# Todo CLI App

A simple command-line todo list application written in Python that allows you to manage your tasks efficiently.

## Features

- ✅ Add new tasks
- 📋 View all tasks with status indicators
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks
- 🚪 Exit the application

## Demo

![Todo CLI Demo](demo/todo_cli_demo_python.gif)

## How to Use

1. Run the application:
   ```bash
   python todo_app_cli.py
   ```

2. Choose from the following options:
   - **1**: Add Task - Enter a new task to your list
   - **2**: View Tasks - Display all tasks with their completion status
   - **3**: Mark Task as Done - Mark a specific task as completed
   - **4**: Delete Task - Remove a task from your list
   - **5**: Exit - Close the application

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Run the application:
   ```bash
   python todo_app_cli.py
   ```

## File Structure

```
├── todo_app_cli.py    # Main application file
├── test.py           # Test file for development
├── demo/
│   └── todo_cli_demo_python.gif  # Demo GIF
└── .vscode/
    └── settings.json  # VS Code settings
```

## Usage Example

```
--- TO-DO LIST ---

1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit

Enter your choice: 1
Enter new task: Buy groceries
Task added!
```

## Error Handling

The application includes error handling for:
- Invalid input (non-numeric choices)
- Non-existent task numbers
- Out-of-range menu selections