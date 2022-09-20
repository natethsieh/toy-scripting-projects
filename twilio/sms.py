import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['twilio_account_sid'] 
auth_token = os.environ['twilio_auth_token'] 

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+19193601648",
    from_="+18156579210",
    body="Hello there!"
)