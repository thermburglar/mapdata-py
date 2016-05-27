# This script cleans the static jobs data for VALU Career Mapping Tools.  The cleaning entails revising the city/state information to remove typos and then assigns a lat/long to each record, by comparing to lists of collected city/states, as well as by pinging the google geocoding service.

# script written by Erin Comparri 4/26/2012 erin.comparri at gmail dot com for Federal Management Partners

import csv, os, sys
from geopy import geocoders

# open the typo dictionary
typofile = os.path.abspath('C:\\Cartography\\Contract\\2012\\Phase3\\Data\\typos.csv')
typoreader = csv.DictReader(open(typofile, 'rb'), delimiter = ',', quotechar = '"') 
typoDict = dict()
for row in typoreader:
        typoName = row["Name"].strip().upper()
        typoNewName = row["NewName"].strip().upper()
        typoDict[typoName] = typoNewName	

# open the city lat/long files 
citydetails = os.path.abspath('C:\\Cartography\\Contract\\2011\\VAToolkit\\Tables\\AdditionalCities.csv')
cityReader = csv.DictReader(open(citydetails, 'rb'), delimiter = ',', quotechar = '"')
cityDict = dict()

for row in cityReader:
        cityDict[row["Name"].strip().upper()] = (row["Lat"],row["Lon"])

morecities = os.path.abspath('C:\\Cartography\\Map Data\\NorthAmerica\\US\\cities_detl.csv')
moreReader = csv.DictReader(open(morecities, 'rb'), delimiter = ',', quotechar = '"')

for row in moreReader:
        cityDict[row["CityState"].strip().upper()] = (row["Lat"],row["Lon"])

# Open the file containing data to be cleaned

afile = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\ClientData\\JanuaryMaps\\JanuaryMap_raw.csv')
#afile = os.path.abspath('C:\\Cartography\\Contract\\2012\\Phase3\\Data\\jobsdata_full_v2.csv')
#afile = os.path.abspath('C:\\Users\\Eri\\Roaming\\SeptMapSource.csv')
jobsReader = csv.DictReader(open(afile, 'rb'), delimiter = ',', quotechar = '"')

# open the file to write the cleaned rows to
temp = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\ClientData\\JanuaryMaps\\JanuaryMap.csv')
k = open(temp, 'w')
k.write("DUTY STA;LOCATION;CITY;ST;CityState;VISN;SERIES;SERIES NAME;FAMILY;OST;OST DESC;PLAN;GRADE;ADMIN;ADMIN2;COST CENTER .ORG;COST CENTER ORG DESCRIPTION;COST CENTER;COST CENTER DESCRIPTION;DUTY BASIS;SUPV;TYPE APPT;LAT;LONG\n")
#k.write("DUTY STA;LOCATION;CityState;VISN;SERIES;SERIES NAME;FAMILY;OST;OST DESC;PLAN;GRADE;ADMIN;ADMIN2;COST CENTER .ORG;COST CENTER ORG DESCRIPTION;COST CENTER;COST CENTER DESCRIPTION;DUTY BASIS;SUPV;TYPE APPT;LAT;LONG\n")
#k.write("ID,DUTY STA,CITY,ST,SERIES,SERIES NAME,FAMILY,OST,OST DESC,LAT,LONG\n")
#k.write("DUTY STA,LOCATION,CITY,ST,VISN,SERIES,SERIES NAME,FAMILY,OST,OST DESC,PLAN,GRADE,ADMIN,ADMIN3,COST CENTER .ORG,COST CENTER ORG DESCRIPTION,COST CENTER,COST CENTER DESCRIPTION,DUTY BASIS,SUPV,TYPE APPT,LAT,LONG\n")

# file for rows that need more attention
unfound = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\ClientData\\JanuaryMaps\\JanNeedsAttention.csv')
ugh = open(unfound, 'w')

delimiter = ','
quote = '\"'
addlcitytest = os.path.abspath('C:\\Cartography\\Contract\\2012\\Phase3\\Data\\typos_test.csv')
out_f = open(addlcitytest, 'w')

# iterate over each line in the data to be cleaned, revising the city/state where matches are found in the typo directory and then fetching the coordinates to append.  Write the row to the cleaned file if coords are found, and in an exception file otherwise.
print "Working... (really!)"

for row in jobsReader:
        citystate = (row["CITY"].strip() + ', ' + row["ST"].strip()).upper()
       # citystate = (row["CityState"])
#        print citystate
        if citystate in typoDict:
                citystate = typoDict.get(citystate)
        if citystate in cityDict:
                coords = cityDict[citystate]
                #k.write(row["CITY"]+","+row["ST"]+","+row["SERIES"]+","+row["SERIES NAME"]+","+row["FAMILY"]+","+row["OST"]+","+row["OST DESC"]+","+ str(coords[0]) + "," + str(coords[1]) + "\n")
                k.write(row["DUTY STA"] + ";" + row["LOCATION"] + ";" + row["CITY"] + ";" + row["ST"] + ";" + citystate + ";" + row["VISN"] + ";" + row["SERIES"] + ";" + row["SERIES NAME"] + ";" + row["FAMILY"] + ";" + row["OST"] + ";" + row["OST DESC"] + ";" + row["PLAN"] + ";" + row["GRADE"] + ";" + row["ADMIN"] + ";" + row["ADMIN2"] + ";" + row["COST CENTER .ORG"] + ";" + row["COST CENTER ORG DESCRIPTION"] + ";" + row["COST CENTER"] + ";" + row["COST CENTER DESCRIPTION"] + ";" + row["DUTY BASIS"] + ";" + row["SUPV"] + ";" + row["TYPE APPT"] + ";" +  str(coords[0]) + ";" + str(coords[1])+ "\n")
                #k.write(row["DUTY STA"] + ";" + row["LOCATION"] + ";" + citystate + ";" + row["VISN"] + ";" + row["SERIES"] + ";" + row["SERIES NAME"] + ";" + row["FAMILY"] + ";" + row["OST"] + ";" + row["OST DESC"] + ";" + row["PLAN"] + ";" + row["GRADE"] + ";" + row["ADMIN"] + ";" + row["ADMIN2"] + ";" + row["COST CENTER .ORG"] + ";" + row["COST CENTER ORG DESCRIPTION"] + ";" + row["COST CENTER"] + ";" + row["COST CENTER DESCRIPTION"] + ";" + row["DUTY BASIS"] + ";" + row["SUPV"] + ";" + row["TYPE APPT"] + ";" +  str(coords[0]) + ";" + str(coords[1])+ "\n")
#                print citystate +" "+str(coords[0])+", "+str(coords[1])
        else:
                try:
                        g = geocoders.Google()
                        place, (lat,lng) = g.geocode(citystate)
                        print place + " from Google"
                        cityDict[citystate] = (lat,lng)
                        out_f.write(quote + citystate + quote + delimiter + str(coords[0]) + delimiter + str(coords[1])+ "\n")
                        k.write(row["DUTY STA"] + ";" + row["LOCATION"] + ";" + row["CITY"] + ";" + row["ST"] + ";" + citystate + ";" + row["VISN"] + ";" + row["SERIES"] + ";" + row["SERIES NAME"] + ";" + row["FAMILY"] + ";" + row["OST"] + ";" + row["OST DESC"] + ";" + row["PLAN"] + ";" + row["GRADE"] + ";" + row["ADMIN"] + ";" + row["ADMIN2"] + ";" + row["COST CENTER .ORG"] + ";" + row["COST CENTER ORG DESCRIPTION"] + ";" + row["COST CENTER"] + ";" + row["COST CENTER DESCRIPTION"] + ";" + row["DUTY BASIS"] + ";" + row["SUPV"] + ";" + row["TYPE APPT"] + ";" +  str(coords[0]) + ";" + str(coords[1])+ "\n")
                 #       k.write(citystate+","+row["SERIES"]+","+row["SERIES NAME"]+","+row["FAMILY"]+","+row["OST"]+","+row["OST DESC"]+","+ str(lat) + "," + str(lng) + "\n")
                 #       k.write(row["DUTY STA"] + "," + row["LOCATION"] + "," + citystate + "," + row["VISN"] + "," + row["SERIES"] + "," + row["SERIES NAME"] + "," + row["FAMILY"] + "," + row["OST"] + "," + row["OST DESC"] + "," + row["PLAN"] + "," + row["GRADE"] + "," + row["ADMIN"] + "," + row["ADMIN2"] + "," + row["COST CENTER .ORG"] + "," + row["COST CENTER ORG DESCRIPTION"] + "," + row["COST CENTER"] + "," + row["COST CENTER DESCRIPTION"] + "," + row["DUTY BASIS"] + "," + row["SUPV"] + "," + row["TYPE APPT"] + "," + str(lat) + "," + str(lng)  + "\n")
                except:
                        print citystate
                        #ugh.write(row["DUTY STA"] + "," + row["LOCATION"] + "," + citystate + "," + row["VISN"] + "," + row["SERIES"] + "," + row["SERIES NAME"] + "," + row["FAMILY"] + "," + row["OST"] + "," + row["OST DESC"] + "," + row["PLAN"] + "," + row["GRADE"] + "," + row["ADMIN"] + "," + row["ADMIN2"] + "," + row["COST CENTER .ORG"] + "," + row["COST CENTER ORG DESCRIPTION"] + "," + row["COST CENTER"] + "," + row["COST CENTER DESCRIPTION"] + "," + row["DUTY BASIS"] + "," + row["SUPV"] + "," + row["TYPE APPT"] + "," + str(lat) + "," + str(lng)  + "\n")
                        ugh.write(citystate+";"+row["LOCATION"]+";"+row["CITY"]+";"+row["ST"]+";"+row["FAMILY"]+";"+row["OST"]+";"+row["OST DESC"]+";"+ "\n")
        #sys.exit()
                        
print "Done!"
