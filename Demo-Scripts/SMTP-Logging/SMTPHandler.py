import ssl
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import logging
import datetime


def smtp_handler(name, toaddr, subject):
    CONTEXT = ssl.create_default_context()
    FILE = 'index.html'
    EMAIL = 'dummyemailtest8@gmail.com'
    PASSWORD = 'dummy_1234'
    if Path(FILE).exists():
        html = Template(Path(FILE).read_text())
    else:
        raise FileExistsError('File Not Found')
    email = EmailMessage()
    email['from'] = name
    email['to'] = toaddr
    email['subject'] = subject
    email.set_content(html.substitute(
        {
            'no': 1,
            'dspace': 20,
            'report_time': datetime.datetime.now()
        }),
        'html')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=CONTEXT)
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(email)
        logging.warning('Succesful')


if __name__ == '__main__':
    smtp_handler('Subhadeep', 'subhadeep762@gmail.com', 'Test')
