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


        for dc in dirCharts:
        
        i = 0
        k = 0
        l = 0              

        for table in workingDoc.tables:
            
            print(table.cell)
            BigPictureCells = (table.cell(1,0), table.cell(1,2), table.cell(4,0), table.cell(4,2))
            small_picture_cells = (table.cell(1,0), table.cell(1,1), table.cell(1,2), table.cell(1,3), table.cell(3,0), table.cell(3,1), table.cell(3,2), table.cell(3,3))
            
            if i < 2:
                for tableCell in BigPictureCells:
                    tableCell.paragraphs[1].clear()
                                        
                    tableCell.paragraphs[1].add_run().add_picture(dc, width = Inches(3.39), height = Inches(2.35))
                    workingDoc.save(filename)
                    k = k + 1
            
            else :
                for tableCell in small_picture_cells:
                    tableCell.paragraphs[0].clear()
                    tableCell.paragraphs[0].add_run().add_picture(dc, width = Inches(1.44), height = Inches(1.01))
                    workingDoc.save(filename)
                    l = l + 1
                
            i = i + 1  



                    else :
            k = 0
            for tableCell in smallPictureCells:
                tableCell.paragraphs[0].clear()
                tableCell.paragraphs[0].add_run().add_picture(dirCharts[k], width = Inches(1.44), height = Inches(1.01))
                k = k + 1
                workingDoc.save(filename)