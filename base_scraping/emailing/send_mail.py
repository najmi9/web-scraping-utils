import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

from ...env import MY_ADDRESS, PASSWORD

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main(name, email, template="message.html", files=[]):
    message_template = read_template(template)

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    
    msg = MIMEMultipart('alternative')       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['Date'] = formatdate(localtime=True)
    msg['To']=email
    msg['Subject']="I know how to send automatically emails to peoples !"
    # add in the message body
    msg.attach(MIMEText(message, 'html'))

    # add an attachment
    for path in files or []:
        if(Path(path).exists()):
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
            msg.attach(part)
        else:
            print('file', path, 'does not exist !')

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    