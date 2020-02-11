#!/usr/bin/env python2

import os
import requests
from bs4 import BeautifulSoup
from time import sleep

def sendmessage(title, message):
  os.system("osascript -e 'display notification \"" + message + "\"\'" + "'with title \"" + title + "\"\'")
  return

url = "http://static.cricinfo.com/rss/livescores.xml"

while True:
  r = requests.get(url)
  while r.status_code is not 200:
    r = requests.get(url)
  soup = BeautifulSoup(r.text)
  data = soup.find_all("description")
  score = data[2].text
  sendmessage("Score", score)
  sleep(10)
