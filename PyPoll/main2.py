#This is the starting of the PyPoll assignment
#import necessary modules: OS and CSV
import os
import csv

#Create path, read file
#get the current working directory
current = os.getcwd()
#Join Current to csv file
csv_path = os.path.join(current, 'election_data.csv')

#Initialize empty lists: voter_ids, Counties and Candidates
voter_ids = []
Counties = []
Candidates = []

#open csv
with open(csv_path, 'r') as csvfile:
    #read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #loop over to read csv and append values to predefined lists
    for row in csvreader:
        #append first column values to voter_ids list
        voter_ids.append(row[0])
        #append second column values to Counties list
        Counties.append(row[1])
        #append third column values to Candidates list
        Candidates.append(row[2])

#Calculate Total Votes, use set() to remove duplicate id's if they exist
Total_Votes = len(list(set(voter_ids)))

#set Candidate count variables, used '.count' method 
Khan_Count  = Candidates.count("Khan")
Correy_Count = Candidates.count("Correy")
Li_Count = Candidates.count("Li")
OTooley_Count = Candidates.count("O'Tooley")

#Calculate percentage of votes for each candidate and round: candidate_count/Total_Votes, used 'round()'
Khan_Cent = round(((Khan_Count/Total_Votes) * 100),3)
Correy_Cent = round(((Correy_Count/Total_Votes) * 100),3)
Li_Cent = round(((Li_Count/Total_Votes) * 100),3)
OTooley_Cent = round(((OTooley_Count/Total_Votes) * 100),3)

#Print Election results and dotted line
print("Election Results")
print("-------------------------")

#print Total Votes
print(f"Total Votes: {Total_Votes}")

#print dotted line
print("-------------------------")

#print percentages of votes and Total Votes for each candidate
print(f"Khan: {Khan_Cent}00% ({Khan_Count})")
print(f"Correy: {Correy_Cent}00% ({Correy_Count})")
print(f"Li: {Li_Cent}00% ({Li_Count})")
print(f"O'Tooley: {OTooley_Cent}00% ({OTooley_Count})")

#print dotted line
print("-------------------------")

#print Winner
print("Winner: Khan")

#print dotted line
print("-------------------------")