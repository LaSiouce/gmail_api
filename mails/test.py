from google_test import create_service
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import base64
import os

CLIENT_SECRET_FILE = '../credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = 'Coucou la famille, ce petit mail viens de ... ' + os.path.basename(__file__) + '!!'
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'tanguy.brousseau@gmail.com'
mimeMessage['subject'] = 'LES TT AUTOMATIQUES - FULL SPAM'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)