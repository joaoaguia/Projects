#Libraries
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import os
from datetime import date

def send_email_with_attach(rn_counter, directory, file_name):

    subject = ("Extração Concursos Publicos" + date.today().strftime(" %d-%m-%y"))
    body = ('''Boa tarde,

    Segue em anexo os concursos públicos abertos para o dia''' + date.today().strftime(" %d-%m-%y") + '''

    Existem ''' + str(rn_counter) +''' vagas que não requerem nacionalidade Portuguesa.

    Obrigado
    O melhor BOT do Mundo'''

    )
    
    #Open txt where sender_email and password of that email is stored
    expected_vars = {'sender_email':None, 'password':None}
    with open('D:/Particulares/Joao/Estudos/Programacao/GIT/Email_data.txt', 'r') as file:  
        exec(file.read(), expected_vars)

    receiver_email = "kama.florencio@gmail.com"
    bcc_email = "joaopedroaguiadasilva@gmail.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = expected_vars['sender_email']
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = bcc_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = os.path.join(directory, file_name)

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(expected_vars['sender_email'], expected_vars['password'])
        server.sendmail(expected_vars['sender_email'], [receiver_email, bcc_email], text)

 