# -*- coding: utf-8 -*-
"""
@author: Elliot Kisiel

Last update: 22 March 2019

A script to change the neccessary information on a GaN activity guide for the 
different languages in the northern and southern hemisphere. 

For this program to run, the following files are necessary:
    
Items that still need to be added
-Be able to download and convert the pdfs to pngs from janiks website directly
"""
# encoding: utf-8

imports = ['mtranslate', 'googletrans', 'os', 'time', 'PIL', 'docx']
import subprocess, sys
import importlib
import docxtopdf as dtp

wdFormatPDF = 17

#imports each module, tells user if import is successful or not, prevents program
#from crashing if a module cannot be imported
for module in imports:
    try:
        print("Importing necessary modules...")
        importlib.import_module(module)
        print("Import of " + module + " successful.")

    except ImportError:
        print(module + " module not found. Beginning install of " + module + ".")
        if module != "docx":
            subprocess.call([sys.executable, "-m", "pip", "install", module])
        else:
            subprocess.call([sys.executable, "-m", "pip", "install", "python-docx"])
        importlib.import_module(module)
        print("Import and install of " + module + " successful.")

import mtranslate, googletrans, os, time       
from shutil import rmtree
from PIL import Image
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, Inches
import pandas

#opens document that will be edited
def open_word_doc(filename):
    document = Document(filename)
    
    return document

#crops an image based on the magnitude, saves image as png
def cut_star_chart(filename):
    
    cut_points = {
            "Mag0" : (80,80,826,596),
            "Mag1" : (834,80,1577,596),
            "Mag2" : (80,604,826,1119),
            "Mag3" : (834,604,1577,1119),
            "Mag4" : (80,1127,826,1642),
            "Mag5" : (834,1127,1577,1642),
            "Mag6" : (80,1651,826,2166),
            "Mag7" : (834,1651,1577,2166)
            }
    
    
    for key, value in cut_points.items():
        im = Image.open(filename)
        im.crop(value).save(key + ".png")

        
        
    return

lang = googletrans.LANGUAGES

#read in the excel sheets for both the north and south constellations
north_cons_df = pandas.read_excel('GaN_cons_and_dates.xlsx',sheet_name = 'North', index_col = None)

south_cons_df = pandas.read_excel('GaN_cons_and_dates.xlsx',sheet_name = 'South', index_col = None)
print(north_cons_df)

#store constellation and date information in respective variables
north_cons = north_cons_df['Constellations']
south_cons = south_cons_df['Constellations']

north_dates = north_cons_df['Dates']
south_dates = south_cons_df['Dates']

#updates the constellation: creates a variable to hold the new constellation, uses the old constellation
#information to find the new constellation
print(north_cons, north_dates, south_cons, south_dates)
new_constellation_north = {}
new_constellation_south = {}
for i in range(len(north_cons)):

    new_constellation_north[north_cons[i]] = north_dates[i] 

for i in range(len(south_cons)):

    new_constellation_south[south_cons[i]] = south_dates[i] 

print(new_constellation_north)
print(new_constellation_south)
year = 2020
Thai_year = year + 543


#updating southern hemisphere information (constellation, date, text displayed to user)
#######################################################################################
########################All the information that needs to change#######################
#######################################################################################
South_constellation_replacement = {
        "Chilean_Spanish" : "Scorpius",
        "English" : "Scorpius",
        "French" : "Scorpius",
        "Indonesian" : "Scorpius",
        "Portuguese" : "Scorpius",
        "Spanish" : "Scorpius"
        }

South_date_replacement = {
        "Chilean_Spanish" : "Del 4 al 13 de julio y del 2 al 11 de agosto",
        "English" : "July 4-13 and August 2-11",
        "French" : "Du 4 au 13 juillet et du 2 au 11 août",
        "Indonesian" : "4-13 Juli dan 2-11 Agustus",
        "Portuguese" : "4 a 13 de julho e 2 a 11 de agosto",
        "Spanish" : "Del 4 al 13 de julio y del 2 al 11 de agosto"
        }

South_heading_first = {
        "Chilean_Spanish" : "",
        "English" : "",
        "French" : "Dates à utiliser pour la Campagne ",
        "Indonesian" : "Waktu Kampanye ",
        "Portuguese" : "Datas das campanhas de ",
        "Spanish" : ""
        }

South_heading_middle = {
        "Chilean_Spanish" : " Fechas de campaña para la constelación del ",
        "English" : " Campaign Dates that use ",
        "French" : " ",
        "Indonesian" : " untuk ",
        "Portuguese" : " que usam ",
        "Spanish" : " Fechas de campaña para la constelación del "
        }

South_heading_last = {
        "Chilean_Spanish" : ": ",
        "English" : ": ",
        "French" : ": ",
        "Indonesian" : ": ",
        "Portuguese" : ": ",
        "Spanish" : ": "
        }

#updating northern hemisphere information (constellation, date, text displayed to user)
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
    
North_date_replacement = {
        
        "Catalan" : "30 d'octubre al novembre 8 i 29 de novembre de desembre 8",
        "Chinese" : "10月30日至11月 8月和11月29日至12月8",
        "Czech" : "30. října - 8. listopadu a 29. listopadu - 8. prosince",
        "English" : "Oct. 30-Nov. 8 and Nov. 29-Dec. 8",
        "Finnish" : "30 lokakuu- 8 marraskuu Ja 29 marraskuu-8 joulukuu" ,
        "French" : "Du 30 octobre au 8 novembre et du 29 novembre au 8 décembre" ,    
        "Galician" : "30 de outubro-8 de novembro e 29 de novembro-8 de decembro",
        "German" : "30. Oktober - 8. November und 29. November - 8. Dezember",
        "Greek" : "30 Οκτωβρίου-8 Νοεμβρίου και 29 Νοεμβρίου-8 Δεκεμβρίου",
        "Indonesian" : "30 Oktober-8 November dan 29 November-8 Desember",
        "Japanese" : "10月30日〜11月8日、11月29日〜12月8日",
        "Polish" : "30 października - 8 listopada i 29 listopada - 8 grudnia",
        "Portuguese" : "30 de outubro a 8 de novembro e 29 de novembro a 8 de dezembro",
        "Romanian" : "30 octombrie-8 noiembrie și 29 noiembrie-8 decembrie",
        "Serbian" : "30. октобра - 8. новембра и 29. новембра - 8. децембра",
        "Slovak" : "30. októbra - 8. novembra a 29. novembra - 8. decembra",
        "Slovenian" : "30. oktobra - 8. novembra in 29. novembra - 8. decembra",
        "Spanish" : "Del 30 de octubre al 8 de noviembre y del 29 de noviembre al 8 de diciembre",
        "Swedish" : "30. októbra - 8. novembra a 29. novembra - 8. decembra",
        "Thai" : "30 ตุลาคม - 8 พฤศจิกายนและ 29 พฤศจิกายน - 8 ธันวาคม"
            
        }

North_heading_first = {
    "Catalan" : "Dates de la campanya ",
    "Chinese" : ""  ,
    "Czech" : "Informace v této příručce jsou určeny pro pozorovací kampaň probíhající od ",
    "English" : "",
    "Finnish" : "",
    "French" : "Dates à utiliser pour la Campagne ",
    "Galician" : "Datas da campaña de ",
    "German" : "Kampagnendaten ",
    "Greek" : "",
    "Indonesian" : "Waktu Kampanye ",  
    "Japanese" : "",
    "Polish" : "",
    "Portuguese" : "Datas das campanhas de ",
    "Romanian" : "Perioadele campaniei din ",
    "Serbian" : "Сазвежђе ",
    "Slovak" : "V roku ",
    "Slovenian" :  "",
    "Spanish" :  "",
    "Swedish" : "Kampanjdatum för ",
    "Thai" : "กำหนดการในปีพ. ศ. "
    }

North_heading_middle = {
    "Catalan" : " en què usem la constel·lació, ",
    "Chinese" : "： "  ,
    "Czech" : ". Při pozorování použijte hvězdy oblohy, které zobrazují souhvězdí ",
    "English" : " Campaign Dates that use ",
    "Finnish" : " havainnointijaksot vuonna ",
    "French" : " ",
    "Galician" : " que usan ",
    "German" : " für das Sternbild ",
    "Greek" : " Ημερομηνίες παρατήρησης για τον αστερισμό του ",
    "Indonesian" : " untuk ",  
    "Japanese" : "年キャンペーン期間 (対象：",
    "Polish" : ": Daty kampanii używające ",
    "Portuguese" : " que usam ",
    "Romanian" : " pentru ",
    "Serbian" : " током ",
    "Slovak" : " môžete pozorovať súhvezdie ",
    "Slovenian" :  ": Datumi kampanje za opazovanje ",
    "Spanish" :  " Fechas de la campaña para ",
    "Swedish" : " ",
    "Thai" : " เซอุส"
    }

North_heading_last = {
    "Catalan" : " ",
    "Chinese" : "年"  ,
    "Czech" : ".",
    "English" : ": ",
    "Finnish" : ": ",
    "French" : ": ",
    "Galician" : ": ",
    "German" : ": ",
    "Greek" : ": ",
    "Indonesian" : ": ",  
    "Japanese" : ")：、",
    "Polish" : ": ",
    "Portuguese" : ": ",
    "Romanian" : ": ",
    "Serbian" : ". године посматрамо ",
    "Slovak" : ": ",
    "Slovenian" :  ": ",
    "Spanish" :  ": ",
    "Swedish" : ": ",
    "Thai" : "ดำเนินโครงการให้เสร็จสมบูรณ์: "
    }

#1date2con3
CountryList1 = ("Czech")
#1con2year3date
CountryList2 = ("Chinese", "Finnish", "Serbian", "Swedish")
#1year2Con3date
CountryList3 = ("Chilean_Spanish", "Catalan", "English", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Thai")  #1year2Con3date

First_Paragraph_first = {
    "Chilean_Spanish" : "Usted está participando en una campaña mundial para observar y registrar las estrellas visibles más débiles como un medio para medir la contaminación lumínica en un lugar determinado. Localizando y observando la constelación ",
    "Catalan" : "Esteu participant en una campanya mundial per observar i anotar la brillantor de les estrelles més febles que es poden veure, com a mitjà per mesurar la contaminació lumínica en un lloc determinat. Localitzant i observant la constel·lació ",
    "Chinese" : "你现在参加的是全球公益科普活动 Globe at Night （全球观星活动），这是一个以观察和记录夜空的可见恒星数来测量你所在地光污染情况的活动。通过定位和观测夜空中的",
    "Czech" : "Celosvětový projekt „Globe at Night“ nabízí možnost zapojit se do jednoduchého pozorování, které pomáhá mapovat světelné znečištění po celém světě. Stačí se kdykoli v níže uvedených intervalech v roce 2018 podívat na souhvězdí Bootes, Lva, Cygnus, Labutě, Pegase nebo Persea a s pomocí přiložených map hvězdného nebe určit, jak slabé hvězdy jste schopni na obloze pozorovat.", ####Figure out what to do with the Czech one
    "English" : "You are participating in a global campaign to observe and record the faintest stars visible as a means of measuring light pollution in a given location. By locating and observing the constellation ",
    "Finnish" : "Osallistut maailmanlaajuiseen tapahtumaan jossa havaitaan ja kirjataan himmeimmät nähtävissä olevat tähdet valosaasteen mittaamiseksi. Havaitsijat eri puolilla maailmaa etsivät ja havaitsevat Härkä tähtikuvion ja vertaavat sitä tähtikarttaan. Näin havaitaan, ",
    "French" :   "Vous allez participer à une campagne mondiale d’observation pour détecter les plus faibles étoiles visibles afin de mesurer la pollution lumineuse sur un site donné. Partout dans le monde, en localisant et en observant la constellation ",
    "Galician" : "Grazas por participar nesta campaña global de medida da contaminación lumínica mediante a observación das estrelas máis febles que podes albiscar. Localizando e observando a constelación de ",
    "German" : "Mach mit an einer weltweiten Kampagne, die schwächsten sichtbaren Sterne zu beobachten und aufzuzeichnen, um die Lichtverschmutzung an einem Ort zu messen. Durch das Auffinden und Beobachten des Sternbildes ",
    "Greek" : "Συμμετέχετε σε μία παγκόσμια καμπάνια για να παρατηρήσετε και να καταγράψετε τη φωτεινότητα των πιο αμυδρά ορατών άστρων σαν μέσο για την μέτρηση της Φωτορρύπανσης σε μία δεδομένη περιοχή. Με τον εντοπισμό και την παρατήρηση του αστερισμού του ",
    "Indonesian" : "Anda sedang berpartisipasi dalam kampanye global pengamatan dan pencatatan penampakan bintang paling redup untuk pengukuran tingkat polusi cahaya di suatu lokasi. Melalui pengamatan dan identifikasi Rasi ",
    "Japanese" : '街には人工光があふれ、夜空が照らされ、星が見えにくくなってきています。また、無駄・過剰な人工光は、莫大なエネルギーの浪費、生態系への悪影響、人間生活・人体への悪影響をも引き起こしています。この光害（ひかりがい）の問題を啓発する活動に、あなたも参加してみませんか。Globe at Night（グローブ・アット・ナイト）は市民参加型の、夜空の明るさ世界同時観察キャンペーンです。どなたでも簡単に参加できます。決められた日時に屋外に出て夜空を眺め、星の見え方をインターネットで報告するだけ。ぜひあなたも参加して、光害の問題を考えてみませんか。そして、世界中の人と、美しい星空・地球環境への思いを共有しましょう。',
    "Polish" : "Uczestniczysz w ogólnoświatowym przedsięwzięciu, którego celem jest obserwacja i odnotowanie najsłabszych widocznych gwiazd w celu zmierzenia zanieczyszczenia światłem w danym miejscu. Poprzez zlokalizowanie i obserwację gwiazdozbioru ",
    "Portuguese" : "Está a participar numa campanha global para observar e registar as estrelas mais fracas visíveis como forma de medir a poluição luminosa num determinado local. Localizando e observando a constelação de ",
    "Romanian" : "Prin această activitate participați în cadrul unei campanii globale de observare și consemnare a celor mai slabe stele vizibile ca metodă de măsurare a poluării luminoase dintr-un anumit loc. Localizând și observând constelația ",
    "Serbian" : "Ви сте учесници глобалног посматрачког пројекта, који има за циљ да одреди колико је светлосно загађене у средини у којој живите. Посматрајући звезде унутар сазвежђа ",
    "Slovak" : "Stávate sa súčasťou celosvetovej kampane Globe at Night, ktorej cieľom je meranie svetelného znečistenia. Pozorovaním súhvezdia ",
    "Slovenian" : "Sodelujete v svetovni aktivnosti opazovanja in beleženja najšibkejših, s prostim očesom  še vidnih zvezd, kot metode za merjenje svetlobnega onesnaževanja na določenem mestu. Z opazovanjem izbranega ozvezdja ",
    "Spanish" : "Usted está participando en una campaña mundial para observar y registrar las estrellas visibles más débiles como un medio para medir la contaminación lumínica en un lugar determinado. Localizando y observando la constelación ",
    "Swedish" : "Du deltar i en världsomspännande kampanj för att observera och rapportera de svagaste synliga stjärnorna, som ett mått på ljusföroreningarna på orten. Genom att hitta och observera stjärnbilden (",
    "Thai" : "คุณกำลังร่วมนโครงการระดับโลกที่จะสังเกตและบันทึกผลดาวฤกษ์ที่จางที่สุดที่มองเห็นได้ ซึ่งก็คือการวัดมลพิษทางแสงในสถานที่นั้นๆ  โดยการมองหาและสังเกต "

}

First_Paragraph_last = {
    "Chilean_Spanish" : " el cielo nocturno y comparándolo con las cartas estelares, la gente de todo el mundo aprenderá cómo las luces de su comunidad contribuyen a la contaminación lumínica. Sus contribuciones a la base de datos en línea documentarán el cielo nocturno visible.",
    "Catalan" : " a la nit i comparant la brillantor de les estrelles del cel amb la brillantor que indiquen els mapes, gent de tot el món aprendran com els llums de la seva zona contribueixen a augmentar la contaminació lumínica. Les vostres aportacions a la base de dades activa faran palesa la visibilitat del cel nocturn.",
    "Chinese" : "，并将所肉眼观察到的星等情况与所给出的星等图表作对比，我们可以知道自己社区中的人造光是如何导致光污染的。你所提供数据将和来自全世界的数据一起帮助建立一张全球光污染地图。",
    "Czech" : "Celosvětový projekt „Globe at Night“ nabízí možnost zapojit se do jednoduchého pozorování, které pomáhá mapovat světelné znečištění po celém světě. Stačí se kdykoli v níže uvedených intervalech v roce 2018 podívat na souhvězdí Bootes, Lva, Cygnus, Labutě, Pegase nebo Persea a s pomocí přiložených map hvězdného nebe určit, jak slabé hvězdy jste schopni na obloze pozorovat.", ###Figure something out with the Czech
    "English" : " in the night sky and comparing it to stellar charts, people from around the world will learn how the lights in their community contribute to light pollution. Your contributions to the online database will document the visible nighttime sky.",
    "Finnish" : " miten valosaaste syntyy kunkin taajaman tai muun ihmisen toiminnan valoista. Antamasi tiedot päivittyvät heti verkossa olevaan tietokantaan, ja näin saadaan käsitys siitä minkä verran taivaan tähdistä on missäkin nähtävissä.",
    "French" :   " dans le ciel nocturne et en la comparant aux cartes stellaires, les participants, apprendront comment l’éclairage, dans leur environnement local, influence la pollution lumineuse. Vos contributions à la base de données en ligne permettront de mesurer la qualité du ciel nocturne.",
    "Galician" : " e comparándoa co que aparece nos mapas estelares recollidos neste documento podes saber canto contribúen á contaminación lumínica os sistemas de iluminación que hai no teu barrio ou vila. As túas achegas á base de datos en liña de GLOBE at Night (O MUNDO á Noite) servirán para documentar a calidade do ceo nocturno.",
    "German" : " am Nachthimmel und den Vergleich mit den Helligkeitskarten, lernen Menschen auf der ganzen Erde, wie die Lichter in ihrer Gemeinde zur Lichtverschmutzung beitragen. Dein Beitrag zur Online-Datenbank beschreibt den sichtbaren Nachthimmel.",
    "Greek" : " στον νυχτερινό ουρανό καθώς και με την σύγκριση των ανωτέρω με τα διαγράμματα για τα μεγέθη των άστρων,  άνθρωποι από όλον τον κόσμο θα μάθουν πώς τα φώτα στην κοινότητά τους συμβάλλουν στην Φωτορρύπανση. Με την κατάθεση των πορισμάτων τους στην ιστοσελίδα θα δημιουργηθεί ένα αρχείο σχετικά με το τι μπορεί να δει κανείς στον νυχτερινό ουρανό.",
    "Indonesian" : " di langit malam dan membandingkannya dengan peta bintang, masyarakat di seluruh dunia dapat mengetahui dan mempelajari seberapa besar kontribusi cahaya di lingkungannya terhadap polusi cahaya. Kontribusi data anda pada basis data online akan membantu mendokumentasikan langit malam yang tampak di berbagai lokasi.",
    "Japanese" : "",
    "Polish" : " na nocnym niebie oraz porównanie go do map nieba ludzie z całego świata będą mogli dowiedzieć się jaki wkład światło emitowane przez ich społeczność wnosi do  zanieczyszczenia światłem. To co dodasz do internetowej bazy danych pomoże udokumentować widoczne nocne niebo.",
    "Portuguese" : " no céu noturno e,  comparando-a com cartas estelares, pessoas de todo o mundo aprenderão  como as luzes da sua comunidade contribuem para a poluição luminosa. As suas contribuições para a base de dados on-line irão documentar a visibilidade do céu noturno em todo o mundo.",
    "Romanian" : " pe cerul nopții și comparând-o cu diagramele stelare, oamenii din întreaga lume vor putea afla în ce măsură iluminatul nocturn din comunitatea lor contribuie la poluarea luminoasă. Contribuțiile dumneavoastră la baza de date online vor facilita o documentare globală privind cerul nocturn observabil.",
    "Serbian" : " и упоређујући их са приложеним звезданим картама, посматрачи широм света могу на практичном примеру да увиде колико је светлосно загађење у њиховој средини. Кроз учешће у овом пројекту, допринећете целовитијем сагледавању глобалног проблема.",
    "Slovak" : " na nočnej oblohe a porovnávaním skutočnej situácie s našimi mapkami sa nielenže dozviete, ako osvetlenie vo Vašom okolí prispieva k svetelnému znečisteniu, ale budete môcť porovnať úroveň svetelného znečistenia aj s inými lokalitami z celého sveta. Vaše pozorovanie tiež rozšíri online databázu dokumentujúcu viditeľnosť nočnej oblohy na našej planéte",
    "Slovenian" : " na nočnem nebu in s primerjavo videnega z zvezdnimi kartami, se lahko ljudje širom sveta podučijo o tem, kako svetila v njihovem kraju prispevajo k svetlobnemu onesnaževanju.  Vaši prispevki v spletno bazo podatkov bodo pomagali dokumentirati nočno nebo, vidno s prostim očesom.",
    "Spanish" : " el cielo nocturno y comparándolo con las cartas estelares, la gente de todo el mundo aprenderán cómo las luces de su comunidad contribuyen a la contaminación lumínica. Sus contribuciones a la base de datos en línea documentarán el cielo nocturno visible.",
    "Swedish" : ") på natthimlen kan folk i hela världen lära sig hur belysningen i våra samhällen och omgivningar bidrar till ljusföroreningar. Era bidrag till online-databasen hjälper till att dokumentera den synliga natthimlens över hela världen.",
    "Thai" : "ในท้องฟ้ายามค่ำคืนและเปรียบเทียบสิ่งที่เห็นกับแผนภาพที่เราให้า คนจากทั่วทุกมุมโลกจะได้เรียนรู้ว่าแสงไฟในชุมชนของพวกเขาสร้างมลพิษทางแสงอย่างไร ผลงานของคุณจะอยู่ในถูกเก็บในฐานข้อมูลออนไลน์ ซึ่งจะเป็นเอกสารเกี่ยวกับท้องฟ้ายามค่ำคืนที่เรามองเห็น",

}

##################################################################################################
##################################################################################################
###	End of the changes section defining things that need to be changed			###
##################################################################################################
##################################################################################################

#1date2con3
CountryList1 = ("Czech")
#1con2year3date
CountryList2 = ("Chinese", "Finnish", "Serbian", "Swedish")
#1year2Con3date
CountryList3 = ("Chilean_Spanish", "Catalan", "English", "French", "Galician", "German", "Greek", "Indonesian", "Japanese", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Thai")  #1year2Con3date

language_translate = {}
#goes through North_constellation_replacement and stores which language to translate to into language_translate
for key, value in North_constellation_replacement.items():
    for code, langs in lang.items():
        if key == "Chinese":
            language_translate[key] = "zh-cn"
        if key == langs.capitalize():
            language_translate[key] = code
#goes through South_constellation_replacement and stores which language to translate to into language_translate
for key, value in South_constellation_replacement.items():
     for code, langs in lang.items():
         if key == "Chilean_Spanish":
             language_translate[key] = "es"
         if key == langs.capitalize():
             language_translate[key] = code


#Be sure to change the websites
website1 = "astro/maps/GaNight/2018/"
website2 = "astro/maps/GaNight/2019/"

hyperlink_website = "http://amper.ped.muni.cz/jenik/astro/maps/GaNight/{year}/".format(year = year)
    #get the proper translations for the specfic date and constellation
for key, value in new_constellation_north.items():
    try:
        os.mkdir("GaN{year}_ActivityGuide_{cons}_N".format(year = year, cons = key))
    except:
        rmtree(os.path.join(os.getcwd(),"GaN{year}_ActivityGuide_{cons}_N".format(year = year, cons = key)))
        os.mkdir("GaN{year}_ActivityGuide_{cons}_N".format(year = year, cons = key))
    cut_star_chart("30-{constellation}-1.png".format(constellation = key))
    print("_____________________________________________________________\n")
    print("Working on constellation {cons}\n".format(cons = key))
    #replace the translations in the proper places
    for language, constellation in North_constellation_replacement.items():
        save_path = os.getcwd() + "/GaN{year}_ActivityGuide_{cons}_N/".format(year = year, cons = key)
        save_name = "GaN" + str(year) + "_ActivityGuide_" + str(key) + "_N_" + str(language) + ".docx"
        save_name_pdf = "GaN" + str(year) + "_ActivityGuide_" + str(key) + "_N_" + str(language) + ".pdf"
        
	#create the path to the updated activity guide
        total_path = os.path.join(save_path, save_name)
        total_path_pdf = os.path.join(save_path, save_name_pdf)
        print(language)
        print("Working...\n")
        try:
            new_dates_trans = mtranslate.translate(value, language_translate[language],"en")
            new_cons_trans = mtranslate.translate(key, language_translate[language],"en")
	#if trying to translate the dates and constellations takes too much time, try again
        except TimeoutError:
            time.sleep(10)
            new_dates_trans = mtranslate.translate(value, language_translate[language],"en")
            new_cons_trans = mtranslate.translate(key, language_translate[language],"en")
        
        working_doc = open_word_doc("GaN2018_ActivityGuide_Perseus_N_" + str(language) + ".docx")  
 	
	#collect information from previous activity guide to keep future activity guides consistent
        obj_styles = working_doc.styles
        obj_charstyle = obj_styles.add_style('GaNStyle', WD_STYLE_TYPE.CHARACTER)
        obj_font = obj_charstyle.font
        obj_font.name = 'Calibri'
        obj_font.size = Pt(12)
        
        obj_styles2 = working_doc.styles
        obj_charstyle2 = obj_styles2.add_style('GaNParagraph', WD_STYLE_TYPE.CHARACTER)
        obj_font2 = obj_charstyle2.font
        obj_font2.name = 'Calibri'
        obj_font2.size = Pt(10)
        
        obj_styles3 = working_doc.styles
        obj_charstyle3 = obj_styles3.add_style('GaNLinks', WD_STYLE_TYPE.CHARACTER)
        obj_font3 = obj_charstyle3.font
        obj_font3.name = 'Calibri'
        obj_font3.size = Pt(9.5)
        
        #goes through the word document and updates constellation and date information   
        for paragraph in working_doc.paragraphs:
            if constellation in paragraph.text:
                if North_date_replacement[language] in paragraph.text:
                  
                    paragraph.clear()
			
                    if language in CountryList1:
					
                        paragraph.add_run(North_heading_first[language] + str(new_dates_trans) + North_heading_middle[language] + str(new_cons_trans) + North_heading_last[language], style = 'GaNStyle')
						
                    elif language in CountryList2:
					
                        paragraph.add_run(North_heading_first[language] + str(new_cons_trans) + North_heading_middle[language] + str(year) + North_heading_last[language] + str(new_dates_trans) + ".", style = 'GaNStyle')
                   
                    elif language in CountryList3:
					
                        if language != "Thai":
                            paragraph.add_run(North_heading_first[language] + str(year) + North_heading_middle[language] + str(new_cons_trans) + North_heading_last[language] + str(new_dates_trans) + ".", style = 'GaNStyle')
                        else:
                            paragraph.add_run(North_heading_first[language] + str(Thai_year) + North_heading_middle[language] + str(new_cons_trans) + North_heading_last[language] + str(new_dates_trans) + ".", style = 'GaNStyle')        
            
                else:
                    paragraph.clear() #delete paragraph that is no longer relevant to current campaign
                    if (language != 'Japanese'):
                    
                        paragraph.add_run(First_Paragraph_first[language] + str(new_cons_trans) + First_Paragraph_last[language], style = 'GaNParagraph')
                            
                    else:
                        
                        paragraph.add_run(First_Paragraph_first[language] + First_Paragraph_last[language], style = 'GaNParagraph')
	    #updates the year in the websites				
            if website1 in paragraph.text:
                new_text = paragraph.text.replace("2018",str(year))
                paragraph.text = None
                paragraph.add_run(new_text, style = 'GaNLinks')
                
            elif website2 in paragraph.text:
                new_text = paragraph.text.replace("2019",str(year))
                paragraph.text = None
                paragraph.add_run(new_text, style = 'GaNLinks')
                
        i = 0
        k = 0
        l = 0              
        for table in working_doc.tables:
            #inserts the approprite cropped pictures based on magnitude
            Big_picture_cells = (table.cell(1,0), table.cell(1,2), table.cell(4,0), table.cell(4,2))
            small_picture_cells = (table.cell(1,0), table.cell(1,1), table.cell(1,2), table.cell(1,3), table.cell(3,0), table.cell(3,1), table.cell(3,2), table.cell(3,3))
            
            if i < 2:
                for tableCell in Big_picture_cells:
                    tableCell.paragraphs[1].clear()
                                        
                    tableCell.paragraphs[1].add_run().add_picture("Mag" + str(k) + ".png", width = Inches(3.39), height = Inches(2.35))
                    working_doc.save(total_path)
                    k = k + 1
            
            else :
                for tableCell in small_picture_cells:
                    tableCell.paragraphs[0].clear()
                    tableCell.paragraphs[0].add_run().add_picture("Mag" + str(l) + ".png", width = Inches(1.44), height = Inches(1.01))
                    working_doc.save(total_path)
                    l = l + 1
                
            i = i + 1
        working_doc.save(total_path)
        
        print(language + " activity guide is done.\n")
    print("Done working on constellation {cons}\n".format(cons = key))
    print("_____________________________________________________________\n")                        

#begin the process again to update the southern hemisphere activity guides
for key,value in new_constellation_south.items():
    try:
        os.mkdir("GaN{year}_ActivityGuide_{cons}_S".format(year = year, cons = key))
    except:
        rmtree(os.path.join(os.getcwd(),"GaN{year}_ActivityGuide_{cons}_S".format(year = year, cons = key)))
        os.mkdir("GaN{year}_ActivityGuide_{cons}_S".format(year = year, cons = key))
    try:
        cut_star_chart("30s-{constellation}-1.png".format(constellation = key))
    except:
        cut_star_chart("30s-Canis_Major-1.png")
    print("_____________________________________________________________\n")
    print("Working on constellation {cons}\n".format(cons = key))
    for language, constellation in South_constellation_replacement.items():
        
        save_path = os.getcwd() + "/GaN{year}_ActivityGuide_{cons}_S/".format(year = year, cons = key)
        save_name = "GaN" + str(year) + "_ActivityGuide_" + str(key) + "_S_" + str(language) + ".docx"
        save_name_pdf = "GaN" + str(year) + "_ActivityGuide_" + str(key) + "_S_" + str(language) + ".pdf"
        
        total_path = os.path.join(save_path, save_name)
        total_path_pdf = os.path.join(save_path, save_name_pdf)
        
        print(language)
        print("Working...")
        try:
            new_dates_trans = mtranslate.translate(value, language_translate[language],"en")
            new_cons_trans = mtranslate.translate(key, language_translate[language],"en")
        except TimeoutError:
            time.sleep(10)
            new_dates_trans = mtranslate.translate(value, language_translate[language],"en")
            new_cons_trans = mtranslate.translate(key, language_translate[language],"en")
        
        working_doc = open_word_doc("GaN2018_ActivityGuide_Scorpius_S_" + str(language) + ".docx") 
        
        obj_styles = working_doc.styles
        obj_charstyle = obj_styles.add_style('GaNStyle', WD_STYLE_TYPE.CHARACTER)
        obj_font = obj_charstyle.font
        obj_font.name = 'Calibri'
        obj_font.size = Pt(14)
        
        obj_styles2 = working_doc.styles
        obj_charstyle2 = obj_styles2.add_style('GaNParagraph', WD_STYLE_TYPE.CHARACTER)
        obj_font2 = obj_charstyle2.font
        obj_font2.name = 'Calibri'
        obj_font2.size = Pt(10)
        
        obj_styles3 = working_doc.styles
        obj_charstyle3 = obj_styles3.add_style('GaNLinks', WD_STYLE_TYPE.CHARACTER)
        obj_font3 = obj_charstyle3.font
        obj_font3.name = 'Calibri'
        obj_font3.size = Pt(9.5)
        
        for paragraph in working_doc.paragraphs:
            if constellation in paragraph.text:
                if South_date_replacement[language] in paragraph.text:
                    
                    paragraph.clear()
                    paragraph.add_run(South_heading_first[language] + str(year) + South_heading_middle[language] + str(new_cons_trans) + South_heading_last[language] + str(new_dates_trans) + ".", style = 'GaNStyle')
                
                else:
                    
                    paragraph.clear()
                    paragraph.add_run(First_Paragraph_first[language] + str(new_cons_trans) + First_Paragraph_last[language], style = 'GaNParagraph')
                    
            if website1 in paragraph.text:
                new_text = paragraph.text.replace("2018",str(year))
                paragraph.text = None
                paragraph.add_run(new_text, style = 'GaNLinks')
                
            elif website2 in paragraph.text:
                new_text = paragraph.text.replace("2019",str(year))
                paragraph.text = None
                paragraph.add_run(new_text, style = 'GaNLinks')   
        i = 0
        k = 0
        l = 0              

        for table in working_doc.tables:
            
            print(table.cell)
            Big_picture_cells = (table.cell(1,0), table.cell(1,2), table.cell(4,0), table.cell(4,2))
            small_picture_cells = (table.cell(1,0), table.cell(1,1), table.cell(1,2), table.cell(1,3), table.cell(3,0), table.cell(3,1), table.cell(3,2), table.cell(3,3))
            
            if i < 2:
                for tableCell in Big_picture_cells:
                    tableCell.paragraphs[1].clear()
                                        
                    tableCell.paragraphs[1].add_run().add_picture("Mag" + str(k) + ".png", width = Inches(3.39), height = Inches(2.35))
                    working_doc.save(total_path)
                    k = k + 1
            
            else :
                for tableCell in small_picture_cells:
                    tableCell.paragraphs[0].clear()
                    tableCell.paragraphs[0].add_run().add_picture("Mag" + str(l) + ".png", width = Inches(1.44), height = Inches(1.01))
                    working_doc.save(total_path)
                    l = l + 1
                
            i = i + 1  

        working_doc.save(total_path)
        
        print(language + " activity guide is done.\n")
    print("Done working on constellation {cons}\n".format(cons = key))
    print("_____________________________________________________________\n")



#If it is possible to convert them to pdfs on your system this will run, otherwise it will throw an error.
dtp.docxtopdf()
