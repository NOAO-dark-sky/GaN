from bs4 import BeautifulSoup
import requests
from IPython.display import Image, display


# Get the url in GaN website where the images are located
url = 'https://www.globeatnight.org/magcharts'
gan = requests.get(url)
#Verify the connection
print(gan.status_code)

# get the soup to pass the content
soup = BeautifulSoup(gan.text, 'html.parser')
# Searching the "div with id = finder" where are the images links
magfloat = soup.find('div' , attrs= {"id" : "finder"}).find_all('div')

images = soup.find_all('img')



for image in images:
    link = image['src']
    if 'hercules' in link:
        linkString = str(link.replace('https://www.globeatnight.org/img/2021/', '').replace('/day/600/','-'))
        with open(linkString, 'wb') as f:
            img = requests.get(link)
            f.write(img.content)