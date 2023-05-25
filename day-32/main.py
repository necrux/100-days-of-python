import smtplib
import datetime

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Happy Birthday\n\nHello")
    connection.close()

now = datetime.datetime.now()
now.year
print(now)