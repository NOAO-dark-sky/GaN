from bs4 import BeautifulSoup
import requests
from IPython.display import Image, display
import os
from shutil import rmtree
import re

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


# Download the images and save them in the images folder
def imageDownload(constNorth, constSouth, latNorth, latSouth):
    #Change the path to the new folder
    os.chdir(createImageDir())

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
    imageLink = str(image['src'])

    # Replace the Constellation names in the North and the latitudes in the imageLink
    for const in constNorth:
        for lat in latNorth:
            newLink = imageLink.replace("hercules", const.lower()).replace("10", transformLatitude(lat))
            # Save the images in local for a later use with an easier name
            linkString = str(newLink.replace('https://www.globeatnight.org/img/2021/', '').replace('/day/600/','-'))
            with open(linkString, 'wb') as f:
                img = requests.get(newLink)
                f.write(img.content)

    # Replace the Constellation names in the South and the latitudes in the imageLink
    for const in constSouth:
        for lat in latSouth:
            newLink = imageLink.replace("hercules", const.lower()).replace("10", transformLatitude(lat))

            linkString = str(newLink.replace('https://www.globeatnight.org/img/2021/', '').replace('/day/600/','-'))
            with open(linkString, 'wb') as f:
                img = requests.get(newLink)
                f.write(img.content)


northConstellations = ["Perseus", "Leo", "Bootes", "Cygnus", "Pegasus", "Orion", "Hercules"]
southConstellations = ["Orion","Canis Major", "Crux", "Leo", "Bootes", "Scorpius", "Hercules", "Sagittarius", "Grus", "Pegasus"]

latitudesNorth = ["50N", "40N", "30N", "20N", "10N", "0"]
latitudesSouth = ["0", "10S", "20S", "30S", "40S"]

imageDownload(northConstellations, southConstellations, latitudesNorth, latitudesSouth)