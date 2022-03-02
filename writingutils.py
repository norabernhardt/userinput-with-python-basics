import csv

def writeToFile(data):
    with open("data.csv", "a") as f:
        studentwriter=csv.writer(f) 
        studentwriter.writerow(data)