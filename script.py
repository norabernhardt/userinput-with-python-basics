
import csv
import datetime

name=input("Wie heißt du? ")
age=input ("Wie lautet dein Geburtsdatum? ")

with open("data.csv", "a") as f:
    studentwriter=csv.writer(f)
    x = int(age)
    if x <= 18:
        print("Du bist zu jung für die Liste")
    else:
        studentwriter.writerow([name, age])

file=open("data.csv")
fileContent=file.read()
print(fileContent)




