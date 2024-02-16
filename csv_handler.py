import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def csv_operation(self, mode, data=None):
        if mode == 'r':
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                return list(reader)
        elif mode == 'w':
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        elif mode == 'a':
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        else:
            print("Invalid mode. Use 'r' for read, 'w' for write, or 'a' for append.")

