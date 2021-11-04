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
    self.tokens = [] 
    self.read_tokens()
    print(self.tokens)
        

  def read_tokens(self):
    ref = db.reference('/mobile_devices')
    devices = ref.get()
    for key, value in devices.items():
      logging.info('Found device: %s', key)
      self.tokens.append(value.get('token'))

  def write_to_database(self):
    ref = db.reference('/')
    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") 
    ref.child('bilge').child('event').push(
      {'timestamp': timestamp,
       'bilge_event': 3})

  def send_notification(self, title, body):
      message = messaging.MulticastMessage(
         notification=messaging.Notification(
                 title=title,
                 body=body,
                 ),
          tokens=self.tokens,

      )
      # Send a message to the device corresponding to the provided
      # registration token.
      response = messaging.send_multicast(message)
      # Response is a message ID string.
      logging.info('Successfully sent message: %s', response)


  def send_message(self):
      message = messaging.MulticastMessage(
         data={
              'score': '850',
              'time': '2:45',
          },
          tokens=self.tokens,
      )
      # Send a message to the device corresponding to the provided
      # registration token.
      response = messaging.send_multicast(message)
      # Response is a message ID string.
      logging.info('Successfully sent message: %s', response)

