import csv
from datetime import datetime

def studentName():
    print("Please verify your name!")
    name = input("Enter your name: ")
    print("Welcome, " + (name) + "!")
def studentDOB():
    print("Please verify your BOD!")    
    date = int(input("Enter date: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    print("Your DOB is " + str(date), + (month), + (year))
    print('')