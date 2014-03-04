# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, session 
from flask import render_template
from twilio.util import TwilioCapability

import twilio.twiml
import os


import serial
import time
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)


app = Flask(__name__)


account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def mainFunction():	
	return render_template('main.html')

def write_out():
    body = request.form['Body'] # get SMS body
    print body
    # for char in body:
    #     signals = alpha[char.lower()]
    #     for signal in signals:
    #         if signal == '1':
    #             on(0.2) # Send dot
    #         elif signal == '2':
    #             on(0.4) # Send dash
    #         time.sleep(0.2)

@app.route("/gifDisplay", methods=['GET', 'POST'])
def displayGif():
	return render_template('gif.html')

@app.route("/textRefresher", methods=['GET', 'POST'])
def textRefresher():
	message = client.messages.list(
		to = "+17472334999"
		)
	text_file = open("badwords.dat", "r")
	badwords = text_file.read().split()
	# badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
	text = message[0].body
	textwords = text.split()
	for word in badwords:
		if word in textwords:
			post = "UH OH! SOMEONE SAID @#!$"
		else:
			post = message[0].body
	return post

@app.route("/response", methods=['GET', 'POST'])
def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""
	text_file = open("badwords.dat", "r")
	badwords = text_file.read().split()
	# badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
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

def on(duration):
	ser.write('1')
	ser.read()
	time.sleep(duration)
	ser.write('0')
	ser.read()



if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8090))
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)