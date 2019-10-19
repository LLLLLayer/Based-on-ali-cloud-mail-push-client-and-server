# -*- coding:utf-8 -*-
import smtplib
import email
import pymysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailFrom = ""

def sendEmailBatch(address, title, content):
    for to_email in address:
        EMAIL_FROM = 'layer@lllayer.top'  # 刚才配置的发信地址
        EMAIL_HOST_PASSWORD = "08110811yjYJ"  # 密码
        EMAIL_HOST, EMAIL_PORT = 'smtpdm.aliyun.com', 80
        # 自定义的回复地址
        replyto = EMAIL_FROM
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = '%s <%s>' % (EMAIL_FROM, EMAIL_FROM)
        msg['To'] = '%s <%s>' % ("client", to_email)

        msg['Reply-to'] = replyto
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()

        textplain = MIMEText('{}'.format(content), _subtype='plain', _charset='UTF-8')
        msg.attach(textplain)
        try:
            client = smtplib.SMTP()
            client.connect(EMAIL_HOST, EMAIL_PORT)
            client.set_debuglevel(0)
            client.login(EMAIL_FROM, EMAIL_HOST_PASSWORD)
            client.sendmail(EMAIL_FROM, [to_email], msg.as_string())
            client.quit()
            print("success:"+to_email)

            conn = pymysql.connect("awstest.cuo6db9gvsjw.us-east-1.rds.amazonaws.com",
                                   "admin",
                                   "12345678",
                                   "testDB")
            cursor = conn.cursor()
            sql = 'INSERT INTO Email VALUES(\''+emailFrom + '\',\''+ to_email + '\',\''+ title + '\')'
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()

        except:
            print("Send Error")

def sendEmail(to_email, title, content):
        EMAIL_FROM = 'layer@lllayer.top'  # 刚才配置的发信地址
        EMAIL_HOST_PASSWORD = "08110811yjYJ"  # 密码
        EMAIL_HOST, EMAIL_PORT = 'smtpdm.aliyun.com', 80
        # 自定义的回复地址
        replyto = EMAIL_FROM
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = '%s <%s>' % (EMAIL_FROM, EMAIL_FROM)
        msg['To'] = '%s <%s>' % ("client", to_email)

        msg['Reply-to'] = replyto
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()

        textplain = MIMEText('{}'.format(content), _subtype='plain', _charset='UTF-8')
        msg.attach(textplain)
        try:
            client = smtplib.SMTP()
            client.connect(EMAIL_HOST, EMAIL_PORT)
            client.set_debuglevel(0)
            client.login(EMAIL_FROM, EMAIL_HOST_PASSWORD)
            client.sendmail(EMAIL_FROM, [to_email], msg.as_string())
            client.quit()
            print("success:"+to_email)

        except:
            print("Send Error")



if __name__ == '__main__':
    sendEmailBatch({"17635366177@163.com","Layer@cug.edu.cn"}, "testSubject", "TestContent")