
import csv
from datetime import date
from datetime import datetime
from dateutils import currentAge
from printutils import fileContent
import writingutils
from folder import putFolder


name=input("Wie heißt du? ")
birthdate=input("Wie lautet dein Geburtsdatum? YYYY.MM.DD ")
birthday=datetime.strptime(birthdate, "%Y.%m.%d")   
age=currentAge(birthday)
putFolder(name)
    
if age > 17:
    writingutils.writeToFile([name,age])
else:
    print("Du bist zu jung für die Liste")

result=fileContent()
print(result)