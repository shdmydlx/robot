


import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




"""
Todo 
取到 report 目录最新生成的html文件
邮件发送此文件
"""

def send_mail(senderUser=None, senderUserpasswd=None, receivers=None, reportfilepath=None,attchFileName="test.html"):

    # with open('./reports/report/Test_LoginTest_2018-09-02_15-11-05.html',encoding='utf-8') as f:
    msg = MIMEMultipart()
    msg.attach(MIMEText(' 邮件发送测试……', 'plain', 'utf-8'))
        
    msg['Subject']="Report Html"
    msg['From']='17081371097@163.com'
    msg['To']='390021310@qq.com'
    reportfilepath='./reports/report/Test_LoginTest_2018-09-02_15-11-05.html'
    att = MIMEText(open(reportfilepath).read(),'plain','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="%s"'%(attchFileName)
    msg.attach(att)

    smtp = smtplib.SMTP_SSL('smtp.163.com',465)
    try:
        smtp.login('17081371097@163.com','ABC123abc')
        smtp.send_message(msg,"17081371097@163.com",'390021310@qq.com')
        smtp.close()
        print("发送邮件成功")
    except smtplib.SMTPException as e:
        print('发送邮件失败',e)
    

