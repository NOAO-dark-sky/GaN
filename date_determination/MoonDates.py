import csv
#ephem can perform astronomical calculations
#Install Ephem
import ephem as ep
import numpy as np
import pandas as pd
import time
from datetime import datetime
import pytz
localFormat = "%Y/%m/%d %H:%Mi:%S"

counter_old = 0
counter_new = 0

#use ephem to access built in cities
Munich = ep.city("Munich")
Boston = ep.city("Boston")
Mexico_City = ep.city("Mexico City")
Dublin = ep.city("Dublin")
Madrid = ep.city("Madrid")
Houston = ep.city("Houston")
Caracas = ep.city("Caracas")
Auckland = ep.city("Auckland")
Brisbane = ep.city("Brisbane")
Cape_Town = ep.city("Cape Town")

Munich.date = '2020'
Boston.date = '2020'
Mexico_City.date = '2020'
Dublin.date = '2020'
Madrid.date = '2020'
Houston.date = '2020'
Caracas.date = '2020'
Auckland.date = '2020'
Brisbane.date = '2020'
Cape_Town.date = '2020'

number_to_city = {0 : "Munich",
        1 : "Boston",
        2 : "Mexico_City",
        3 : "Dublin",
        4 : "Madrid",
        5 : "Houston",
        6 : "Caracas",
        7 : "Auckland",
        8 : "Brisbane",
        9 : "Cape_Town"}

#access city latitude using ephem
City_lats = {"Munich" : Munich.lat,
        "Boston" : Boston.lat,
        "Mexico_City" : Mexico_City.lat,
        "Dublin" : Dublin.lat,
        "Madrid" : Madrid.lat,
        "Houston" : Houston.lat,
        "Caracas" : Caracas.lat,
        "Auckland" : Auckland.lat,
        "Brisbane" : Brisbane.lat, 
        "Cape_Town" : Cape_Town.lat}

local_time_conversion_regular = {"Munich" : "Europe/Berlin",
        "Boston" : "US/Eastern",
        "Mexico_City" : "America/Mexico_City",
        "Dublin" : "Europe/Dublin",
        "Madrid" : "Europe/Madrid",
        "Houston" : "US/Central",
        "Caracas" : "America/Caracas",
        "Auckland" : "Pacific/Auckland",
        "Brisbane" : "Australia/Brisbane", 
        "Cape_Town" : "Africa/Johannesburg"}

Northern_Cities = ["Munich", "Boston", "Mexico_City", "Dublin", "Madrid", "Houston", "Caracas"]
Southern_Cities = ["Auckland", "Brisbane", "Cape_Town"]

#Set the moon object up
moon = ep.Moon()
sun = ep.Sun()

#open file, enter in moon headers (start, end, moon phase)
with open('Moon_Dates_qv.csv', mode = 'w+') as f:
    moon_writer = csv.writer(f,delimiter = ',' , quotechar = '"')
    moon_writer.writerow(['Start', 'End','Moon Phase'])

#open file, enter in moon headers (latitude, year, month, etc)
with open('Moon_Dates.csv', mode = 'w+') as f:
    moon_writer = csv.writer(f,delimiter = ',' , quotechar = '"')
    moon_writer.writerow(['Latitude', 'Year', 'Month', 'Day', 'Moon Phase', 'Sunset Time (local)', 'Moonrise Time (local)', 'Moonset Time (local)'])

moon.compute(Munich)
old_phase = moon.phase
#Compute the next setting and rising times for the moon
for i in range(3650 * 4):
    #set horizon to a negative value, horizon: the altitude of the upper limb of a body at the moment
    #you consider it to be rising and setting
    #https://rhodesmill.org/pyephem/quick.html
    Munich.horizon = '-12'
    Boston.horizon = '-12'
    Mexico_City.horizon = '-12'
    Dublin.horizon = '-12'
    Madrid.horizon = '-12'
    Houston.horizon = '-12'
    Caracas.horizon = '-12'
    Auckland.horizon = '-12'
    Brisbane.horizon = '-12'
    Cape_Town.horizon = '-12'
    
    if i != 0:
        
        Munich.date = S1
        Boston.date = S2
        Mexico_City.date = S3
        Dublin.date = S4
        Madrid.date = S5
        Houston.date = S6
        Caracas.date = S7
        Auckland.date = S8
        Brisbane.date = S9
        Cape_Town.date = S0

    #calculate when the sun sets at each city, use the center of the sun to tell when the sun sets (time, day, month, and year)
    S1 = Munich.next_setting(sun, use_center = True) 
    S2 = Boston.next_setting(sun, use_center = True) 
    S3 = Mexico_City.next_setting(sun, use_center = True) 
    S4 = Dublin.next_setting(sun, use_center = True) 
    S5 = Madrid.next_setting(sun, use_center = True) 
    S6 = Houston.next_setting(sun, use_center = True)
    S7 = Caracas.next_setting(sun, use_center = True)
    S8 = Auckland.next_setting(sun, use_center = True)
    S9 = Brisbane.next_setting(sun, use_center = True)
    S0 = Cape_Town.next_setting(sun, use_center = True)

    sun_setting_times = [S1,S2,S3,S4,S5,S6,S7,S8,S9,S0]
    
    if i != 0:

        Munich.date = M1
        Boston.date = M2
        Mexico_City.date = M3
        Dublin.date = M4
        Madrid.date = M5
        Houston.date = M6
        Caracas.date = M7
        Auckland.date = M8
        Brisbane.date = M9
        Cape_Town.date = M0

    #ignore PyEphem refrection
    Munich.horizon = '-0:34'
    Boston.horizon = '-0:34'
    Mexico_City.horizon = '-0:34'
    Dublin.horizon = '-0:34'
    Madrid.horizon = '-0:34'
    Houston.horizon = '-0:34'
    Caracas.horizon = '-0:34'
    Auckland.horizon = '-0:34'
    Brisbane.horizon = '-0:34'
    Cape_Town.horizon = '-0:34'

    #calculate when the moon sets at each city (time, day, month, year)
    M1 = Munich.next_setting(moon) 
    M2 = Boston.next_setting(moon) 
    M3 = Mexico_City.next_setting(moon) 
    M4 = Dublin.next_setting(moon) 
    M5 = Madrid.next_setting(moon) 
    M6 = Houston.next_setting(moon)
    M7 = Caracas.next_setting(moon)
    M8 = Auckland.next_setting(moon)
    M9 = Brisbane.next_setting(moon)
    M0 = Cape_Town.next_setting(moon)

    setting_times = [M1,M2,M3,M4,M5,M6,M7,M8,M9,M0]

    if i != 0:

        Munich.date = r1
        Boston.date = r2
        Mexico_City.date = r3
        Dublin.date = r4
        Madrid.date = r5
        Houston.date = r6
        Caracas.date = r7
        Auckland.date = r8
        Brisbane.date = r9
        Cape_Town.date = r0

    #calculates when the moon rises at each city
    r1 = Munich.next_rising(moon)
    r2 = Boston.next_rising(moon)
    r3 = Mexico_City.next_rising(moon)
    r4 = Dublin.next_rising(moon)
    r5 = Madrid.next_rising(moon)
    r6 = Houston.next_rising(moon)
    r7 = Caracas.next_rising(moon)
    r8 = Auckland.next_rising(moon)
    r9 = Brisbane.next_rising(moon)
    r0 = Cape_Town.next_rising(moon)

    rising_times = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r0]
    #determine if the time is in the proper range.
    
    all_rise_and_set_times = {"moonrise" : rising_times,
                                "moonset" : setting_times,
                                "sunset" : sun_setting_times}

    #moonrise time between 2200 and 0600
    final_countdown = 0
    new_phase = ep.Moon(M8).phase 
    for city in range(10):
        #record each city's moonrise, moonset, and sunset
        rise_t = all_rise_and_set_times["moonrise"][city]
        set_t = all_rise_and_set_times["moonset"][city]
        sunset_t = all_rise_and_set_times["sunset"][city]


        datetime_moonrise_naive = datetime(rise_t.tuple()[0],rise_t.tuple()[1],rise_t.tuple()[2],rise_t.tuple()[3],rise_t.tuple()[4],int(rise_t.tuple()[5]))
        datetime_moonrise = datetime_moonrise_naive.replace(tzinfo = pytz.utc)
        localDate_and_time_moonrise = datetime_moonrise.astimezone(pytz.timezone(local_time_conversion_regular[number_to_city[city]]))

        datetime_moonset_naive = datetime(set_t.tuple()[0],set_t.tuple()[1],set_t.tuple()[2],set_t.tuple()[3],set_t.tuple()[4],int(set_t.tuple()[5]))
        datetime_moonset = datetime_moonset_naive.replace(tzinfo = pytz.utc)
        localDate_and_time_moonset = datetime_moonset.astimezone(pytz.timezone(local_time_conversion_regular[number_to_city[city]]))

        datetime_sunset_naive = datetime(sunset_t.tuple()[0],sunset_t.tuple()[1],sunset_t.tuple()[2],sunset_t.tuple()[3],sunset_t.tuple()[4],int(sunset_t.tuple()[5]))
        datetime_sunset = datetime_sunset_naive.replace(tzinfo = pytz.utc)
        localDate_and_time_sunset = datetime_sunset.astimezone(pytz.timezone(local_time_conversion_regular[number_to_city[city]]))

        if(counter_new == 1) and (counter_old == 0) and (old_phase - new_phase < -0.032):
            final_countdown += 1

        if (counter_new == 0) and (counter_old == 1) and (old_phase - new_phase <-0.032):
            counter_new = 1
            counter_old = 0

        if (ep.Moon(set_t).phase/100 <= 0.71) and (old_phase - new_phase >= -0.032):
            
            if (counter_new == 0) and (counter_old == 0):
                startday = localDate_and_time_moonset.day
                startmonth = localDate_and_time_moonset.month
                startyear = localDate_and_time_moonset.year
                counter_old = 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Adding the information to the large file for closer examination~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            with open('Moon_Dates.csv', mode = 'a') as f:
                moon_writer = csv.writer(f,delimiter = ',' , quotechar = '"')
                if (localDate_and_time_moonset.minute < 10) and (localDate_and_time_moonrise.minute >= 10) and (localDate_and_time_sunset.minute >= 10):

                    moon_writer.writerow([number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:0{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])
                
                elif (localDate_and_time_moonset.minute < 10) and (localDate_and_time_moonrise.minute < 10) and (localDate_and_time_sunset.minute >= 10):

                    moon_writer.writerow([number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:0{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:0{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute < 10) and (localDate_and_time_moonrise.minute < 10) and (localDate_and_time_sunset.minute < 10):

                    moon_writer.writerow([number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:0{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:0{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:0{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute >= 10) and (localDate_and_time_moonrise.minute < 10) and (localDate_and_time_sunset.minute < 10):

                    moon_writer.writerow([ number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:0{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:0{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute >= 10) and (localDate_and_time_moonrise.minute >= 10) and (localDate_and_time_sunset.minute < 10):

                    moon_writer.writerow([ number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:0{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute >= 10) and (localDate_and_time_moonrise.minute >= 10) and (localDate_and_time_sunset.minute >= 10):

                    moon_writer.writerow([ number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute >= 10) and (localDate_and_time_moonrise.minute < 10) and (localDate_and_time_sunset.minute >= 10):

                    moon_writer.writerow([ number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:0{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])

                elif (localDate_and_time_moonset.minute < 10) and (localDate_and_time_moonrise.minute >= 10) and (localDate_and_time_sunset.minute < 10):

                    moon_writer.writerow([ number_to_city[city], localDate_and_time_moonset.year, localDate_and_time_moonset.month, localDate_and_time_moonset.day, ep.Moon(set_t).phase/100.0, '{H}:0{minute}'.format(H = localDate_and_time_sunset.hour, minute = localDate_and_time_sunset.minute), '{H}:{minu}'.format(H = localDate_and_time_moonrise.hour, minu = localDate_and_time_moonrise.minute), '{H}:0{MIN}'.format(H = localDate_and_time_moonset.hour, MIN = localDate_and_time_moonset.minute)])



    if(counter_new == 1) and (counter_old == 0) and (final_countdown == 9):
        
        with open('Moon_Dates_qv.csv', mode = 'a') as f:

            moon_writer = csv.writer(f,delimiter = ',' , quotechar = '"')
            moon_writer.writerow(["{Y}/{M}/{D}".format(Y = startyear, M = startmonth, D = startday), "{Y}/{M}/{D}".format(Y = localDate_and_time_moonrise.year, M = localDate_and_time_moonrise.month, D = localDate_and_time_moonrise.day), old_phase/100.0])
            counter_new = 0
            counter_old = 0
    old_phase = new_phase
    if(i % 365 == 0):
        print("Next Year")
        



#Time to determine which constellations go where. We will use skyfield
#Install Skyfield
import skyfield as sf

with sf.api.load.open(sf.data.hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)


north_constellation_check = {"Perseus" : , 
