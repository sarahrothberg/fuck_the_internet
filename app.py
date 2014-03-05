# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, session 
from flask import render_template
from twilio.util import TwilioCapability

import twilio.twiml
import os


# import serial
# import time

# ser = serial.Serial('/dev/tty.usbmodem411', 9600)

textTime = "0"
lastTextTime = "0"


# alpha = {'a':'12', 'b':'2111', 'c':'2121', 'd':'211', 'e':'1', 'f':'1121', 'g':'221',
#          'h':'1111', 'i':'11', 'j':'1222', 'k':'212', 'l':'1211', 'm':'22', 'n':'21',
#          'o':'222', 'p':'1221', 'q':'2212', 'r':'121', 's':'111', 't':'2', 'u':'112',
#          'v':'1112', 'w':'122', 'x':'2112', 'y':'2122', 'z':'2211', '1':'12222',
#          '2':'11222', '3':'11122', '4':'11112', '5':'11111', '6':'21111', '7':'22111',
#          '8':'22211', '9':'22221', '0':'22222', ' ':' '}


app = Flask(__name__)

smsReceived = None
count = 0
account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)


# def on(duration):
# 	ser.write('1')
# 	ser.read()
# 	time.sleep(duration)
# 	ser.write('0')
# 	ser.read()


@app.route("/", methods=['GET', 'POST'])
def mainFunction():	
	return render_template('main.html')

def write_out():
	body = request.form['date_created'] # get SMS body
	for char in body:
		signals = alpha[char.lower()]
		for signal in signals:
			if signal == '1':
				on(0.2) # Send dot
			elif signal == '2':
				on(0.4) # Send dash
			time.sleep(.02)
	return '<Response></Response>'

@app.route("/ledOff", methods=['GET', 'POST'])
def test():
	ser.write("0")
	# smsReceived = True
	print "Low in LED OFF"
	return render_template('gif.html')

@app.route("/gifDisplay", methods=['GET', 'POST'])
def displayGif():
	return render_template('gif.html')


@app.route("/textRefresher", methods=['GET', 'POST'])
def textRefresher():
	message = client.messages.list(
		to = "+17472334999"
		)

	# with open(badwords.dat) as f:
    	# badwords = f.readlines()
# 
	badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
	text = message[0].body
	textwords = text.split()
	for word in badwords:
		if word in textwords:
			post = "UH OH! SOMEONE SAID @#!$"
		else:
			post = message[0].body
			# ser.write("1")
			# # smsReceived = True
	return post

@app.route("/response", methods=['GET', 'POST'])
def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""
	
	# with open(badwords.dat) as f:
 #    	badwords = f.readlines()

	badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
	text = request.values.get('Body')
	textwords = text.split()
	for word in badwords:
		if word in textwords:			
			msg = " UH OH, A$$FACE SAFESEARCH IS ON!"
		else:	 
			msg = " THANKS FOR UR QUESTION. <3, THE INTERNET"
	resp = twilio.twiml.Response()			
	resp.message(msg)
	return str(resp)

if __name__ == "__main__":

	# while True:
	# 	message = client.messages.list(
	# 		to = "+17472334999"
	# 		)

	# 	textTime = message[0].date_created

	# 	print "last text time= " + lastTextTime
	# 	print "current text time= " + textTime
		
	# 	if textTime != lastTextTime:
	# 		ser.write('1')
	# 		lastTextTime = textTime
	# 	else: 
	# 		ser.write('0')
			

	port = int(os.environ.get('PORT', 8000))
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)


	

