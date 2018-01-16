#! /usr/bin/env python

import sys,os, time, datetime, re, webkit, threading, random
import urllib, urllib2, json
from bs4 import BeautifulSoup
import captcha_solver

show_tickets = ["http://www.lastweektickets.com/"] #List of websites to reserve from
num_guests = [1,2,3]
targetdate = datetime.datetime(2017, 1, 24, 17, 0)
epsilon = 3600 #seconds in an hour (discrepancy)
mintime = targetdate - epsilon
maxtime = targetdate + epsilon

sound_prompt = "vlc C:\Users\Dani\Music\Serial.mp3"
sound_interval = 5

contact_info = {"name":"Danielle Williams", "email": "danicodes94@gmail.com",
                "phone":6418880700, "zip":11434, "age":22}

timeout = 10

minperiod = 10
maxperiod = 30

assert mintime < targetdate
assert maxtime > targetdate

def makequery ():
    query_url = show_tickets[0]
    return query_url % 


