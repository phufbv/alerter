import requests
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
 
URL = 'http://courses.project.samueltaylor.org/'
COURSE_NUM_NDX = 0
SEATS_NDX = 1
 
def get_open_seats():
    r = requests.get(URL)
#    soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.text)
    courses = {}

#    for row in soup.find_all('tr'):
    for row in soup.findAll('tr'):
#        cols = [e.text for e in row.find_all('td')]
        cols = [e.text for e in row.findAll('td')]
        if cols:
            courses[cols[COURSE_NUM_NDX]] = int(cols[SEATS_NDX])
    return courses
