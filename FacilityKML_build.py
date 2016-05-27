import csv, os, cgi
kmlname = "VAFacilities"
afile = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\derived_data\\AllFacilities_v3.csv')
reader = csv.DictReader(open(afile, 'rb'), delimiter = ';', quotechar = '"')
TypeDict = dict()
for row in reader:
    if not row["Result Score"] == 4:
        if not TypeDict.has_key(row["SiteType"]):
            TypeDict[row["SiteType"]] = []
        sitetype = TypeDict[row["SiteType"]]
        sitetype.append(row)  
with open('C:\\Cartography\\Contract\\2012\\VAToolkit\\derived_data\\%s.kml'%(kmlname), 'w') as k:
    k.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>%s</name>
	<visibility>0</visibility>
	<open>1</open>"""%(kmlname))
    Types = TypeDict.keys()
    Types.sort()
    for Type in Types:
        joblist = TypeDict[Type]
        jobnum = len(joblist)
        jobtext = str(jobnum)+" Facilities"
        if jobnum == 1:
            jobtext = "1 Facility"
        k.write("""<Folder>
		<name>%s</name>
		<description>%s</description>
		<visibility>0</visibility>"""%(Type, cgi.escape(jobtext)))
        for row in joblist:
            k.write("""<Placemark>
            <name>%s</name>
    	    <visibility>0</visibility>
    	    <description><![CDATA[<br><br><br>
    <table border="1" padding="0">
    <tr><td>Facility Name</td><td>%s</td></tr>
    <tr><td>Address</td><td>%s</td></tr>
    <tr><td>Phone</td><td>%s</td></tr>]]></description>
			<Point>
				<extrude>1</extrude>
				<altitudeMode>relativeToGround</altitudeMode>
				<coordinates>%s,%s,0</coordinates>
			</Point>
		</Placemark>"""%(row["StationID"],row["Facility"],row["Address"],row["Phone"],row["Lon"],row["Lat"]))
        k.write("</Folder>")
    k.write("</Document></kml>")
            																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																			
