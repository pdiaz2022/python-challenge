import os
import csv

# path = "C:/Users/pedia/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"
csvpath = os.path.join ('Resources', 'budget_data.csv')
output_file = os.path.join('Analysis','budget_data.txt')

# Define variables: 
# The total number of months included in the dataset, 
# The net total amount of "Profit/Losses" over the entire period, 

totalmonth = 0
net_profit_losses = 0 
change_profit_losses = 0 
average_profit_losses = 0 

# Open & read csv file 
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        totalmonth = totalmonth + 1
        net_profit_losses = net_profit_losses + int(row[1])

    #Print the results 
    print ("Total number of months:" + str(totalmonth))
    print ("The net total amount:" + str(net_profit_losses))
  
    # exporting file 
    export = open(output_file, 'w')
    export.write("Total number of months:" + str(totalmonth) + "\n")
    export.write("The net total amount:" + str(net_profit_losses) + "\n")