#This is the starting of the Pybank Project
#import necessary modules
import os
import csv

#Create path, read file
current = os.getcwd()
csv_path = os.path.join(current,'budget_data.csv')

#initialize an empty months list, Profit_Losses list, Profit_Changes list
Months = []
Profit_Losses = []
Changes = []
counter = 0
total_count = 0

#open csv
with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
         Months.append(row[0])
         Profit_Losses.append(int(row[1]))

#Loop over Profit_Losses
for value in range(len(Profit_Losses)):
    if counter == 12:
        #store indexing into variable
        values = Profit_Losses[total_count:(total_count + counter)]
        #append to changes list
        Changes.append(sum(values)/len(values))
        #Add to total count
        total_count = total_count + counter
        #Reset counter
        counter = 0
    else:
        counter = counter + 1

#calculate net profits by summing up values in the list
Net = sum(Profit_Losses)

#Total Months
Total_Months = len(Months)

#Greatest Increase/Decrease
Greatest_Increase = max(Profit_Losses)
Greatest_Decrease = min(Profit_Losses)

#getting the dates associated with the Greatest
index_1 = Profit_Losses.index(Greatest_Increase)
index_2 = Profit_Losses.index(Greatest_Decrease)

#getting the values from Months[]
Month_1 = Months[index_1]
Month_2 = Months[index_2]

#Initial print statements
print("Financial Analysis")
print("------------------------")
#Other print statements
print(f"Total Months: ",Total_Months)
print(f"Total: ${Net}")
#print(round(sum(Changes)/len(Changes),2))
print(f"Greatest Increase in Profits: {Month_1} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Month_2} (${Greatest_Decrease})")
