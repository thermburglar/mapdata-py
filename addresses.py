import csv, os, sys
from geopy import geocoders
afile = os.path.abspath('C:\\Cartography\\Contract\\2013\\Data\\VAFacilities\\getaddress_20130410.csv')
mapReader = csv.DictReader(open(afile, 'rb'), delimiter = ',', quotechar = '"')
outfile = os.path.abspath('C:\\Cartography\\Contract\\2013\\Data\\VAFacilities\\getaddress_20130410_out.csv')
k = csv.writer(open(outfile, 'wb'), delimiter = ',', quotechar = '"')
k.writerow(["Index","Facility","troubleshoot","PlaceResult","Lat","Lon","ResultCode"])
for row in mapReader:
    s = row["PhysicalAddress"]
    s = s.replace('\xa0','')
    print row["Index"] + " " + s
    rcode = "1"
    try:
        g = geocoders.Google()
        place, (lat,lng) = g.geocode(s)
        place = place.encode('ascii', 'replace')
    except:
        place = "error"
        rcode = "2"
    k.writerow([row["Index"],row["PhysicalAddress"],s,place,lat,lng,rcode])
    place = ""


