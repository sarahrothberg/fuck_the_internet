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

# @app.route("/", methods=['GET', 'POST'])
# def displayQuestion():
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	smsMessage = message[0].body
# 	return render_template ('main.html', smsMessage = smsMessage)

@app.route("/textRefresher", methods=['GET', 'POST'])
def textRefresher():
	message = client.messages.list(
		to = "+17472334999"
		)
	return message[0].body

# @app.route("/", methods=['GET', 'POST'])
# def storesMessages():
# 	# message = request.values.get('Body', None)
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	return message[0].body

@app.route("/response", methods=['GET', 'POST'])

# def checkForBadWords():
# 	# response = "THANKS FOR UR QUESTION. FROM, THE INTERNET"
# 	# message = client.messages.list(
# 	# 	to = "+17472334999"
# 	# 	)
# 	# badword = "Fuck"
# 	# text = message[0].body
# 	# textWords = text.split()
# 	# #if the text contains naughty words
# 	# if badWord in textWords:
# 	# 	response = "OH NO A$$FACE SAFESEARCH IS ON!"
# 	# else:
# 	# 	response = "THANKS FOR UR QUESTION. FROM, THE INTERNET"
# 	# fromTheInternet()
# 	# return 'words checked'

def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""
	text_file = open("badwords.txt", "r")
	words = text_file.read().split()
	words.append(badwords)
	text = request.values.get('Body')
	textWords = text.split()
	badwords = []
	for word in badwords:
		if word in textWords:
			msg = "OH NO A$$FACE SAFESEARCH IS ON!"
		else:
			msg = "THANKS FOR UR QUESTION. FROM, THE INTERNET"
	resp = twilio.twiml.Response()
	resp.message(msg)
	return str(resp)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8090))
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)