import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACfd589b278ea443ffade9ba5037e60f2c'
auth_token = '9339b81227a21ce492fe5c3702cd5882'
client = Client(account_sid, auth_token)
def sendotp(phone,otp):
    if phone is None:
        return None
    try:
        message = client.messages \
                        .create(
                            body="this is veification from shopperscart your otp is "+str(otp),
                            from_='+13347218682',
                            to='+91'+str(phone)
                        )
        return True
    except Exception as e:
        print(e)
        return False
