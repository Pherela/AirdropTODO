import csv
import os

class TodoApp:
    def __init__(self, filename):
        self.filename = filename
        # Check if file exists, if not, create it
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                pass

    def add_project(self, tasks, project, category):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            for task in tasks:
                while True:
                    try:
                        num_links = int(input(f"Enter the number of links for task '{task}': "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                links = []
                for i in range(num_links):
                    link = input(f"Enter link {i+1} for task '{task}': ")
                    links.append(link)
                writer.writerow([project, category, task] + links)

    def add_task_to_project(self, project):
        tasks = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            tasks = list(reader)
        project_exists = any(t[0] == project for t in tasks)
        if not project_exists:
            print(f"Project {project} does not exist.")
            return
        task = input(f"Enter a new task for project '{project}': ")
        category = [t[1] for t in tasks if t[0] == project][0]
        while True:
            try:
                num_links = int(input(f"Enter the number of links for task '{task}': "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        links = []
        for i in range(num_links):
            link = input(f"Enter link {i+1} for task '{task}': ")
            links.append(link)
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([project, category, task] + links)

    def view_tasks(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(f'Project: {row[0]}, Category: {row[1]}, Task: {row[2]}, Links: {", ".join(row[3:])}')

    def delete_project(self, project):
        tasks = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            tasks = list(reader)
        new_tasks = [t for t in tasks if t[0] != project]
        if len(tasks) == len(new_tasks):
            return f'Project {project} does not exist.'
        else:
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(new_tasks)
            return f'Project {project} has been deleted.'

    def edit_project(self, old_project, new_project):
        tasks = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            tasks = list(reader)
        for i, t in enumerate(tasks):
            if t[0] == old_project:
                t[0] = new_project
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

    def edit_task(self, project, old_task, new_task):
        tasks = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            tasks = list(reader)
        for i, t in enumerate(tasks):
            if t[0] == project and t[2] == old_task:
                t[2] = new_task
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

    def edit_task_link(self, project, task):
        tasks = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            tasks = list(reader)
        for i, t in enumerate(tasks):
            if t[0] == project and t[2] == task:
                while True:
                    try:
                        num_links = int(input(f"Enter the number of new links for task '{task}': "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                links = []
                for j in range(num_links):
                    link = input(f"Enter new link {j+1} for task '{task}': ")
                    links.append(link)
                t[3:] = links
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

def main():
    app = TodoApp('tasks.csv')
    while True:
        print("1. Add project")
        print("2. Add task to existing project")
        print("3. View tasks")
        print("4. Delete project")
        print("5. Edit project")
        print("6. Edit task")
        print("7. Edit task link")
        print("8. Quit")
        option = input("Choose an option: ")
        if option == '1':
            while True:
                try:
                    num_projects = int(input("Enter the number of projects: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            for j in range(num_projects):
                project = input(f"Enter project {j+1}: ")
                category = input(f"Enter a category for the project: ")
                while True:
                    try:
                        num_tasks = int(input("Enter the number of tasks: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                tasks = []
                for i in range(num_tasks):
                    task = input(f"Enter task {i+1}: ")
                    tasks.append(task)
                app.add_project(tasks, project, category)
        elif option == '2':
            project = input("Enter the project to add a task to: ")
            app.add_task_to_project(project)
        elif option == '3':
            app.view_tasks()
        elif option == '4':
            project = input("Enter a project to delete: ")
            result = app.delete_project(project)
            print(result)
        elif option == '5':
            old_project = input("Enter the project to edit: ")
            new_project = input("Enter the new project: ")
            app.edit_project(old_project, new_project)
        elif option == '6':
            project = input("Enter the project of the task to edit: ")
            old_task = input("Enter the task to edit: ")
            new_task = input("Enter the new task: ")
            app.edit_task(project, old_task, new_task)
        elif option == '7':
            project = input("Enter the project of the task to edit the link: ")
            task = input("Enter the task to edit the link: ")
            app.edit_task_link(project, task)
        elif option == '8':
            break

if __name__ == "__main__":
    main()

