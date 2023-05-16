import os
import csv

absoulte_path = os.path.dirname(__file__)
csv_path = os.path.join(absoulte_path, 'Resources', 'election_data.csv')

# Read and print csv

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # set variables
    total_votes = 0
    candidates = {}
    max_votes = 0

    # loop through dataset
    for row in csvreader:
        print(row)
        total_votes += 1
        if row [2] in candidates:
            candidates[row[2]] +=1
        else: candidates[row[2]] =1    
    # loop through candidates
    for candidate in candidates:
        percent = (candidates[candidate]/total_votes) * 100
        candidates[candidate] = [percent, candidates[candidate]]

    for candidate, votes in candidates.items():
        if candidates[candidate][1] > max_votes:
            winner = candidate
            max_votes = candidates[candidate][1]
    names_of_candidates = list(candidates.keys())


# print results analysis
results = (f"Election Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------\n"
        f"{names_of_candidates[0]}: {round(candidates[names_of_candidates[0]][0], 3)}% ({candidates[names_of_candidates[0]][1]})\n"
        f"{names_of_candidates[1]}: {round(candidates[names_of_candidates[1]][0], 3)}% ({candidates[names_of_candidates[1]][1]})\n"
        f"{names_of_candidates[2]}: {round(candidates[names_of_candidates[2]][0], 3)}% ({candidates[names_of_candidates[2]][1]})\n"
        f"----------------------\n"
        f"winner: {winner}\n"
        f"----------------------\n")
print(results)
