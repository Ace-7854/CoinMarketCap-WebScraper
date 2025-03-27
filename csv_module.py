"""
Module/class for making, and updating the csv
"""
import csv

class csv_module:
    def __init__(self,filepath):
        self.file = filepath
        self.header = ["Name","Abbreviation"]
    
    def write_to_file(self, data):
        try:
            with open(self.file, 'w', newline='') as csvfile:
                # Creating a CSV writer object
                csvwriter = csv.writer(csvfile)

                # Writing the field names
                csvwriter.writerow(self.header)

                csvwriter.writerows(data)
        except Exception as e:
            print(f"Error in Csv_writer: {e}")
            
    
    def read_from_file(self):
        with open(self.file, mode='r') as file:
            csvFile = csv.reader(file)

        for line in csvFile:
            print(line)