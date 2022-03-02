
import csv
from datetime import date
from datetime import datetime


def currentAge(birthday):
    today=date.today()
    yearDiff = today.year - birthday.year
    noBirthdayThisYear = (today.month, today.day) < (birthday.month, birthday.day)

    if noBirthdayThisYear:
        return yearDiff -1
    return yearDiff

name=input("Wie heißt du? ")
age=input("Wie lautet dein Geburtsdatum? YYYY.MM.DD ")


with open("data.csv", "a") as f:
    studentwriter=csv.writer(f) 
    birthday=datetime.strptime(age, "%Y.%m.%d")   
    
    if currentAge(birthday) > 18:
        studentwriter.writerow([name, age])
    else:
        print("Du bist zu jung für die Liste")

file=open("data.csv")
fileContent=file.read()
print(fileContent)
