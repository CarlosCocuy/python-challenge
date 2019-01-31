import os
import csv

def average (numbers):
    sum = 0
    length = len(numbers)
    for number in numbers:
        sum += number

    return round(float(sum/length),2)


budgetCSV=os.path.join('..','Resources',"budget_data.csv")


# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:
    #initialize variables
    count = 0
    total =0
    change =[]
    current =0
    last = 0
    increase =0
    decrease =0
    InDate=''
    DeDate=''

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # print header
    print("Financial Analysis")
    print("---------------------------")
    #skip header row
    next(csvreader)

    #meat and potatoes
    for i in csvreader:
        #easy to calculate the total and count the rows
        total += int(i[1])
        count =count+1

        #saving the current profit
        current = int(i[1])
        #ensuring the first row isn't an error
        if last !=0:
            #making a list of change to calculate average later
            change.append(current-last)
            #tracking greatest increase and decrease
            if current-last >increase:
                increase = current - last
                InDate = i[0]
            if current - last <decrease:
                decrease = current - last
                DeDate = i[0]
        #saving the current profit to be used as the last profit next i
        last = int(i[1])
    #printing the results
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average  Change: ${average(change)}')
    print(f'Greatest Increase in Profits: {InDate} (${increase})')
    print(f'Greatest Decrease in Profits: {DeDate} (${decrease})')
