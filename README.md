# GaN (Globe at Nigth) Activity Guides Generator


## Table of contents
* [Description](#description)
* [Languages](#laguages)
* [Constellations](#constellations)
* [Technologies](#technologies)
* [How it works](#how_it_works)

## Description

Welcome. This software makes it possible to create several Activity guides for the Globe at Night campaign, a worldwide citizen science movement, in multiple languages. Users can measure and report their observations of the night sky brightness thanks to the several Activity instructions that will be accessible in PDF format for the constellations.

## Languages

The 20 Languages for the GaN Activity guide are:
Catalan
Chinese (Traditional)
Czech
English
Finnish
French
Galician
German
Greek
Indonesian
Japanese
Polish
Portuguese
Romanian
Serbian
Slovak
Slovenian
Spanish
Swedish
Thai

## Constellations:

### Northern Hemisphere:
Bootes
Cygnus
Gemini
Hercules
Leo
Orion
Pegasus
Perseus
Taurus

### Southern Hemisphere:
Bootes
Canis Major
Crux
Grus
Hercules
Leo
Orion
Pegasus
Sagittarius
Scorpius
Taurus

# Technologies
MS Word
MS Excel
Python:
    os
    time
    sys
    deeep_translator
    python-docx
    pandas
    shutil
    multiprocessing

## How it works 
1. The constellations and the observation dates must be created, edited and saved in the excel file: Gan_cons_and_dates.xlsx
2. The Activity Guides changes should be edited in the word files for each languages
3. While runnig the program the different aActivity guides for the selected contellations and languages will be created and saved.
