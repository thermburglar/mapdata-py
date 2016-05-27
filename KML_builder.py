import csv, os, cgi
filelist = os.listdir('c:\python\CSVs')
os.chdir('c:\python\CSVs')
for afile in filelist:
    kmlname = afile[0:len(afile)-4]
    with open(afile, 'rb') as f:
        reader = csv.DictReader(f)
        OSTDict = dict()
        ostname = dict()
        for row in reader:
            family = row["FAMILY"]
            if not OSTDict.has_key(row["OST"]):
                OSTDict[row["OST"]] = dict()
                ostname[row["OST"]] = row["OST_DESCRIPTION"]
            GradeDict = OSTDict[row["OST"]]
            if not GradeDict.has_key(row["GR"]):
                GradeDict[row["GR"]] = []
            joblist = GradeDict[row["GR"]]
            joblist.append(row)
    with open('c:\python\%s.kml'%(kmlname), 'w') as k:
        k.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>%s (%s)</name>
	<visibility>0</visibility>
	<open>1</open>"""%(kmlname, family))
        OSTs = OSTDict.keys()
        OSTs.sort()
        for OST in OSTs:
            GradeDict = OSTDict[OST]
            k.write("""<Folder>
		<name>%s (%s)</name>
		<visibility>0</visibility>"""%(cgi.escape(ostname[OST]),OST))
            grades = GradeDict.keys()
            grades.sort()
            for grade in grades:
                joblist = GradeDict[grade]
                jobnum = len(joblist)
                jobtext = str(jobnum)+" Job Incumbents"
                if jobnum == 1:
                    jobtext = "1 Job Incumbent"
                k.write("""<Folder>
		<name>Grade %s (%s)</name>
		<description>%s</description>
		<visibility>0</visibility>"""%(grade,OST,cgi.escape(jobtext)))
                for row in joblist:
                    k.write("""<Placemark>
				<visibility>0</visibility>
				<description><![CDATA[<br><br><br>
    <table border="1" padding="0">
    <tr><td>Station</td><td>%s</td></tr>
    <tr><td>Location</td><td>%s</td></tr>
    <tr><td>Org_CC</td><td>%s</td></tr>
    <tr><td>Org_CC_Description</td><td>%s</td></tr>
    <tr><td>OST</td><td>%s</td></tr>
    <tr><td>Title</td><td>%s</td></tr>
    <tr><td>Series</td><td>%s</td></tr>
    <tr><td>Family</td><td>%s</td></tr>
    <tr><td>OST_Description</td><td>%s</td></tr>
    <tr><td>Grade</td><td>%s</td></tr>
    <tr><td>Pay_Plan</td><td>%s</td></tr>
    <tr><td>Type</td><td>%s</td></tr>]]></description>
				<Point>
					<extrude>1</extrude>
					<altitudeMode>relativeToGround</altitudeMode>
					<coordinates>%s,%s,0</coordinates>
				</Point>
			</Placemark>"""%(row["STATION"],row["LOCATION"],row["ORG_CC"],row["ORG_CC_DESCRIPTION"],
                                         row["OST"],row["TITLE"],row["SERIES"],row["FAMILY"],row["OST_DESCRIPTION"],
                                         row["GR"],row["PAY_PLAN"],row["TYPE_APPT"],row["Lon"],row["Lat"]))
                k.write("</Folder>")
            k.write("</Folder>")
        k.write("</Document></kml>")
            
