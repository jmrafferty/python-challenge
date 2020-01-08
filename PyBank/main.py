# First we'll import the os module
import os

# Module for reading CSV files
import csv

#Store csvpath as variable.
csvpath = os.path.join("Resources", "budget_data.csv")

# Read w/ CSV Module
with open (csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    total_months = 0
    total_pnl = 0
    total_change = 0
    Increase = 0
    Decrease = 0
    
    #variable for next row -- This skips line 1
    #nxt_row = next(csvreader)
    
    File = []
    changes = [0]
    profit = 0
    loss = 0    
    
    # Read each row of data after the header
    for row in csvreader:
        
        #File.append([row[0], row[1]])
        
        File.append(row)
         
        #add 1 to month total for each line      
        total_months = total_months + 1
        
        #Sum = sum + index 1 of row as integer
        total_pnl = total_pnl + int(row[1])


#Loop through rows
#File[[row][column]]
#0..85
for row in range(len(File)):
    
    #Set current to the value of index 1 or 'row'
    current = int(File[row][1])
    
    #initiate 'previous' as 0 -- for first line
    previous = 0
    
    #if current is > 0 add 'current' to 'profit'
    
    if current > 0:
        profit = profit + current
    else:
        loss = loss + current
    
    
    if row != 0:
        previous = int(File[row - 1][1])
        
        changes.append(current - previous)
    
    #Print 'File' list and test month over month changes
    #print(str(row) + str(File[row]) + str(changes[row]))
    

print("Total Months = " + str(len(changes)))
print("Net P&L = " + str(total_pnl))
print("Total Change = " + str(sum(changes)))
print("Average Change = " + str(sum(changes)/(len(changes) - 1)))
print("Greatest Profit Increase = " + str(max(changes)))
print("Month of Greatest Increase = " + str(File[changes.index(max(changes))][0]))
print("Greatest Decrease in Profits = " + str(min(changes)))
print("Month of Greatest Decrease = " + str(File[changes.index(min(changes))][0]))

results_dict = {"Total Months": str(len(changes)), 
                "Net P&L" : str(total_pnl),
                "Average Change" : str(sum(changes)/(len(changes) - 1)),
                "Greatest Profit Increase": str(max(changes)),
                "Month of Greatest Increase" : str(File[changes.index(max(changes))][0]),
                "Greatest Decrease in Profits" : str(min(changes)),
                "Month of Greatest Decrease" : str(File[changes.index(min(changes))][0])}

# Specify the file to write to
output_path = os.path.join("output", "pybank_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (header)
    csvwriter.writerow(csv_header)
                       
    csvwriter.writerow(results_dict)
    
    # Write the data lines
    #csvwriter.writerow("Total Months", "str(len(changes))")
    #csvwriter.writerow("Net P&L", str(total_pnl))
    #csvwriter.writerow("Average Change", str(sum(changes)/(len(changes) - 1)))
    #csvwriter.writerow("Greatest Profit Increase", str(max(changes)))
    #csvwriter.writerow("Month of Greatest Increase", str(File[changes.index(max(changes))][0]))
    #csvwriter.writerow("Greatest Profit Decrease", str(min(changes)))
    #csvwriter.writerow("Month of Greatest Decrease", str(File[changes.index(min(changes))][0]))

    #print(File[0][0])
    # create variable to hold the value of index 1 in the next line (row +1)
    
    #if row == len(File) - 1:
        
        #change = 0
        
    #else:
        
        #new = int(File[row + 1][1])    
        #print(new)
        #print(next(row))
        #change = new - initial
    
    #changes.append(change)
    
    #Gives 0? -- 
    #total_change = total_change + change
    
    #av_change = total_change / total_months
    


#print("Total # of months = " + str(total_months))
#print("Total change = " + str(total_change))
#print("Average change = " + str(av_change))



#print("Total of Profits (only) = " + str(profit))
#print("Total of Losses (only) = " + str(loss))

#to test month over month change


#for change in changes:
    #print(change)
    


    
    
    