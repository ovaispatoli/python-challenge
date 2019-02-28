#This is the starting of the Pybank Project
#import necessary modules
import os
import csv

#Create path, read file
current = os.getcwd()
csv_path = os.path.join(current,'budget_data.csv')

#initialize an empty months list
Months = []

#open csv
with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        

#Total Months
Total_Months = len(Months)
print(f"Total Months: ",Total_Months)