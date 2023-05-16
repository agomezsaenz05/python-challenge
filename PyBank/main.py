import os
import csv

absolute_path = os.path.dirname(__file__)
csv_path = os.path.join(absolute_path,'Resources', 'budget_data.csv')

# Read and print csv

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # set variables
    number_of_months = 0
    net_profit_losses = 0
    prev_net = None
    monthly_net_change = []
    
    

    # loop through dataset
    for row in csvreader:
        print(row)
        number_of_months += 1
        net_profit_losses += int(row[1])
        if prev_net is not None:
            monthly_net_change.append(int(row[1])-prev_net)

        prev_net = int(row[1])

        dates.append(row[0])


        

    # print the number of months included in the dataset
    print (number_of_months)

    # print the net total amount of profit/losses over the entire period
    print (net_profit_losses)

    # print the changes in profit/losses over the entire period and the avg of those changes
    print (sum(monthly_net_change)/len(monthly_net_change))

    # print the greatest increase in profits over the entire period
    print (max(monthly_net_change))
    # print the greatest decrease in profits  over the entire period
    print (min(monthly_net_change))
    
    # print results analysis
    results = (f"Financial Analysis\n"
               f"--------------------\n"
               f"Total Months: {number_of_months}\n"
               f"Total: ${net_profit_losses}\n"
               f"Average Change: ${round(sum(monthly_net_change)/len(monthly_net_change))}\n"
               f"Greatest Increase in Profits: Aug-16 (${(max(monthly_net_change))})\n"
               f"Greatest Decrease in Profits: Feb-14 (${(min(monthly_net_change))})")
    print(results)

    # Create text file with results analysis and save to folder
    path = os.path.join(absolute_path,'Analysis', 'Results.txt')
    dataFile = open(path, 'w')
    dataFile.write(results)
    dataFile.close()






