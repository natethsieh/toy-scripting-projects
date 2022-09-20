import smtplib 

from email.message import EmailMessage 
from string import Template 
from pathlib import Path 

html = Template(Path('index.html').read_text())

#print(html.substitute(name='Hello'))

email = EmailMessage()
email['from'] = 'nate dawgg'
email['to'] = 'nthsieh928@gmail.com'
email['subject'] = 'You have won $1,000,000'

try: 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
except: 
    print('Something went wrong')

