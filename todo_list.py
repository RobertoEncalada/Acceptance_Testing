class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'status': 'Pending'})

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['status'] = 'Completed'
                return
        raise ValueError(f'Task "{task}" not found in the to-do list')

    def delete_task(self, task):
        for t in self.tasks:
            if t['task'] == task:
                self.tasks.remove(t)
                return
        raise ValueError(f'Task "{task}" not found in the to-do list')

    def clear_tasks(self):
        self.tasks = []

def print_tasks(tasks):
    if not tasks:
        print("The to-do list is empty.")
    else:
        for t in tasks:
            print(f"Task: {t['task']}, Status: {t['status']}")

if __name__ == "__main__":
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Clear all tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print(f'Task "{task}" added.')
        elif choice == '2':
            print("To-Do List:")
            print_tasks(todo_list.list_tasks())
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            try:
                todo_list.complete_task(task)
                print(f'Task "{task}" marked as completed.')
            except ValueError as e:
                print(e)
        elif choice == '4':
            task = input("Enter the task to delete: ")
            try:
                todo_list.delete_task(task)
                print(f'Task "{task}" deleted.')
            except ValueError as e:
                print(e)
        elif choice == '5':
            todo_list.clear_tasks()
            print("All tasks cleared.")
        elif choice == '6':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
