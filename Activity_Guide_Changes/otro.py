    northYear = 2022
    northConstellations = ["Perseus", "Leo", "Bootes", "Cygnus", "Pegasus", "Orion", "Hercules"]
    northLanguages = ["Catalan", "Chinese", "Czech", "English", "Finnish", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Serbian", "Slovak", "Slovenian", "Spanish", "Swedish", "Thai"]
    latitudesNorth = ["50N", "40N", "30N", "20N", "10N", "0"]
    # Creating the directories and the Paths for North Constellations
    northDirectories= agc.createNorthDir(northYear, northConstellations)
    northPaths = agc.createNorthPaths(northDirectories, northLanguages)
 

    # Get the data from the User for south constellations
    southYear = northYear
    southConstellations = ["Orion","Canis Major", "Crux", "Leo", "Bootes", "Scorpius", "Hercules", "Sagittarius", "Grus", "Pegasus"]
    southLanguages = ["English", "French", "Indonesian", "Portuguese", "Spanish"]
    latitudesSouth = ["0", "10S", "20S", "30S", "40S"]