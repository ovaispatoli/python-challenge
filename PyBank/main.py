#This is the starting of the Pybank Project
#import necessary modules
import os
import csv

#Create path, read file
current = os.getcwd()
csv_path = os.path.join(current,'budget_data.csv')
#print(csv_path)

with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ')
    csv_header = next(csvreader)
    for row in csvreader:
        print(row)
        