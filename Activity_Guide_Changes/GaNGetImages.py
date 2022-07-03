from bs4 import BeautifulSoup
import requests
from IPython.display import Image, display
import os
from shutil import rmtree

#Create a new folder to download the images
def createImageDir():
    savePath = os.getcwd() 
    savePath = os.path.join(savePath + "\GaN\images")
    rmtree(savePath)
    os.mkdir(savePath)


createImageDir()