import os
import csv

election_data = os.path.join("..", "RUTSOM201905DATA2", "Homework", "03-Python", "PyPoll", "Resources", "election_data.csv")

candidates = []
number_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1

    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_votes.append(percentage)

    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Resuts")
print(f"Total Votes: {str(total_votes)}")

for i in range(len(candidates)):
    print(f"{candidates[1]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print(f"Winner: {winning_candidate}")

output = open("output.text", "w")
line1 = "Election Results"
line2 = str(f"Total Votes: {str(total_votes)}")
output.write()
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    output.write()
line3 = str(f"Winner: {winning_candidate}")
output.write()

