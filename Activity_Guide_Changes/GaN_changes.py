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
dfnorth = pd.read_excel (r'C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx',sheet_name='North')
dfsouth = pd.read_excel (r'C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx',sheet_name='South')

#Get Dates From North and South Constellations
NorthConsUser = str(input("Please enter the name of the North Constellation: "))
NorthDateUser=dfnorth.loc[dfnorth['Constellations'] == NorthConsUser, 'Dates'].iloc[0]
print(NorthDateUser)

SouthConsUser = str(input("Please enter the name of the South Constellation: "))
SouthDateUser=dfsouth.loc[dfsouth['Constellations'] == SouthConsUser, 'Dates'].iloc[0]
print(SouthDateUser)






