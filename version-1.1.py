
import csv
from datetime import date
from datetime import datetime
from dateutils import currentAge
from printutils import fileContent



name=input("Wie heißt du? ")
age=input("Wie lautet dein Geburtsdatum? YYYY.MM.DD ")
birthday=datetime.strptime(age, "%Y.%m.%d")   

age=currentAge(birthday)


with open("data.csv", "a") as f:
    studentwriter=csv.writer(f) 
    
    if currentAge(birthday) > 18:
        studentwriter.writerow([name, age])
    else:
        print("Du bist zu jung für die Liste")

result=fileContent()
print(result)