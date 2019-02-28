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
    print(csv_header)
    for row in csvreader:
        voter_ids.append(row[0])
        Counties.append(row[1])
        Candidates.append(row[2])

#test print
print(voter_ids[0],Counties[0], Candidates[0])