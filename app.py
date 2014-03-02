# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
<<<<<<< HEAD
from flask import Flask, request, redirect, session 
from flask import render_template
=======
from flask import Flask, request, redirect, session
>>>>>>> e4d27b6ab03f383f21d35fd346372138eebd5c33
from twilio.util import TwilioCapability

import twilio.twiml
import os


<<<<<<< HEAD
=======
SECRET_KEY = 'a secret key'
>>>>>>> e4d27b6ab03f383f21d35fd346372138eebd5c33
app = Flask(__name__)


# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)

<<<<<<< HEAD

@app.route("/", methods=['GET', 'POST'])
def displayQuestion():
	message = client.messages.list(
		to = "+17472334999"
		)
	smsMessage = message[0].body
	return render_template ('main.html', smsMessage = smsMessage)

# @app.route("/textRefresher", methods=['GET', 'POST'])
# def textReferesher():
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	return message[0].body

# @app.route("/", methods=['GET', 'POST'])
# def storesMessages():
# 	# message = request.values.get('Body', None)
# 	message = client.messages.list(
# 		to = "+17472334999"
# 		)
# 	return message[0].body
=======
message = client.messages.list(
	 to= "+17472334999"
)

@app.route("/", methods=['GET', 'POST'])
def displayQuestion():
	resp = twilio.twiml.Response()
    return message[0].body
>>>>>>> e4d27b6ab03f383f21d35fd346372138eebd5c33

@app.route("/response", methods=['GET', 'POST'])
def fromTheInternet():
	"""Respond to incoming calls with a simple text message."""
<<<<<<< HEAD
	resp = twilio.twiml.Response()
	resp.message("THANKS FOR UR QUESTION. FROM, THE INTERNET")
	return str(resp)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8090))
=======
    resp = twilio.twiml.Response()
    resp.message("THANKS FOR UR QUESTION. FROM, THE INTERNET")
    return str(resp)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
>>>>>>> e4d27b6ab03f383f21d35fd346372138eebd5c33
	app.run(host = '0.0.0.0', port=port)
	app.run(debug=True)