# This script creates a cross reference table showing station IDs for each OST in a city/state.  To be used to remove ambiguity from job postings data coming from USAJobs

# Written by Erin Comparri, 4/20/2012  erin.comparri at gmail com  for Federal Management Partners

import csv, os
afile = os.path.abspath('/Users/eri/Dropbox/cleaning/cleanjobsdata.csv')
outfile = os.path.abspath('/Users/eri/Dropbox/ostcrossref_full.csv')
reader = csv.DictReader(open(afile, 'rb'), delimiter = ',' , quotechar = '"') 

OSTDict = dict()
for row in reader:
	series = row["OST"].split('-')[0]
	test = row["CITY"].strip() + ',' + row["ST"]+','+ series +','+row["DUTY STA"]
	print test
	if not OSTDict.has_key(test):
		OSTDict[test] = []
	
outwt = open(outfile, 'w')

outwt.write ("\"City\",\"State\",\"Series\",\"StationID\"\n")

OSTs = OSTDict.keys()
OSTs.sort()
for row in OSTs:
	outwt.write (row+"\n")

