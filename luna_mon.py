from absl import app
from absl import flags

import logging
import logging.handlers

import fcm_client

FLAGS = flags.FLAGS
flags.DEFINE_string('service_account_key', None, 'The path to the service account key')
flags.DEFINE_string('log_file', 'fcm_logs.log', 'The path to the log file.')
flags.DEFINE_string('database_url', None, 'The URL to the FCM realtime database.')
flags.register_validator('service_account_key', lambda value: value,
                         message='Must pass a service account key.')
flags.mark_flag_as_required('service_account_key')
def main(argv):
  del argv  # Unused.
  logging.info('Hello world')
  # Setup logging.
  root_logger = logging.getLogger()
  del root_logger.handlers[:]
  root_logger.propagate = False
  formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)
  root_logger.addHandler(console_handler)
  file_handler = logging.handlers.RotatingFileHandler(FLAGS.log_file,
            maxBytes=(1024 * 1024 * 5),  # Max size for log files is 5MBs.
            backupCount=5)
  file_handler.setFormatter(formatter)
  root_logger.addHandler(file_handler)

  fcm = fcm_client.FCM_Client(FLAGS.service_account_key, FLAGS.database_url)
  fcm.send_notification('hello world', 'This a great notification that says'
                        'hello.')
  # fcm.send_message()
  # fcm.write_to_database()

if __name__ == "__main__":
  app.run(main)

