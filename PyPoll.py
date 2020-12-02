#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates that received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join ("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize a counter
total_votes = 0
#Declare candidate list
candidate_options = []
#Declare candidate vote dictionary
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Print the header row.
    headers = next(file_reader)
   
    #print each row in CSV file
    for row in file_reader:
        #Add to total vote count.
        total_votes += 1
        #Print candidate name from each row
        candidate_name = row[2]
        #If candididate does not match existing...
        if candidate_name not in candidate_options:
            #Add candidate_name to candidate_options
            candidate_options.append(candidate_name)
            #Begin tracking the candidates vote
            candidate_votes[candidate_name] = 0
        #Increment votes for candidate in dict.
        candidate_votes[candidate_name] += 1
        
    #Save results to our text file.
with open(file_to_save, "w") as txt_file:
        
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    #Save final vote count to the text file.
    txt_file.write(election_results)    
       
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes =candidate_votes[candidate_name]
        #Calculate percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #print candidate name and percentage of votes.
        #Make variable candidate_results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to text file
        txt_file.write(candidate_results)     
        # print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percent =
                #vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #And set the winning candidate equal to candidates name.
            winning_candidate = candidate_name

    #Print each candidates name, vote count, and percentage to terminal.
            # print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n)")
            
                     
    winning_candidate_summary =(
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary) 
    # Save th ewinning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    #Print the candidate list
    #print(candidate_options)
    #Print the total votes.
    #print(total_votes)
    #Print candidate vote dictionary.
    #print(candidate_votes)

#---------------------
# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
    #Write some data to  the file.
 #   txt_file.write("Counties in the Election\n")
  #  txt_file.write("--------------------------\nArapahoe\nDenver\nJefferson ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")



