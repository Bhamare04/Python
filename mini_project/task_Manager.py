import os



file_name = "tasks.txt"
def load_tasks():
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                tasks_id,title,status = line.strip().split(' | ')
                tasks[int(tasks_id)] = {'title': title, 'status': status}
                

    return tasks

            #save tasks to file
def save_tasks(tasks):
    with open(file_name, 'w') as f:
        for task_id, task in tasks.items():
            f.write(f"{task_id} | {task['title']} | {task['status']}\n")

            #add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {'title': title, 'status': 'pending'}
    print(f"Task '{title}' added with ID {task_id}.")

    #view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            print(f"ID: {task_id} | Title: {task['title']} | Status: {task['status']}")

    #mark a task as completed
def mark_task_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]['status'] = 'completed'
        print(f"Task ID {task_id} marked as completed.")
    else:
        print(f"Task ID {task_id} not found.")

#delete  a task

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    deleted_task = tasks.pop(task_id, None)
    if deleted_task:
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")

#main function to run the task manager
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()