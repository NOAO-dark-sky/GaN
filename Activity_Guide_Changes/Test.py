import os
from os import getcwd
from docx import Document

def openWordDoc(filename):
    document = Document(filename)
    return document

#new = getcwd() 
#new = os.path.join(new + '\GaN\docs_changed\Hello')
#os.mkdir(new)
#print(new)

#new =getcwd()
#print(new)

year = 2022
northConsUser= {"Orion": 1, "Taurus": 2, "Hercules": 3}
language = {"English": "a", "Spanish": "b", "German": "c"}

wordPath = os.path.abspath("..\Gan\GaN\docs_to_change\GaN2018_ActivityGuide_Perseus_N_")
workingDoc = openWordDoc(wordPath + "English" + ".docx")

northConsUser= {"Orion": "01/12/2020", "Taurus": "16/05/2022", "Hercules": "10/07/2022"}
language = {"English": "Perseus", "Spanish": "Perseo", "French" : "Persée"}

for constellation, date in northConsUser.items():
    savePath = os.getcwd() 
    savePath = os.path.join(savePath + "\GaN\docs_changed\GaN{year}_ActivityGuide_{cons}".format(year = year, cons = constellation))        
    os.mkdir(savePath)
    for lang, letter in language.items():
        #newWordPath = os.path.abspath("..\Gan\GaN\docs_changed\GaN_{year}_ActivityGuide_{cons}_/".format(year = year, cons = northConsUser))
        newWordPath = os.path.join(savePath + "\GaN_{year}_ActivityGuide_{cons}_".format(year = year, cons = constellation) + str(lang) + ".docx")
        workingDoc.save(newWordPath)
