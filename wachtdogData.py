#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os
import datetime
import json
import requests
from datetime import date
import time
"""
1-Request last value data server
2-compare the last value with the current date
3-If last value > current date + 5 min
4-send email for admin
"""
r=requests.get('http://emoncms.org/feed/timevalue.json?id=1')
print r.status_code
if r.status_code == 200:
	print r.text
	json_data = json.loads(r.text)
	date1=int(json_data['time']) #check the key 
	print date1
	
	os.environ['TZ'] = 'Brazil/East'
	now = datetime.datetime.now()
	now1 = time.mktime(now.timetuple())
	print(now1)
	#print(now1.strftime('%Y-%m-%d %H:%M:%S'))
	timeInterval=(now1-date1)/60 # converte p/ minutos
	print timeInterval
	if timeInterval > 5:
		# credentials
		sender    = 'asdfgg@gmail.com'
		psw        = '123432'
		 
		# msg information
		addressee = 'xxxx@gmail.com'
		topic      = 'notification'
		text        = notification! )'
		 
		# msg
		msg = '\r\n'.join([
		  'From: %s' % sender,
		  'To: %s' % addressee,
		  'Subject: %s' % topic,
		  '',
		  '%s' % text
		  ])
		 
		# Sending email
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(sender,psw)
		server.sendmail(sender, addressee, msg)
		print "Send Email"
		server.quit()
	
	
