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

    numProcess = 8

    # Get the data from the User for north constellations
    northYear = 2022
    northConstellations = ["Perseus", "Leo", "Orion"]
    northLanguages = ["Chinese", "Czech", "English", ]
    latitudesNorth = ["50N", "30N"]
    

    # Creating the directories and the Paths for North Constellations
    northDirectories= agc.createNorthDir(northYear, northConstellations)
    northPaths = agc.createNorthPaths(northDirectories, northLanguages, latitudesNorth)
 

    # Get the data from the User for south constellations
    southYear = northYear
    southConstellations = ["Orion","Canis Major","Bootes"]
    southLanguages = ["Portuguese", "Spanish"]
    latitudesSouth = ["0","40S"]

    # Creating the directories and the Paths for South Constelllations
    southDirectories= agc.createSouthDir(southYear, southConstellations)
    southPaths = agc.createSouthPaths(southDirectories, southLanguages,latitudesSouth)
    
    if len(northConstellations) == 0:
        print("There are not constellations selected for the north hemisphere.")
        pass
    else:
        # Create a list from the new doc Paths for a leter use in the Images printing
        northListPaths = []
        #Call de translation for north constellations function, requiring multiprocessing with Pool
        pool1 = multiprocessing.Pool(processes = numProcess)
        for path in northPaths:
            northListPaths.append(pool1.apply_async(agc.northTranslation, args = (path, )).get())
        pool1.close()
        pool1.join()
    
    
    # Create a list from the new doc Paths for a leter use in the Images printing
    if len(southConstellations) == 0:
        print("There are not constellations selected for the south hemisphere.")
        pass
    else:
        #Call de translation for north constellations function, requiring multiprocessing with Pool
        southListPaths = []
        pool2 = multiprocessing.Pool(processes = numProcess)
        for path in southPaths:
            southListPaths.append(pool2.apply_async(agc.southTranslation, args = (path, )).get())
        pool2.close()
        pool2.join()
    
    # Activate the Scrapper
    agc.createImageDir()
    linksNorth = agc.imagesLinks(northConstellations,latitudesNorth)
    linksSouth = agc.imagesLinks(southConstellations,latitudesSouth)
    
    if len(northConstellations) == 0:
        print("There are not constellations selected for the north hemisphere.")
        pass
    else: 
        pool3 = multiprocessing.Pool(processes = numProcess)
        for link in linksNorth:
            pool3.apply_async(agc.imageDownload, args = (link, ))
        pool3.close()
        pool3.join()

    
    if len(southConstellations) == 0:
        print("There are not constellations selected for the south hemisphere.")
        pass
    else:
        pool4 = multiprocessing.Pool(processes = numProcess)
        for link in linksSouth:
            pool4.apply_async(agc.imageDownload, args = (link, ))
        pool4.close()
        pool4.join()

    #Print Images in the Word files
    if len(northConstellations) == 0:
        print("There are not constellations selected for the north hemisphere.")
        pass
    else:
        pool5 = multiprocessing.Pool(processes = numProcess)
        northPDFPaths = []
        for path in northListPaths:
            northPDFPaths.append(pool5.apply_async(agc.printImage, args = (path, )).get())
        pool5.close()
        pool5.join()
    
    if len(southConstellations) == 0:
        print("There are not constellations selected for the south hemisphere.")
        pass
    else:
        pool6 = multiprocessing.Pool(processes = numProcess)
        southPDFPaths = []
        for path in southListPaths:
            southPDFPaths.append(pool6.apply_async(agc.printImage, args = (path, )).get())
        pool6.close()
        pool6.join()
    
    
    # Finishing time counter and getting time of execution
    finish = time.time() - start
    print('Execution time: ', time.strftime("%H:%M:%S", time.gmtime(finish)))