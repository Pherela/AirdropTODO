import csv
import os
from csv_handler import CSVHandler


class TodoApp:
    def __init__(self, filename):
        self.filename = filename
        self.ensure_file_exists()
        self.handler = CSVHandler(self.filename)

    def ensure_file_exists(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                pass

    def add_project(self, project_priority, project_name, project_category, task_priority, task_name, task_link):
        self.handler.append_csv([[project_priority, project_name, project_category, task_priority, task_name, task_link]])

    def add_task(self, project_name, task_priority, task_name, task_link):
        data = self.handler.read_csv()
        for row in data:
            if row[1] == project_name:
                task_data = [row[0], row[1], row[2], task_priority, task_name, task_link]
                self.handler.append_csv([task_data])

    def view_projects(self):
        data = list(self.handler.read_csv())
        seen = set()
        print('{:<8} {:<14} {:<8}'.format(*data[0]))
        for row in sorted(data[1:], key=lambda row: {'high': 1, 'medium': 2, 'low': 3}.get(row[0], 4)):
           if row[1] not in seen:
                print('{:<8} {:<14} {:<8}'.format(*row))
                seen.add(row[1])

    def view_tasks(self):
        data = list(self.handler.read_csv())
        print('{:<12} {:<14}'.format(*data[0][4:6]))
        for row in sorted(data[1:], key=lambda row: {'high': 1, 'medium': 2, 'low': 3}.get(row[3], 4)):
            clean_url = row[5].replace('http://', '').replace('https://', '').replace('www.', '')
            print('{:<12} {:<14}'.format(row[4], clean_url))

    def delete_project(self, project_name):
        tasks = self.handler.read_csv()
        new_tasks = [t for t in tasks if t[1] != project_name]
        self.handler.write_csv(new_tasks)

    def edit_string(self):
        data = self.handler.read_csv()
        old_string = input("Enter the old string you want to replace: ")
        new_string = input("Enter the new string: ")
        data = [[new_string if item == old_string else item for item in sublist] for sublist in data]
        self.handler.write_csv(data)
        print("The string has been successfully replaced.")



def main():
    app = TodoApp('tasks.csv')
    while True:
        print("\n".join([
            "1. add project",
            "2. add task",
            "3. view projects",
            "4. view tasks",
            "5. Edit project",
            "6. edit task",
            "7. edit link",
            "8. Quit",
        ]))
        option = input("Choose an option: ")

        if option == '1':
            project_name = input("Please enter the project name: ")
            project_priority = input("Please enter the project priority: ")
            project_category = input("Please enter the project category: ")
            task_name = input("Please enter the task name: ")
            task_priority = input("Please enter the task priority: ")
            task_link = input("Please enter the task link: ")
            app.add_project(project_priority, project_name, project_category, task_priority, task_name, task_link)
        elif option == '2':
            project_name = input("Please enter the project name: ")
            task_name = input("Please enter the task name: ")
            task_priority = input("Please enter the task priority: ")
            task_link = input("Please enter the task link: ")
            app.add_task(project_name, task_priority, task_name, task_link)
        elif option == '3':
            app.view_projects()
        elif option == '4':
            app.view_tasks()
        elif option == '5':
            app.edit_string()
        elif option == '6':
            app.edit_string()
        elif option == '7':
            app.edit_string()
        elif option == '8':
            break



if __name__ == "__main__":
    main()

