
import os
import csv

pollCSV=os.path.join('..','Resources',"election_data.csv")

# Read in the CSV file
with open(pollCSV, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #setting variables
    error=0
    khan=0
    Correy=0
    Li =0
    OT = 0
    count =0
    winner='none'
    # print header
    print("Election Results")
    print("-------------------------")
    #skip header row
    next(csvreader)
    for i in csvreader:
        #easy to count the rows
        count =count+1
        if(i[2] == "Khan"):
            khan=khan+1
        elif(i[2]=="Correy"):
            Correy=Correy+1
        elif(i[2]=="Li"):
            Li=Li+1
        elif(i[2]=="O'Tooley"):
            OT=OT+1
        else:
            error=1
    #calculate percent
    kp=round(khan/count*100,3)
    cp=round(Correy/count*100,3)
    lp=round(Li/count*100,3)
    op=round(OT/count*100,3)
    if khan > max(Correy,Li,OT):
        winner = "Khan"
    elif Correy > max(khan,Li,OT):
        winner = "Correy"
    elif Li > max(khan,Correy,OT):
        winner = "Li"
    elif OT > max(khan,Correy,Li):
        winner = "O'Tooley"
    if( error ==1):
        print("look at ifs")
    print(f'Total Votes: {count}')
    print("-------------------------")
    print(f'Khan: {kp}% ({khan})')
    print(f'Correy: {cp}% ({Correy})')
    print(f'Li: {lp}% ({Li})')
    print("O'Tooley "+f': {op}% ({OT})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
