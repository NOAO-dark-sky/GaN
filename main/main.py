# -*- coding:utf-8 -*-
import time
import os
import sys
import multiprocessing

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
sys.path.append(PROJECT_ROOT)
import Activity_Guide_Changes as agc



if __name__ =='__main__':

    # Start time counter
    start = time.time()

    # Get the data from the User for north constellations
    northYear = 2022
    northConstellations = ["Perseus", "Leo", "Bootes", "Cygnus", "Pegasus", "Orion", "Hercules"]
    northLanguages = ["Catalan", "Chinese", "Czech", "English", "Finnish", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Serbian", "Slovak", "Slovenian", "Spanish", "Swedish", "Thai"]

    # Creating the directories and the Paths for North Constellations
    northDirectories= agc.createNorthDir(northYear, northConstellations)
    northPaths = agc.createNorthPaths(northDirectories, northLanguages)
 

    # Get the data from the User for south constellations
    southYear = northYear
    southConstellations = ["Orion","Canis Major", "Crux", "Leo", "Bootes", "Scorpius", "Hercules", "Sagittarius", "Grus", "Pegasus"]
    southLanguages = ["English", "French", "Indonesian", "Portuguese", "Spanish"]

    # Creating the directories and the Paths for South Constelllations
    southDirectories= agc.createSouthDir(southYear, southConstellations)
    southPaths = agc.createSouthPaths(southDirectories, southLanguages)

    latitudesNorth = ["50N", "40N", "30N", "20N", "10N", "0"]
    latitudesSouth = ["0", "10S", "20S", "30S", "40S"]


    if len(northConstellations) == 0:
        print("There are not constellations selected for the north hemisphere.")
        pass
    else:
        # Create a list from the new doc Paths for a leter use in the Images printing
        northListPaths = []
        #Call de translation for north constellations function, requiring multiprocessing with Pool
        pool1 = multiprocessing.Pool(processes = 4)
        for path in northPaths:
            northListPaths.append(pool1.apply_async(agc.northTranslation, args = (path, )).get())
        pool1.close()
        pool1.join()
    
    
    # Create a list from the new doc Paths for a leter use in the Images printing
    southListPaths = []
    if len(southConstellations) == 0:
        print("There are not constellations selected for the south hemisphere.")
        pass
    else:
        #Call de translation for north constellations function, requiring multiprocessing with Pool
        pool2 = multiprocessing.Pool(processes = 4)
        for path in southPaths:
            southListPaths.append(pool2.apply_async(agc.southTranslation, args = (path, )).get())
        pool2.close()
        pool2.join()
    
    agc.createImageDir()
    linksNorth = agc.imagesLinks(northConstellations,latitudesNorth)
    linksSouth = agc.imagesLinks(southConstellations,latitudesSouth)

    if len(northConstellations) == 0:
        print("There are not constellations selected for the north hemisphere.")
        pass
    else: 
        pool3 = multiprocessing.Pool(processes = 4)
        for link in linksNorth:
            pool3.apply_async(agc.imageDownload, args = (link, ))
        pool3.close()
        pool3.join()

    southListPaths = []
    if len(southConstellations) == 0:
        print("There are not constellations selected for the south hemisphere.")
        pass
    else:
        pool4 = multiprocessing.Pool(processes = 4)
        for link in linksSouth:
            pool4.apply_async(agc.imageDownload, args = (link, ))
        pool4.close()
        pool4.join()
    
    # Finishing time counter and getting time of execution
    finish = time.time() - start
    print('Execution time: ', time.strftime("%H:%M:%S", time.gmtime(finish)))