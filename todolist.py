class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' has been added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")
    
    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo.add_task(task)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo.delete_task(task_number)
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
