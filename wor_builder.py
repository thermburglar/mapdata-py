import csv, os, sys

# open csv file containing family names, and load into a list
familyFile = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\ClientData\\JanuaryMaps\\familyTable.csv')
reader = csv.reader(open(familyFile, "rb"), delimiter = ",", quotechar = '"')

familynames = []

for name in reader:
    familynames.append(''.join(name))

#print familynames
#sys.exit()

templateFile = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\Tools\\template.wor')
m = open(templateFile, 'r')
worStr = m.read()
for thisFamily in familynames:
    fileBase = thisFamily.replace(' ','')
    fileBase = fileBase.replace('/','')
    fileBase = fileBase.replace('&','')
    str = worStr %(thisFamily)
    worFile = os.path.abspath('C:\\Cartography\\Contract\\2012\\VAToolkit\\ClientData\\JanuaryMaps\\%s.wor' %(fileBase))
    with open(worFile, 'w') as worWriter:
        worWriter.write(str.replace("<filename>", fileBase))

print "Done!"
