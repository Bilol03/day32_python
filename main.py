from smtplib import *
import datetime as dt
from random import *


my_email = 'madiyarovbilol78@gmail.com'
sending_email = 'madiyarovbilol8@gmail.com'
sending_password = 'gfudwozzxngztill'

connection = SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=sending_password)

today = dt.datetime.now()
file = open('quotes.txt', 'r')
quotas = file.readlines()
print(today.weekday())


quota = choice(quotas)
print(quota)
if today.weekday() == 6:
    connection.sendmail(from_addr=my_email, to_addrs=sending_email, msg=f"Subject: Motivation \n\n {quota}")
connection.close()















#
#
#
# connection.close()

# import datetime as dt
#
# today = dt.datetime.now()

# print(today)
