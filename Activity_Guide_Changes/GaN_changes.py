# Install mtranslate, googletrans for translations
# Install docx for managing the Word Files.
# Install Pandas to manage the Excel file and bring the information
# Import Shutil to remove the directory
import mtranslate, googletrans, os, time      
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, Inches
import pandas as pd
from shutil import rmtree

# Get Data from the Excel File using Pandas
# Capitalize  constellations names for a later comparison
dfNorth = pd.read_excel (r'C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx',sheet_name='North')
dfNorth['Constellations'] = dfNorth['Constellations'].str.capitalize()

dfSouth = pd.read_excel (r'C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx',sheet_name='South')
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








