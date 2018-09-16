
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# with open('./reports/report/Test_LoginTest_2018-09-02_15-11-05.html',encoding='utf-8') as f:
msg = MIMEMultipart()
msg.attach(MIMEText(' 邮件发送测试……', 'plain', 'utf-8'))
    
msg['Subject']="Report Html"
msg['From']='17081371097@163.com'
msg['To']='390021310@qq.com'

att = MIMEText(open('./reports/report/Test_LoginTest_2018-09-02_15-11-05.html').read(),'plain','utf-8')
att["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att["Content-Disposition"] = 'attachment; filename="test.html"'
msg.attach(att)

smtp = smtplib.SMTP_SSL('smtp.163.com',465)
smtp.login('17081371097@163.com','ABC123abc')
smtp.send_message(msg,"17081371097@163.com",'390021310@qq.com')
smtp.close()