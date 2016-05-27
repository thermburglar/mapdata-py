#!/usr/bin/env python
 
from feedparser import parse
from xml.dom import minidom
import csv,os
 
csvfile = 'C:\\Cartography\\Contract\\2013\\Data\\VAJobPostings\\jobs_02062013.csv'
url = "http://jobsearch.mycareeratva.va.gov/RSS.aspx?jbf574=VA*&fedemp=y&fedpub=y"
 
def main():
  header = False
  if not os.path.exists(csvfile):
    header = True
  feed = parse(url)
  writer = csv.writer(open(csvfile,'wb'),delimiter = '|')
  if header:
    writer.writerow(['title', 'published', 'link', 'description', 'agency', 'location', 'salary','closing_date','who_may_apply','pay_plan','appointment_term','job_status','vacancy_announcement_number','control_number'])
 
  for e in feed.entries:
    xml = """<job>%s</job>""" % e.summary.replace('&', '&amp;')
    try:
      nodes = minidom.parseString(xml)
    except :
      print xml
      raise
    nodes =  nodes.childNodes[0].childNodes
    description = nodes[1].firstChild.wholeText
    agency = nodes[3].firstChild.wholeText
    location = nodes[5].firstChild.wholeText
    salary = nodes[7].firstChild.wholeText
    closing_date = nodes[9].firstChild.wholeText
    who_may_apply = nodes[11].firstChild.wholeText
    pay_plan = nodes[13].firstChild.wholeText
    appointment_term = nodes[15].firstChild.wholeText
    job_status = nodes[17].firstChild.wholeText
    vacancy_announcement_number = nodes[19].firstChild.wholeText
    control_number = nodes[21].firstChild.wholeText
    writer.writerow([e.title, e.published, e.link, description, agency, location, salary, closing_date, who_may_apply, pay_plan, appointment_term, job_status, vacancy_announcement_number, control_number])
 
if __name__== "__main__":
  main()
