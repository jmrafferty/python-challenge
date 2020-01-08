# First we'll import the os module
import os

# Module for reading CSV files
import csv

#Store csvpath as variable.
csvpath = os.path.join("Resources", "election_data.csv")


candidates_votes = []
file_to_output = os.path.join("Resources", "election_results.csv")

# Read w/ CSV Module
with open (csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    
    candidates = []
    candidate_votes = {}
    total_votes = 0
    
    #Set variable to hold winning vote count -- this position doesn't work.
    #winner's name is missing.
    #winning_count = 0
    
    
    #for row in csvreader:
        
        #candidates_votes.append(row)
        

    for i in csvreader:
        total_votes = total_votes + 1
        candidate_name = i[2]
        #vote = candidates_votes[i]        
        
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            #candidates_votes.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        else:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
          
    #print(candidates_votes) 
    
      

with open(file_to_output, "w") as txt_file:
    
    election_results = (f"\n\nElection Results\n"
    f"\n"
    f"Total Votes: {total_votes}\n"
    f"\n")
    print(election_results, end="")
    txt_file.write(election_results)

    #Set variables to hold winning vote count and candidate
    winning_count = 0
    winning_candidate = ""

    for candidate in candidate_votes:
    
    
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
    
    
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    
        #Print each candidates vote count & % to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end= "")
    
        #Save candidates' voter counts and %s to a txt file
        txt_file.write(voter_output)
    
        #Print winner to terminal
        winning_candidate_summary = (f"\n"
                                     f"Winner: {winning_candidate}\n"
                                     f"\n")
        
    #Print winner to txt file
    txt_file.write(winning_candidate_summary)

    
print(winning_candidate_summary)

     
#print(candidates)
#with open(file_to_output, "w") as txt_file:
    #Save candidates' voter counts and %s to a txt file
    #txt_file.write(voter_output)    
    