#coding:utf-8
import os
import time
import numpy as np
import pandas as pd
import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header

def send_email(sender,password,content,time1,receiver):
    print(content)
    # sender = 'ZHONGDAchenqd6@163.com'#input('From: ')
    # password = 'xxx'#getpass.getpass('Password: ')密码就不给你们看了哈，你们自己手动输入！
    smtp_server = 'smtp.163.com'#input('SMTP server: ')
    # receivers = [receiver]
    
    message = MIMEText(content,'plain','utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('The month is bad ! Do you think so?','utf-8')
    
    time.sleep(time1 - time.time())
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(sender,password)
    server.sendmail(sender,receiver,message.as_string())
    print('邮件发送成功!')
    server.quit()
    
def get_list(filename):
    with open(filename,"r") as f:
        data = f.readlines()
    data = [i.strip().split(",") for i in data[1:]]
    return data
    
if __name__ == '__main__':
    filename = "email.csv"
    data = get_list(filename)
    for i in range(len(data)):
        theTime = time.strptime(data[i][1], "%Y/%m/%d %H:%M")
        timestamp = time.mktime(theTime)
        data[i][1] = timestamp
    df = pd.DataFrame(data,columns = ['name','time','email'])
    df.sort_values("time",inplace = True)
    print("Please input your 163 email!")
    sender = input()
    print("Please input your 163 email's password!")
    password = input()
    for i in df.values:
        send_email(sender,password,"Dear " + i[0] + " : Hello!",i[1],i[2])