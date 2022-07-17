from docx import Document
from PIL import Image
from docx.shared import Pt, Inches
import os

# Open the MS Word files created in the translations
def openWordDoc(filename):
    document = Document(filename)
    return document

# Get the latitudes according to the images names in the GaN webpage (north ="10", south ="10s")
def transformLatitude(lat):
    if "N" in lat:
        lat = str(lat.rstrip(lat[-1]))
    else:
        lat = str(lat.lower())
    return lat

# get the links from the charts for each latitude
def openImage(fileName):
    constellation = fileName.split('_')[-4]
    latitude = fileName.split('_')[-2]

    path = os.getcwd() 
    path = os.path.join(path + "\GaN\images")

    lat = transformLatitude(latitude)

    magnitudes = ["05", "15", "25", "35", "45", "55", "65", "75"]

    pathsList = []
    for mag in magnitudes:
        pathsList.append(path + "\\" + constellation + "-" + lat + "_" + mag + ".png")
    
    return pathsList




#crops an image based on the magnitude, saves image as png
def cutStarChart(filename):

    workingDoc = openWordDoc(filename)
    dirCharts = openImage(filename)

    table1 = workingDoc.tables[0]
    table1 = (table1.cell(1,0), table1.cell(1,2), table1.cell(4,0), table1.cell(4,2))
    i= 0
    for tableCell in table1:
        tableCell.paragraphs[1].clear()
        tableCell.paragraphs[1].add_run().add_picture(dirCharts[i], width = Inches(3.39), height = Inches(2.35))
        i = i + 1
    workingDoc.save(filename)

    table2 = workingDoc.tables[1]
    table2 = (table2.cell(1,0), table2.cell(1,2), table2.cell(4,0), table2.cell(4,2))
    for tableCell in table2:
        tableCell.paragraphs[1].clear()
        tableCell.paragraphs[1].add_run().add_picture(dirCharts[i], width = Inches(3.39), height = Inches(2.35))
        i = i + 1
    workingDoc.save(filename)

    table3 = workingDoc.tables[2]
    table3 = (table3.cell(1,0), table3.cell(1,1), table3.cell(1,2), table3.cell(1,3), table3.cell(3,0), table3.cell(3,1), table3.cell(3,2), table3.cell(3,3))
    j = 0
    for tableCell in table3:
        tableCell.paragraphs[0].clear()
        tableCell.paragraphs[0].add_run().add_picture(dirCharts[j], width = Inches(1.44), height = Inches(1.01))
        j = j + 1
    workingDoc.save(filename)     

def bigTable():
    pass

def littleTable():
    pass

northListPaths = ['C:\\Users\\Marco Moreno\\OneDrive\\Documentos\\Enciso Systems\\GaN\\GaN\\docs_changed\\GaN_North_2022_ActivityGuide_Leo\\GaN_2022_ActivityGuide_Leo_lat_0_Spanish.docx', 'C:\\Users\\Marco Moreno\\OneDrive\\Documentos\\Enciso Systems\\GaN\\GaN\\docs_changed\\GaN_North_2022_ActivityGuide_Leo\\GaN_2022_ActivityGuide_Leo_lat_40N_Spanish.docx']

southListPaths = ['C:\\Users\\Marco Moreno\\OneDrive\\Documentos\\Enciso Systems\\GaN\\GaN\\docs_changed\\GaN_South_2022_ActivityGuide_Orion\\GaN_2022_ActivityGuide_Orion_lat_10S_French.docx', 'C:\\Users\\Marco Moreno\\OneDrive\\Documentos\\Enciso Systems\\GaN\\GaN\\docs_changed\\GaN_South_2022_ActivityGuide_Orion\\GaN_2022_ActivityGuide_Orion_lat_20S_French.docx']


for path in northListPaths:
    cutStarChart(path)


