import csv
import os
PyPollcsv = os.path.join("C:\\Users\\14374\\Desktop\\Study\\python module3\\PyPoll\\Resources\\election_data.csv")

# Initialize variables
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV file
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Count the total number of votes and gather candidate data
    for row in csvreader:
        count += 1
        candidatelist.append(row[2])

    # Find unique candidates
    unique_candidate = list(set(candidatelist))

    # Calculate vote count and percentage
    for candidate in unique_candidate:
        votes = candidatelist.count(candidate)
        vote_count.append(votes)
        vote_percent.append((votes / count) * 100)

    # Find the winner
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

# Print to terminal
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {count}")
print("-------------------------")

for i in range(len(unique_candidate)):
    print(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})")

print("-------------------------")
print(f"The winner is: {winner}")
print("-------------------------")

# Print to a text file
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Vote: {count}\n")
    text.write("---------------------------------------\n")

    for i in range(len(unique_candidate)):
        text.write(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})\n")

    text.write("---------------------------------------\n")
    text.write(f"The winner is: {winner}\n")
    text.write("---------------------------------------\n")
