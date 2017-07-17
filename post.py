#!/usr/bin/python

import smtplib
import urllib2,json
import requests
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


piir = 5

while True:

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("INSERT_EMAIL@gmail.com", "INSERT_TOKEN")

        sahver_t = requests.get('http://192.168.1.251/feed/value.json?id=96&apikey=INSERT_READ_API_KEY').json()
	
	sahver_t = float(sahver_t)

	print sahver_t

	if sahver_t < piir:
		fromaddr = "INSERT_EMAIL@gmail.com"
		toaddr = "RECIEVER_EMAIL"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "INSERT SUBJECT"
		body = "CHANGE " +str(sahver_t)+ " HOW NEEDED"
		msg.attach(MIMEText(body, 'plain'))
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()

	time.sleep(7200)