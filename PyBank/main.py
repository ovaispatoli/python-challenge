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
Profit_Changes = []
counter = 0

#open csv
with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
         Months.append(row[0])
         Profit_Losses.append(int(row[1]))

#Loop over Profit_Losses
for row in Profit_Losses:
    if counter > 0:
        #store the two values in value_1 and value_2 
        value_1 = Profit_Losses[(counter - 1)]
        value_2 = Profit_Losses[counter]
        #Calculate Monthly_Change = month2 - month1
        Monthly_Change = value_2 - value_1
        #Append to Profit_Changes list
        Profit_Changes.append(Monthly_Change)
        #add to counter
        counter = counter + 1
    else:
        #add to counter
        counter = counter + 1

#calculate net profits by summing up values in the list
Net = sum(Profit_Losses)

#Total Months
Total_Months = len(Months)

#Calculate Average Change
Average_Change = round(sum(Profit_Changes)/len(Profit_Changes),2)

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

#Print Total Months
print(f"Total Months: ",Total_Months)

#Print Net Profits
print(f"Total: ${Net}")

#Print Average Change
print(f"Average Change: ${Average_Change}")

#Print Greatest Increase and Greatest Decrease
print(f"Greatest Increase in Profits: {Month_1} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Month_2} (${Greatest_Decrease})")
