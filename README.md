# GaN (Globe at Nigth) Activity Guides Generator


## Table of contents
* [Description](#description)
* [Languages](#laguages)
* [Constellations](#constellations)
* [Technologies](#technologies)
* [Charts](#charts)
* [How it works](#how_it_works)
* [Project Status](#project_status)

## Description

Welcome. This software makes it possible to create several Activity guides for the Globe at Night campaign, a worldwide citizen science movement, in multiple languages. Users can measure and report their observations of the night sky brightness thanks to the Activity instructions that will be accessible in PDF format for the constellations.

## Languages

The 20 Languages for the GaN Activity guide are:
* Catalan
* Chinese (Traditional)
* Czech
* English
* Finnish
* French
* Galician
* German
* Greek
* Indonesian
* Japanese
* Polish
* Portuguese
* Romanian
* Serbian
* Slovak
* Slovenian
* Spanish
* Swedish
* Thai

## Constellations:

### Northern Hemisphere:
* Bootes
* Cygnus
* Gemini
* Hercules
* Leo
* Orion
* Pegasus
* Perseus
* Taurus

### Southern Hemisphere:
* Bootes
* Canis Major
* Crux
* Grus
* Hercules
* Leo
* Orion
* Pegasus
* Perseus
* Sagittarius
* Scorpius
* Taurus

# Technologies
* MS Word
* MS Excel
* Python 3:
    * os
    * time
    * sys
    * deeep_translator
    * python-docx
    * pandas
    * shutil
    * multiprocessing
    * BeautifulSoup
    * Requests

## charts
The charts are taken from the website "https://www.globeatnight.org/magcharts"

## How it works 
1. The constellations and the observation dates must be created, edited and saved in the excel file: Gan_cons_and_dates.xlsx
2. The Activity Guides changes should be edited in the word files for each language
3. While runnig the program, the different aActivity guides for the selected contellations and languages will be created and saved in PDF  format.

## Project status

Now working on the .docx to .pdf conversion (last actualization 07-17-2022)
