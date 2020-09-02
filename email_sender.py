import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = ' your name'
email['to'] = ' put your email here'
email['subject'] = 'Hello how are you, this is a automated email'

email.set_content(html.substitute({'name':'Name'}), 'html')
try:
    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('put your email here', '')
        smtp.send_message(email)
        print('all good boss! :)')
except:
    print("you need to put security of the email to OFF before use the script")
