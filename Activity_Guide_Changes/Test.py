import googletrans
import pandas as pd
import os, sys

translator= googletrans.Translator()

excelPath = os.path.join(sys.path[0],"GaN_cons_and_dates.xlsx")
dfNorth = pd.read_excel (excelPath,sheet_name='North')
dfNorth['Constellations'] = dfNorth['Constellations'].str.capitalize()

#store constellation and date information in respective variables
northCons = dfNorth['Constellations']

northDates = dfNorth['Dates']

#updates the constellation: creates a variable to hold the new constellation, uses the old constellation
#information to find the new constellation
newConstellationNorth = {}

for i in range(len(northCons)):
    newConstellationNorth[northCons[i]] = northDates[i] 

#print(newConstellationNorth)
year = 2022
Thai_year = year + 543


North_constellation_replacement = {
        
        "Catalan" : "Perseus",
        "Chinese" : "英仙座",
        "Czech" : "Persea",
        "English" : "Perseus",
        "Finnish" : "Perseus" ,
        "French" : "Persée" ,    
        "Galician" : "Perseo",
        "German" : "Perseus",
        "Greek" : "Περσεύς",
        "Indonesian" : "Perseus",
        "Japanese" : "ペルセウス",
        "Polish" : "Perseusz",
        "Portuguese" : "Perseu",
        "Romanian" : "Perseu",
        "Serbian" : "Персеус",
        "Slovak" : "Perseus",
        "Slovenian" : "Perseus",
        "Spanish" : "Perseo",
        "Swedish" : "Perseus",
        "Thai" : "เซอุส"
            
        }

lang = googletrans.LANGUAGES

#langCodes ={}

for languageBase, constName in North_constellation_replacement.items():
    for codeLanguage, languageName in lang.items():
        if languageBase.lower() == languageName:
                textTranslate = translator.translate(newConstellationNorth.get("Taurus"), dest = codeLanguage)
                print(textTranslate.text)
            

            #langCodes[codeLanguage] = languageBase.lower()
            #dateTranslation = translator.translate(newConstellationNorth.get(constName),dest = codeLanguage)

#print (langCodes)


'''
#1date2con3
CountryList1 = ("Czech")
#1con2year3date
CountryList2 = ("Chinese", "Finnish", "Serbian", "Swedish")
#1year2Con3date
CountryList3 = ("Chilean_Spanish", "Catalan", "English", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Thai")  #1year2Con3date

language_translate = {}
#goes through North_constellation_replacement and stores which language to translate to into language_translate
for language, constName in North_constellation_replacement.items():
    for code, langs in lang.items():
        if language == "Chinese":
            language_translate[language] = "zh-cn"
            new_dates_trans = translator.translate(constName, language_translate[language],"en")
            new_cons_trans = translator.translate(language, language_translate[language],"en")
            print(new_dates_trans.text, new_cons_trans.text)
        elif language == langs.capitalize():
            language_translate[language] = code
            new_dates_trans = translator.translate(constName, language_translate[language],"en")
            new_cons_trans = translator.translate(language, language_translate[language],"en")
            print(new_dates_trans.text, new_cons_trans.text)
            '''
        







