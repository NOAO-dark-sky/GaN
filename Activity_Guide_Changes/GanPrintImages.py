from docx import Document
from docx.shared import Inches
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
    constellation = fileName.split('_')[-4].lower().replace(" ", "-")
    latitude = fileName.split('_')[-2]

    path = os.getcwd() 
    path = os.path.join(path + "\GaN\images")

    lat = transformLatitude(latitude)

    magnitudes = ["05", "15", "25", "35", "45", "55", "65", "75"]

    pathsList = []
    for mag in magnitudes:
        pathsList.append(path + "\\" + constellation + "-" + lat + "_" + mag + ".png")
    
    return pathsList

# get the links from the charts for each latitude
def openLocalImage(fileName):
    constellation = fileName.split('_')[-4].lower().replace(" ", "-")
    latitude = fileName.split('_')[-2]

    path = os.getcwd() 
    path = os.path.join(path + "\GaN\images_local")

    lat = transformLatitude(latitude)

    magnitudes = ["05", "15", "25", "35", "45", "55", "65", "75"]

    pathsList = []
    for mag in magnitudes:
        pathsList.append(path + "\\" + constellation + "-" + lat + "_" + mag + ".png")
    
    return pathsList


#crops an image based on the magnitude, saves image as png
def printImage(fileName):
    
    constellation = fileName.split('_')[-4]
    latitude = fileName.split('_')[-2]

    workingDoc = openWordDoc(fileName)
    if "Crux_lat_0_" in fileName:
        dirCharts = openLocalImage(fileName.replace("0_", "10S_"))
    elif "Bootes_lat_40S_" in fileName:
        dirCharts = openLocalImage(fileName.replace("40S_", "30S_"))
    elif "Hercules_lat_40S_" in fileName:
        dirCharts = openLocalImage(fileName.replace("40S_", "30S_"))
    else:
        dirCharts = openImage(fileName)

    table1 = workingDoc.tables[0]
    table1 = (table1.cell(1,0), table1.cell(1,2), table1.cell(4,0), table1.cell(4,2))
    i= 0
    for tableCell in table1:
        tableCell.paragraphs[1].clear()
        tableCell.paragraphs[1].add_run().add_picture(dirCharts[i], width = Inches(3.39), height = Inches(2.35))
        i = i + 1
    workingDoc.save(fileName)

    table2 = workingDoc.tables[1]
    table2 = (table2.cell(1,0), table2.cell(1,2), table2.cell(4,0), table2.cell(4,2))
    for tableCell in table2:
        tableCell.paragraphs[1].clear()
        tableCell.paragraphs[1].add_run().add_picture(dirCharts[i], width = Inches(3.39), height = Inches(2.35))
        i = i + 1
    workingDoc.save(fileName)

    table3 = workingDoc.tables[2]
    table3 = (table3.cell(1,0), table3.cell(1,1), table3.cell(1,2), table3.cell(1,3), table3.cell(3,0), table3.cell(3,1), table3.cell(3,2), table3.cell(3,3))
    j = 0
    for tableCell in table3:
        tableCell.paragraphs[0].clear()
        tableCell.paragraphs[0].add_run().add_picture(dirCharts[j], width = Inches(1.44), height = Inches(1.01))
        j = j + 1
    workingDoc.save(fileName)

    print("The charts in the activity guide for the constellation {cons}".format(cons = constellation) + " in the latitude {lat}".format(lat = latitude) +" have been printed \n________________________________________________________________________________________________\n")    

    return fileName




