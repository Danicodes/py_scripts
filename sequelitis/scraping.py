#! /usr/bin/env python

import sys, os, time, re
from datetime import datetime
import urllib, urllib2, json
from bs4 import BeautifulSoup
import csv
import pandas as pd

quote_page = "http://www.imdb.com/list/ls003495084/"
page = urllib2.urlopen(quote_page)
print type(page)
soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
name_box = soup.find(‘h1’, attrs={‘class’: ‘lister-list’})
name = name_box.text.strip() # strip() is used to remove starting and trailing

print name_box
# open a csv file with append, so old data will not be erased
#csv path
#with open(‘sequelitis_movie_list.csv’, ‘a’) as movies_csv_file:
# writer = movies_csv.writer(movies_csv_file)
# writer.writerow([name, price, datetime.now()])
