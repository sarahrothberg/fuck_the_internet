# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, session 
from flask import render_template
from twilio.util import TwilioCapability

import twilio.twiml
import os


app = Flask(__name__)


# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def mainFunction():	
	return render_template('main.html')

#below is the working one!!!
@app.route("/textRefresher", methods=['GET', 'POST'])
def textRefresher():
	message = client.messages.list(
		to = "+17472334999"
		)
	return message[0].body

# @app.route("/textRefresher", methods=['GET', 'POST'])
# def textRefresher():
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
# 	text = message[0].body
# 	textwords = text.split()
# 	for word in badwords:
# 		if word in textwords:
# 			post = "uh oh! someone said something shitty!"
# 		else:
# 			post = message[0].body
# 	return post


# @app.route("/textRefresher", methods=['GET', 'POST'])
# def textRefresher():
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	badwords = ['fuck', 'shit', 'cunt', 'cocksucker', 'asshole'];
# 	text = request.values.get('Body')
# 	textwords = text.split()
# 	for word in badwords:
# 		if word in textwords:
# 			post = message[1].body
# 		else:	 
# 			post = message[0].body
# 	return post

@app.route("/response", methods=['GET', 'POST'])
def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""
	# with open("./badwords.txt", 'r') as badwords:
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
	port = int(os.environ.get('PORT', 8090))
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)