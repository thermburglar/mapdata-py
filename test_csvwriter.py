
import csv, os, sys
from geopy import geocoders

typofile = os.path.abspath('C:\\Cartography\\Contract\\2012\\Phase3\\Data\\typos.csv')
typoreader = csv.DictReader(open(typofile, 'rb'), delimiter = ',', quotechar = '"') 
typoDict = dict()
for row in typoreader:
        typoName = row["Name"].strip().upper()
        typoNewName = row["NewName"].strip().upper()
        typoDict[typoName] = typoNewName
delimiter = ','
quote = '\"'
typotest = os.path.abspath('C:\\Cartography\\Contract\\2012\\Phase3\\Data\\typos_test.csv')
out_f = open(typotest, 'w')
for key, value in typoDict.iteritems():
    print key + " " + value
    out_f.write("%s%s%s%s%s%s%s%s" %(quote, key, quote, delimiter, quote, value, quote, '\n'))
