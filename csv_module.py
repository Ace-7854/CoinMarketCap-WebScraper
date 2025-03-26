"""
Module/class for making, and updating the csv
"""
import csv

class csv_module:
    def __init__(self,filepath):
        self.file = filepath
        self.header = "name"
    
    def write_to_file(self, data):
        with open(self, 'w', newline='') as csvfile:
            # Creating a CSV writer object
            csvwriter = csv.writer(csvfile)

            # Writing the field names
        csvwriter.writerow(self.header)

            # Writing the data rows
        csvwriter.writerows() #update
    
    def read_from_file(self):
        with open('', mode='r') as file:
            csvFile = csv.reader(file)

        for line in csvFile:
            print(line)