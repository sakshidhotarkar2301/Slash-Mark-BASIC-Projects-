import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = 'Completed' if task['completed'] else 'Not Completed'
                print(f"{i}. {task['name']} - {status}")

    def add_task(self):
        task_name = input("Enter the task name: ")
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"Task '{task_name}' added to your to-do list.")

    def mark_completed(self):
        if self.display_and_select_task():
            print(f"Task '{self.selected_task['name']}' marked as completed.")
            self.selected_task['completed'] = True

    def remove_task(self):
        if self.display_and_select_task():
            removed_task = self.tasks.pop(self.selected_task_index)
            print(f"Task '{removed_task['name']}' removed from your to-do list.")

    def display_and_select_task(self):
        self.display_tasks()
        task_number = self.get_task_number()
        if task_number is not None:
            self.selected_task_index = task_number - 1
            self.selected_task = self.tasks[self.selected_task_index]
            return True
        return False

    def get_task_number(self):
        try:
            task_number = int(input("Enter the task number: "))
            if 1 <= task_number <= len(self.tasks):
                return task_number
            print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        return None


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application Menu:")
        menu_options = [
            "Display To-Do List",
            "Add a Task",
            "Mark a Task as Completed",
            "Remove a Task",
            "Quit"
        ]
        for i, option in enumerate(menu_options, 1):
            print(f"{i}. {option}")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            todo_list.add_task()
        elif choice == '3':
            todo_list.mark_completed()
        elif choice == '4':
            todo_list.remove_task()
        elif choice == '5':
            print("Exiting the To-Do List Application. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
