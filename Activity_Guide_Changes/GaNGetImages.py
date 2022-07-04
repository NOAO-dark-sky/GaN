from bs4 import BeautifulSoup
import requests
from IPython.display import Image, display
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
    #Verify the connection
    print(gan.status_code)

    # get the soup to pass the content
    soup = BeautifulSoup(gan.text, 'html.parser')
    # Searching the "div with id = finder" where are the images links to get the first Link
    image = soup.find('div' , attrs= {"id" : "finder"}).find('img')
    #Get the link from the image
    imageFirstLink = str(image['src'])

    imagesLinks = []
    # Replace the Constellation names in the North and the latitudes in the imageLink
    for const in constellations:
        for lat in latitudes:
            newLink = imageFirstLink.replace("hercules", const.lower()).replace("10", transformLatitude(lat))
            imagesLinks.append(newLink)
    return imagesLinks       


# Download the images and save them in the images folder
def imageDownload(link):
    #Change the path to the new folder
    os.chdir(r'C:\Users\Marco Moreno\OneDrive\Documentos\Enciso Systems\GaN\GaN\images')

    # Save the images in local for a later use with an easier name
    linkString = str(link.replace('https://www.globeatnight.org/img/2021/', '').replace('/day/600/','-'))
    with open(linkString, 'wb') as f:
        img = requests.get(link)
        f.write(img.content)
        
        return print(linkString + " has been downloaded.\n____________________________________________________________________________________________\n")






