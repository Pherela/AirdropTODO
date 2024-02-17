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
        try:
            with open(self.filename, mode, newline='') as f:
                csv.writer(f).writerows(data)
        except Exception as e:
            print(f"An error occurred: {e}")

