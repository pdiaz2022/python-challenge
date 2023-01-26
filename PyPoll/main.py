import os
import csv

# path = "C:/Users/pedia/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv"
csvpath = os.path.join ('Resources', 'election_data.csv')

output_file = os.path.join('Analysis','election_data.txt')

# Define variables: 
# Total number of votes cast 
total_votes = 0

# List of candidates who received votes 
Active_candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

# Total number and % of votes for each candidate 
Charles_total_votes = 0 
Diana_total_votes = 0
Raymon_total_votes = 0 
Charles_percentage_votes = 0 
Diana_percentage_votes = 0 
Raymon_percentage_votes = 0 
candidate = []


# Open & read csv file 
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
    
    # Total number of votes
        
        total_votes = total_votes + 1

    # The total number of votes each candidate won
        if row[2] == "Charles Casper Stockham":
            Charles_total_votes = Charles_total_votes + 1
        elif row[2] == "Diana DeGette":
            Diana_total_votes = Diana_total_votes + 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_total_votes = Raymon_total_votes + 1
        
            # The percentage of votes each candidate won     
        Charles_percentage_votes = round((Charles_total_votes/total_votes)*100,3)
        Diana_percentage_votes = round((Diana_total_votes/total_votes)*100,3)
        Raymon_percentage_votes = round((Raymon_total_votes/total_votes)*100,3)

        candvotes= [Charles_total_votes, Diana_total_votes, Raymon_total_votes]
    
    # print (max(candvotes))

    maxvotes = max(candvotes)
    if maxvotes == candvotes[0]:
        winner = "Charles Casper Stockham"
    elif maxvotes == candvotes[1]:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

      
              
    #Print the results
    print ("Election results")
    print ("------------------")
    print ("Total votes:" + str(total_votes))
    print ("------------------")
    print ("Total number of votes each candidate won")
    print ("Charles Casper Stockham:" + str(Charles_percentage_votes)+"%" + " ("+str(Charles_total_votes)+")")
    print ("Diana DeGette: " + str(Diana_percentage_votes) +"%" + " ("+str(Diana_total_votes)+")")
    print ("Raymon Anthony Doane: " + str(Raymon_percentage_votes) +"%" + " ("+str(Raymon_total_votes)+")")
    print ("------------------")
    print(f"Winner: {winner}")
 
# exporting file 

export = open(output_file,'w')

export.write("Election results" + "\n")
export.write("------------------" + "\n")
export.write("Total votes:" + str(total_votes)+ "\n")
export.write("------------------" + "\n")
export.write("Total number of votes each candidate won" + "\n")
export.write("Charles Casper Stockham:" + str(Charles_percentage_votes)+"%" + " ("+str(Charles_total_votes)+")" + "\n")
export.write("Diana DeGette: " + str(Diana_percentage_votes) +"%" + " ("+str(Diana_total_votes)+")" + "\n")
export.write("Raymon Anthony Doane: " + str(Raymon_percentage_votes) +"%" + " ("+str(Raymon_total_votes)+")" + "\n")
export.write("------------------" + "\n")
export.write(f"Winner: {winner}" + "\n")
