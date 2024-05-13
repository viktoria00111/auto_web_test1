import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "test.python.99@mail.ru"
toaddr = "test.python.99@mail.ru"
mypass = "4BYT2Atuoap$"
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test message from final lesson"
text = "GoodBye, fu**ing GB!"

msg.attach(MIMEText(text))

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = f'attachment; filename="{basename(reportname)}"'
    msg.attach(part)


server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()