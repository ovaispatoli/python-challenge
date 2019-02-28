#import modules/libraries
import os
import csv

#Create path, read file
current = os.getcwd()
csv_path = os.path.join(current, 'election_data.csv')

#The empty lists
voter_ids = []
Counties = []
Candidates = []

#open csv
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(csv_header)
    #loop over to read csv and assign values to predefined lists
    for row in csvreader:
        voter_ids.append(row[0])
        Counties.append(row[1])
        Candidates.append(row[2])

#Calculate Total Votes, use set() to remove duplicate id's if they exist
Total_Votes = len(list(set(voter_ids)))


#Print Election results and dotted line
#print("Election Results")
#print("---------------------")

#print Total Votes
print(f"Total Votes: {Total_Votes}")

#print dotted line
#print("---------------------")

#print percentages of votes and Total Votes for each candidate
#print(f"Khan: {} ({})")
#print(f"Correy: {} ({})")
#print(f"Li: {} ({})")
#print(f"O'Tooley: {} ({})")

#print Winner
#print(f"Winner: {}")

#print dotted line
#print("---------------------")