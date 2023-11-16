
import os
import csv



# Using double backslashes
PyBankcsv = os.path.join("C:\\Users\\14374\\Desktop\\Study\\python module3\\PyBank\\Resources\\budget_data.csv")
import csv



# Initialize lists to store data from the CSV file
months = []  # List to store the dates
profits_losses = []  # List to store profit/loss values
changes = []  # List to store changes in profit/loss

# Open the CSV file and read its content
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Append data to respective lists
        months.append(date)
        profits_losses.append(profit_loss)

# Calculate the total number of months
total_months = len(months)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over the entire period
for i in range(1, total_months):
    changes.append(profits_losses[i] - profits_losses[i - 1])

# Calculate the average of changes
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase) + 1
greatest_increase_date = months[greatest_increase_index]

greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease) + 1
greatest_decrease_date = months[greatest_decrease_index]

# Print the results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(net_total) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(greatest_increase) + " ($" + str(greatest_increase_date) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(greatest_decrease) + " ($" + str(greatest_decrease_date) + ")\n")
    text.write("----------------------------------------------------------\n")