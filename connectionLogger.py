# Created in November 2017

# If your internet drops out regularly it can be handy to have evidence to show your ISP.  
# This python script will run every 30 seconds, try and connect to Google and if it 
# fails, it will add the date and time of the failure to a CSV file for proof.

# Latest source : https://github.com/therealrobster/Internet-Connection-CSV-Logger
# license : https://github.com/therealrobster/Internet-Connection-CSV-Logger/blob/master/LICENSE


import sys
import csv
import datetime
import socket
import time

REMOTE_SERVER = "www.google.com"

def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

while True:
  if is_connected() == False:
    data = [datetime.datetime.now().strftime("%y-%m-%d"), datetime.datetime.now().strftime("%H:%M"), "No connection"]
    out = csv.writer(open("connectoinLog.csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(data)
    print("writing CSV data")

  #rest for a bit, the forum isn't that busy
  restTime = 30  #300 is 5 minutes 
  minutes = restTime / 60
  print "Resting for " + str(minutes) + " minutes before trying again..."
  time.sleep(restTime)

