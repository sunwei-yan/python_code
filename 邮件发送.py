from http import server
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
msg=MIMEText("",'html','utf-8')
msg['From']=formataddr(["热搜助手","pythontest2481@126.com"])
msg['Subject']="微博热搜"
server = smtplib.SMTP_SSL('smtp.126.com')
server.login("pythontest2481@126.com","PHBGOLPROTJQXFHF")
server.sendmail("pythontest2481@126.com","543477641@qq.com",msg.as_string())
server.quit()