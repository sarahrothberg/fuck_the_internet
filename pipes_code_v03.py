# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2f3087700e52df09a6bf868cd422d398"
auth_token  = "fe3eecfae2e9747c93c67dce12458853"
client = TwilioRestClient(account_sid, auth_token)
 

messages = client.messages.list(
	 to= "+17472334999"
)

print messages[0].body