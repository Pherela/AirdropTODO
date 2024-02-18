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
        for row in sorted(data[1:], key=lambda row: {'high': 1, 'medium': 2, 'low': 3}.get(row[0], 4)):
            clean_url = row[5].replace('http://', '').replace('https://', '').replace('www.', '')
            print('{:<12} {:<14}'.format(row[4], clean_url))

    def delete_items(self, condition):
        self.handler.write_csv([item for item in self.handler.read_csv() if not condition(item)])

    def edit_string(self):
        old, new = input("Old string: "), input("New string: ")
        data = self.handler.read_csv()
        self.handler.write_csv([[new if i == old else i for i in s] for s in data])
        print("String replaced.")

def main():
    app = TodoApp('tasks.csv')
    while True:
        print("\n".join([f"{i}. {option}" for i, option in enumerate(["add project", "add task", "view project", "view task", "edit project", "edit task", "edit link", "delete project", "Quit"], start=1)]))
        option = input("Choose an option: ")

        if option == '1':
            app.add_project(*[input(f"Please enter the {field}: ") for field in ["project priority", "project name", "project category", "task priority", "task name", "task link"]])
        elif option == '2':
            app.add_task(*[input(f"Please enter the {field}: ") for field in ["project name", "task priority", "task name", "task link"]])
        elif option in ['3', '4']:
            getattr(app, ['view_projects', 'view_tasks'][int(option)-3])()
        elif option in ['5', '6', '7']:
            app.edit_string()
        elif option == '8':
            app.delete_items(lambda item: item[1] == input("Please enter the project name: "))
        elif option == '9':
            break

if __name__ == "__main__":
    main()

