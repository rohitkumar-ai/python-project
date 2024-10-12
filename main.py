# To-Do List Application

# Function to view tasks
def view_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        if tasks:
            print("Your Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
        else:
            print("No tasks added yet.")

# Function to add a task
def add_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(f"{task}\n")
    print(f"Task '{task}' added!")

# Function to remove a task
def remove_task(task_num):
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)
        print(f"Task '{removed_task.strip()}' removed!")
    else:
        print("Invalid task number.")

# Main application loop
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_num = int(input("Enter task number to remove: "))
            remove_task(task_num)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
