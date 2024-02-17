import csv
import os
from prettytable import PrettyTable
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
            if row['project_name'] == project_name:
                task_data = [row['project_priority'], row['project_category'], task_priority, task_name, task_link]
                self.handler.append_csv(task_data)

    def view_data(self):
        read = self.handler.read_csv()
        data = list(read)
        table = PrettyTable()
        table.align = 'l'
        order = {'high': 1, 'medium': 2, 'low': 3}
        data[1:] = sorted(data[1:], key=lambda row: order.get(row[0], 4))
        seen = set()
        for i, row in enumerate(data):
            if i == 0:
                table.field_names = [row[0], row[1], row[2]]
            elif row[1] not in seen:
                table.add_row([row[0], row[1], row[2]])
                seen.add(row[1])
        print(table)

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
            "2. Add task to existing project",
            "3. View projects",
            "4. Delete project",
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
            task_name = input("Please enter the task name: ")                                                   task_priority = input("Please enter the task priority: ")                                           task_link = input("Please enter the task link: ")
            app.add_task(project_name, task_priority, task_name, task_link)
        elif option == '3':
            app.view_data()
        elif option == '4':
            project = input("Enter a project to delete: ")
            print(app.delete_project(project))
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

