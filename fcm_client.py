import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

class FCM_Client(object):

  def __init__(self, service_account_key):
    cred = credentials.Certificate(service_account_key)
    firebase_admin.initialize_app(cred)

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

