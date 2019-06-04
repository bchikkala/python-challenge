import os
import csv

budget_data = os.path.join("..", "RUTSOM201905DATA2", "Homework", "03-Python", "PyBank", "Resources", "budget_data.csv")

total_months = 0
total_profitloss = 0
value = 0
changes = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_profitloss += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])

        changes = int(row[1])-value
        profits.append(changes)
        value = int(row[1])

        total_months += 1

        total_profitloss = total_profitloss + int(row[1])

    greatest_increase = max(profits)
    greatest_index = profits.inde(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    avg_changes = sum(profits)/len(profits)

print("Financial Analysis of Company")
print(f"Total Months: {str(total_months)}")
print(f"Total: ")
print(f"Average Changes: ${str(round(avg_changes,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt', "w")

line1 = "Financial Analysis"
line2 = str(f"Total Months: {str(total_months)}")
line3 = str(f"Total: ${str(total_profitloss)}")
line4 = str(f"Average Change: ${str(round(avg_changes, 2))}")
line5 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line6 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
