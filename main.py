import csv
import os

class TodoApp:
    def __init__(self, filename):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                pass

    def get_input(self, prompt, input_type=str):
        while True:
            try:
                value = input_type(input(prompt))
                return value
            except ValueError:
                print(f"Invalid input. Please enter a {input_type.__name__}.")

    def get_links(self, num_links):
        return [self.get_input(f"Enter link {i+1}: ") for i in range(num_links)]

    def add_task(self, task):
        num_links = self.get_input(f"Enter the number of links for task '{task}': ", int)
        links = self.get_links(num_links)
        return [task] + links

    def add_project(self, tasks, project, category, priority):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            for task in tasks:
                task_info = self.add_task(task)
                writer.writerow([project, category, priority] + task_info)

    def add_task_to_project(self, project):
        task = input(f"Enter a new task for project '{project}': ")
        num_links = self.get_input(f"Enter the number of links for task '{task}': ", int)
        links = self.get_links(num_links)
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([project, task] + links)

    def view_tasks(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(f'Project: {row[0]}, Category: {row[1]}, Priority: {row[2]}, Task: {row[3]}, Links: {", ".join(row[4:])}')

    def delete_project(self, project):
        tasks = self.read_tasks()
        new_tasks = [t for t in tasks if t[0] != project]
        self.write_tasks(new_tasks)

    def edit_project(self, old_project, new_project):
        tasks = self.read_tasks()
        for t in tasks:
            if t[0] == old_project:
                t[0] = new_project
        self.write_tasks(tasks)

    def edit_task(self, project, old_task, new_task):
        tasks = self.read_tasks()
        for t in tasks:
            if t[0] == project and t[3] == old_task:
                t[3] = new_task
        self.write_tasks(tasks)

    def edit_task_link(self, project, task):
        tasks = self.read_tasks()
        for t in tasks:
            if t[0] == project and t[3] == task:
                num_links = self.get_input(f"Enter the number of new links for task '{task}': ")
                links = self.get_links(num_links)
                t[4:] = links
        self.write_tasks(tasks)

    def read_tasks(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def write_tasks(self, tasks):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

def main():
    app = TodoApp('tasks.csv')
    while True:
        print("\n".join([
            "1. Add project",
            "2. Add task to existing project",
            "3. View tasks",
            "4. Delete project",
            "5. Edit project",
            "6. Edit task",
            "7. Edit task link",
            "8. Quit",
        ]))
        option = app.get_input("Choose an option: ")

        if option == '1':
            num_projects = app.get_input("Enter the number of projects: ", int)
            for j in range(num_projects):
                project = input(f"Enter project {j+1}: ")
                category = input(f"Enter a category for the project: ")
                priority = input(f"Enter a priority for the project: ")
                num_tasks = app.get_input("Enter the number of tasks: ", int)
                tasks = [input(f"Enter task {i+1}: ") for i in range(num_tasks)]
                app.add_project(tasks, project, category, priority)
        elif option == '2':
            project = input("Enter the project to add a task to: ")
            app.add_task_to_project(project)
        elif option == '3':
            app.view_tasks()
        elif option == '4':
            project = input("Enter a project to delete: ")
            print(app.delete_project(project))
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

