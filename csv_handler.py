import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        try:
            with open(self.filename, 'r') as f:
                return list(csv.reader(f))
        except Exception as e:
            print(f"An error occurred: {e}")

    def write_csv(self, data):
        if data:
            self._write_data(data, 'w')
        else:
            print("No data provided for writing.")

    def append_csv(self, data):
        if data:
            self._write_data(data, 'a')
        else:
            print("No data provided for appending.")

    def _write_data(self, data, mode):
        if isinstance(data, list) and all(isinstance(row, list) for row in data):
            try:
                with open(self.filename, mode, newline='') as f:
                    csv.writer(f).writerows(data)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid data format. Please provide a list of lists where each inner list represents a row.")

