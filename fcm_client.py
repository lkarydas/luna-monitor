import datetime
import logging
import firebase_admin

from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import db

class FCM_Client(object):

  def __init__(self, service_account_key, database_url):
    cred = credentials.Certificate(service_account_key)
    firebase_admin.initialize_app(cred,
                                  {'databaseURL': database_url})

  def write_to_database(self):
    ref = db.reference('/')
    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") 
    ref.child('bilge').child('event').push(
      {'timestamp': timestamp,
       'bilge_event': 3})

  def send_notification(self, device_token, title, body):
      message = messaging.Message(
         notification=messaging.Notification(
                 title=title,
                 body=body,
                 ),
          token=device_token,

      )
      # Send a message to the device corresponding to the provided
      # registration token.
      response = messaging.send(message)
      # Response is a message ID string.
      logging.info('Successfully sent message: %s', response)


  def send_message(self, device_token):
      message = messaging.Message(
         data={
              'score': '850',
              'time': '2:45',
          },
          token=device_token,
      )
      # Send a message to the device corresponding to the provided
      # registration token.
      response = messaging.send(message)
      # Response is a message ID string.
      logging.info('Successfully sent message: %s', response)

