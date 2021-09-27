import os
from twilio.rest import Client

def send_message(text_message):
    twilio_sid = os.getEnv('TWILIO_SID')
    twilio_auth = os.getEnv('TWILIO_AUTH')
    twilio_number = os.getEnv('TWILIO_NUMBER')

    client = Client(twilio_sid, twilio_auth)

    text_from = twilio_number
    text_to = os.getEnv('GPUMONITOR_TEXT_TO')

    message = client.messages.create(body=text_message, from_=text_from, to=text_to)
