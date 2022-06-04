# Install mtranslate, googletrans for translations
# Install python-docx for managing the Word Files.
# Install Pandas to manage the Excel file and bring the information
# Import Shutil to remove the directory
import mtranslate, googletrans, os, time, sys    
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, Inches
import pandas as pd
from shutil import rmtree

# Define the path for the excel file
excelPath = os.path.join(sys.path[0],"GaN_cons_and_dates.xlsx")

# Get Data from the Excel File using Pandas
# Capitalize  constellations names for a later comparison
dfNorth = pd.read_excel (excelPath,sheet_name='North')
dfNorth['Constellations'] = dfNorth['Constellations'].str.capitalize()

dfSouth = pd.read_excel (excelPath,sheet_name='South')
dfSouth['Constellations'] = dfSouth['Constellations'].str.capitalize()

# Validate the constellation names getting from the user according to the Excel file.
# Get Dates From North and South Constellations
northConsUser = str(input("Please enter the name of the North Constellation: "))
northConsUser = northConsUser.capitalize()
validateNorth = northConsUser in dfNorth['Constellations'].values
while validateNorth == False:
    northConsUser = str(input("Please enter the a valid name for the North Constellation: "))
    northConsUser = northConsUser.capitalize()
    validateNorth = northConsUser in dfNorth['Constellations'].values
else:
    northDateUser=dfNorth.loc[dfNorth['Constellations'] == northConsUser, 'Dates'].iloc[0]
    print(northDateUser)

southConsUser = str(input("Please enter the name of the South Constellation: "))
southConsUser = southConsUser.capitalize()
validateSouth = southConsUser in dfSouth['Constellations'].values
while validateNorth == False:
    southConsUser = str(input("Please enter a valid name for the South Constellation: "))
    southConsUser = southConsUser.capitalize()
    validateSouth = southConsUser in dfSouth['Constellations'].values
else:
    southDateUser=dfSouth.loc[dfSouth['Constellations'] == southConsUser, 'Dates'].iloc[0]
    print(southDateUser)

#########################################################################################
#########################################################################################
############################  ###########################################################

#store constellation and date information in respective variables
northCons = dfNorth['Constellations']
southCons = dfSouth['Constellations']

northDates = dfNorth['Dates']
southDates = dfSouth['Dates']

#updates the constellation: creates a variable to hold the new constellation, uses the old constellation
#information to find the new constellation
print(northCons, northDates, southCons, southDates)
newConstellationNorth = {}
newConstellationSouth = {}
for i in range(len(northCons)):

    newConstellationNorth[northCons[i]] = northDates[i] 

for i in range(len(southCons)):

    newConstellationSouth[southCons[i]] = southDates[i] 

print(newConstellationNorth)
print(newConstellationSouth)
year = 2022
Thai_year = year + 543

#updating southern hemisphere information (constellation, date, text displayed to the user)
#######################################################################################
########################All the information that needs to change#######################
#######################################################################################

#opens document that will be edited
def openWordDoc(filename):
    document = Document(filename)
    return document


#######################################################################################
########################All the information that needs to change#######################
#######################################################################################

lang = googletrans.LANGUAGES
#updating northern hemisphere information (constellation, date, text displayed to user)
North_constellation_replacement = {
        "English" : "Perseus"
        }
    
North_date_replacement = {
        "English" : "Oct. 30-Nov. 8 and Nov. 29-Dec. 8"
        }

North_heading_first = {
    "English" : ""
    }

North_heading_middle = {
    "English" : " Campaign Dates that use "
    }

North_heading_last = {
    "English" : ": "
    }


First_Paragraph_first = {
    "English" : "You are participating in a global campaign to observe and record the faintest stars visible as a means of measuring light pollution in a given location. By locating and observing the constellation "
    }

First_Paragraph_last = {
    "English" : " in the night sky and comparing it to stellar charts, people from around the world will learn how the lights in their community contribute to light pollution. Your contributions to the online database will document the visible nighttime sky."
}

##################################################################################################
##################################################################################################
        ###	End of the changes section defining things that need to be changed			###
##################################################################################################
##################################################################################################
#1date2con3
CountryList1 = ("Czech")
#1con2year3date
CountryList2 = ("Chinese", "Finnish", "Serbian", "Swedish")
#1year2Con3date
CountryList3 = ("Chilean_Spanish", "Catalan", "English", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Thai")  #1year2Con3date

language_translate = {}
#goes through North_constellation_replacement and stores which language to translate to into language_translate
for key, value in North_constellation_replacement.items():
    for code, langs in lang.items():
        if key == "Chinese":
            language_translate[key] = "zh-cn"
        if key == langs.capitalize():
            language_translate[key] = code


#replace the translations in the proper places
for language, constellation in North_constellation_replacement.items():
    # Define the Word file path
    wordPath = os.path.abspath("..\Gan\GaN\docs_to_change\GaN2018_ActivityGuide_Perseus_N_")
    working_doc = openWordDoc(wordPath + str(language) + ".docx") 
    print("_____________________________________________________________\n")
    print("Working on {language} language\n".format(language = key))

    
