# Election Audit

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local elecetion.  Using the data provided in a csv file.


1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
[Election_Data](Resources/election_results.csv)

- Software Python 3.7.6, Visual Studio Code 1.51

## Results
Upon running the python script we can see that
the analysis shows:
- Total Votes Cast = 369,711
- The candidates who recieved votes were:
  - Charles Casper Stockham
  - Diana DeGette  
  - Raymon Anthony Doane
  
- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the vote.
    -   85,213 votes
  - Diana DeGette recieved 73.8% of the vote.
    -  272,892 votes
  - Raymon Anthony Doane 3.1% of the vote.
    -  11,606 votes
  
- **The winner of the election was:**
    - **Diana DeGette with 73.8% of the vote. 272,892 votes.**

## Challenge Overview

The election commission has requested some additional data to complete the audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

These results should be printed to the command line and saved election_results.txt file.  

## County Election Audit Results

The requested results for the challenge were as follows:

- Total Votes = 369,711

- Voter turnout for each county:
    - Jefferson = 38,855
    - Denver = 306,055
    - Arapahoe = 24,801

- Percentage of votes from each county:
    - Jefferson = 10.5% 
    - Denver = 82.8% 
    - Arapahoe = 6.7%

- **County with the highest turnout:**
    - **Denver had the highest turnout, 306,055 votes which is 82.8% of total votes cast.**

The county results along with the candidate results can be seen in the following output text file.

[Election Results Text File](analysis/election_analysis.txt)

The results will also be printed in the command line.  See screenshot below:

![ElectionResults](https://github.com/RussellShelley/Imagefiles/blob/main/ElectionResultsTerminal.png?raw=true)

## Election Audit Summary

This code has great potential to be reused in other elections.
It could be altered to work for ballots with multiple candidate races.  If more electoral positions were on the ballot, the voters choices could be returned on additional columns via the CSV file. We can modify the code so as to gather a seperate set of candidate data from the new columns [3] [4] etc. The loops we used to gather and then print data can be made into functions, which can be applied to each column. Additionaly we could modify the code to have a user input to determine how many races to return data from.

Another modification is to make the "file to open" an user input.  This can increase reusabilty by allowing the user to select any file to read from.