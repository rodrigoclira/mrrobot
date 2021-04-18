#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path
import mimetypes
from sys import argv
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import argparse
import datetime


EMAILFROM = ""
USERNAME = ""
PASSWORD = ""


def send_email(subject, message, to, fileToSend):
    emailfrom = EMAILFROM
    emailto = to
    username = USERNAME
    password = PASSWORD
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = subject
    msg.preamble = subject
    
    if (message != ""):
        msg.attach(MIMEText(message))
        
    if (filename != ""):
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
    
        maintype, subtype = ctype.split("/", 1)
    
        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
    
        
        attachment.add_header("Content-Disposition", "attachment", filename=path.basename(fileToSend))
        msg.attach(attachment)

        
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto , msg.as_string())
    server.quit()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Script used to generate report of current tasks')
    # parser.add_argument("-s", dest="subject", help="TODO", required = False)
    # parser.add_argument("-A", dest="attach", help="TODO", required = False)
    # parser.add_argument("-d", dest="destination", help="TODO", required = True)
    # parser.add_argument('-m', dest= "msg", help="TOODO", required = True)
    # args = parser.parse_args()
    
    
    
    filename = "/home/rcls/FITec/scripts/LoginReport/mailpy.py"
    subject = "Testando"
    msg = "TESTE"
    recipient = ""
    recipient = ""
    
    send_email(subject, msg, recipient, filename)
    #for recipient in TOADDRS:
    #    send_email(args.subject, args.msg, recipient, filename)

