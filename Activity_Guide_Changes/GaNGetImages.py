from bs4 import BeautifulSoup
import requests
import os
from shutil import rmtree

# Create a new folder to download the images
def createImageDir():
    savePath = os.getcwd() 
    savePath = os.path.join(savePath + "\GaN\images")
    rmtree(savePath)
    os.mkdir(savePath)
    return savePath


# Get the latitudes according to the images names in the GaN webpage (north ="10", south ="10s")
def transformLatitude(lat):
    if "N" in lat:
        lat = str(lat.rstrip(lat[-1]))
    else:
        lat = str(lat.lower())
    return lat

def imagesLinks(constellations, latitudes):
        # Get the url in GaN website where the images are located
    url = 'https://www.globeatnight.org/magcharts'
    gan = requests.get(url)
    
    # get the soup to pass the content
    soup = BeautifulSoup(gan.text, 'html.parser')
    # Searching the "div with id = finder" where are the images links to get the first Link
    image = soup.find('div' , attrs= {"id" : "finder"}).find('img')
    #Get the link from the image
    imageFirstLink = str(image['src'])

    imagesLinks = []
    magnitudes = ["05", "15", "25", "35", "45", "55", "65", "75"]
    # Replace the Constellation names in the North and the latitudes in the imageLink
    for const in constellations:
        for lat in latitudes:
            for mag in magnitudes:
                newLink = imageFirstLink.replace("hercules", const.lower().replace(" ", "-")).replace("10", transformLatitude(lat).replace("05", mag)).replace("05", mag)
                imagesLinks.append(newLink)
    return imagesLinks       


# Download the images and save them in the images folder
def imageDownload(link):
    #Change the path to the new folder
    newPath = os.getcwd()
    newPath = os.path.join(newPath + "\GaN\images\\")

    # Verify the status code of the link
    if requests.get(link).status_code == 200:
    # Save the images in a local folder for a later use with an easier name
        linkString = str(link.replace('https://www.globeatnight.org/img/2021/', '').replace('/day/600/','-'))
        newLinkString = os.path.join(newPath + linkString)
        with open(newLinkString, 'wb') as f:
            img = requests.get(link)
            f.write(img.content)
            
            return print(linkString + " has been downloaded.\n____________________________________________________________________________________________\n")






