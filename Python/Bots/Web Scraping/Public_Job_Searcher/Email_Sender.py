#********************************************************
#Program:       Email_Sender
#Description:   This scrypt is resposible to send e-mails using a Gmail as a sender email, in order to run the scrypt, we need to provide the following parameters:
#               to, bcc, subject, text, attachment, sender_data - location of the txt file ('C:/xxxxxx/xxxx/xxxxxx.txt') that have the gmail account and password, 
#               the txt need to be configured as the following example:
#               sender_email = 'xxxxxx@gmail.com'
#               password = 'xxxxxxxxxxxxxxxx'
#********************************************************

#Libraries
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
import os

def send_email(to, bcc, subject, text, attachment, sender_data):
    log = ''
    #Open txt where the sender email and password is stored
    expected_vars = {'sender_email':None, 'password':None}
    with open(sender_data, 'r') as file:  
        exec(file.read(), expected_vars)
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = expected_vars['sender_email']
    message["To"] = to
    message["Subject"] = subject
    message["Bcc"] = bcc  # Recommended for mass emails
    # Add body to email
    message.attach(MIMEText(text, "plain"))

    if Path(attachment).is_file():
        # Open attachment file in binary mode
        with open(attachment, "rb") as attach:
            # Add file as application/octet-stream
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attach.read())
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        filename = os.path.basename(attachment)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        # Add attachment to message and convert message to string
        message.attach(part)
    else:
        log = (f"{filename} not found.")
        return log

    text = message.as_string()

    try:
        # Log in to server using secure context and send email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(expected_vars['sender_email'], expected_vars['password'])
        server.sendmail(expected_vars['sender_email'], [to, bcc], text)
        log = (f'Email sent to {to}')
    except smtplib.SMTPException as e:
        log = (f'An error occurred: {e}')
    finally:
        server.quit()
        return log