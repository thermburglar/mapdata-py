#!/usr/bin/python
import sys
from openpyxl.reader.excel import load_workbook

filename = '/Users/eri/Dropbox/VA HRIS Nov_2011 updtd 3_9_2012.xlsx'
csv_file = '/Users/eri/Dropbox/alljobsdata.csv'

def main():
    wb=load_workbook(filename)

    for sheet in wb.worksheets:
        csv_file='%s.csv' % sheet.title
        print 'Creating %s' % csv_file
        fd=open(csv_file, 'wt')
        for row in sheet.rows:
            values=[]
            for cell in row:
                value=cell.value
                if value is None:
                    value=''
                if not isinstance(value, unicode):
                    value=unicode(value)
                value=value.encode('utf8')
                values.append(value)
            fd.write('\t'.join(values))
            fd.write('\n')
        fd.close()

if __name__=='__main__':
    main()
