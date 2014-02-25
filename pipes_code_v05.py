# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
from twilio.util import TwilioCapability

import twilio.twiml
import os

app = Flask(__name__)


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)
 

messages = client.messages.list(
	 to= "+17472334999"
)

@app.route("/", methods=['GET', 'POST'])
def displayQuestion():
    return messages[0].body

# @app.route("/response", methods=['GET', 'POST'])
# def fromTheInternet():
#     resp = twilio.twiml.Response()
#     resp.message("THANKS FOR UR QUESTION. <3, THE INTERNET")
#     return str(resp)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port=port)
	# app.run(debug=True)