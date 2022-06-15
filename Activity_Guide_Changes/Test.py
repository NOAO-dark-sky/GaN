import googletrans

North_constellation_replacement = {
        
        "Catalan" : "Perseus",
        "Chinese" : "英仙座",
        "Czech" : "Persea",
        "English" : "Perseus",
        "Finnish" : "Perseus" ,
        "French" : "Persée" ,    
        "Galician" : "Perseo",
        "German" : "Perseus",
        "Greek" : "Περσεύς",
        "Indonesian" : "Perseus",
        "Japanese" : "ペルセウス",
        "Polish" : "Perseusz",
        "Portuguese" : "Perseu",
        "Romanian" : "Perseu",
        "Serbian" : "Персеус",
        "Slovak" : "Perseus",
        "Slovenian" : "Perseus",
        "Spanish" : "Perseo",
        "Swedish" : "Perseus",
        "Thai" : "เซอุส"
            
        }

lang = googletrans.LANGUAGES

#1date2con3
CountryList1 = ("Czech")
#1con2year3date
CountryList2 = ("Chinese", "Finnish", "Serbian", "Swedish")
#1year2Con3date
CountryList3 = ("Chilean_Spanish", "Catalan", "English", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Thai")  #1year2Con3date

language_translate = {}
#goes through North_constellation_replacement and stores which language to translate to into language_translate
for language, constName in North_constellation_replacement.items():
    for code, langs in lang.items():
        if language == "Chinese":
            language_translate[language] = "zh-cn"
        if language == langs.capitalize():
            language_translate[language] = code
        







