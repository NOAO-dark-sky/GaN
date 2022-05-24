# encoding: utf-8

imports = ['mtranslate', 'googletrans', 'os', 'time', 'PIL', 'docx']
import subprocess, sys
import importlib
#The right name of the file is docxToPdf
import docxToPdf as dtp

wdFormatPDF = 17

#imports each module, tells user if import is successful or not, prevents program
#from crashing if a module cannot be imported
for module in imports:
    try:
        print("Importing necessary modules...")
        importlib.import_module(module)
        print("Import of " + module + " successful.")

    except ImportError:
        print(module + " module not found. Beginning install of " + module + ".")
        if module != "docx":
            subprocess.call([sys.executable, "-m", "pip", "install", module])
        else:
            subprocess.call([sys.executable, "-m", "pip", "install", "python-docx"])
        importlib.import_module(module)
        print("Import and install of " + module + " successful.")

# Is needed to Install mtranslate and googletrans
import mtranslate, googletrans, os, time       
from shutil import rmtree
from PIL import Image
#Install python-docx library
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, Inches
import pandas

#opens document that will be edited
def open_word_doc(filename):
    document = Document(filename)
    
    return document

#crops an image based on the magnitude, saves image as png
def cut_star_chart(filename):
    
    cut_points = {
            "Mag0" : (80,80,826,596),
            "Mag1" : (834,80,1577,596),
            "Mag2" : (80,604,826,1119),
            "Mag3" : (834,604,1577,1119),
            "Mag4" : (80,1127,826,1642),
            "Mag5" : (834,1127,1577,1642),
            "Mag6" : (80,1651,826,2166),
            "Mag7" : (834,1651,1577,2166)
            }
    
    
    for key, value in cut_points.items():
        im = Image.open(filename)
        im.crop(value).save(key + ".png")

        
        
    return

lang = googletrans.LANGUAGES

#read in the excel sheets for both the north and south constellations
north_cons_df = pandas.read_excel(r"C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx",sheet_name = 'North', index_col = None)

south_cons_df = pandas.read_excel(r"C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\Activity_Guide_Changes\GaN_cons_and_dates.xlsx",sheet_name = 'South', index_col = None)
print(north_cons_df)

#store constellation and date information in respective variables
north_cons = north_cons_df['Constellations']
south_cons = south_cons_df['Constellations']

north_dates = north_cons_df['Dates']
south_dates = south_cons_df['Dates']

#updates the constellation: creates a variable to hold the new constellation, uses the old constellation
#information to find the new constellation
print(north_cons, north_dates, south_cons, south_dates)
new_constellation_north = {}
new_constellation_south = {}
for i in range(len(north_cons)):

    new_constellation_north[north_cons[i]] = north_dates[i] 

for i in range(len(south_cons)):

    new_constellation_south[south_cons[i]] = south_dates[i] 

print(new_constellation_north)
print(new_constellation_south)
year = 2020
Thai_year = year + 543





