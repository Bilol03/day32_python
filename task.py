##################### Extra Hard Starting Project ######################
import pandas as pd
from random import *
from smtplib import *
import datetime as dt

today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = 'madiyarovbilol78@gmail.com'
# sending_email = 'madiyarovbilol8@gmail.com'
sending_password = 'gfudwozzxngztill'

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")

birthday_dict = {(data['month'], data['day']): data for (index, data) in df.iterrows()}



if today_tuple in birthday_dict:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_day = birthday_dict[today_tuple]
    file = open(f"letter_templates/letter_{randint(1,3)}.txt", 'r')

    file = file.read()
# 4. Send the letter generated in step 3 to that person's email address.


    connection = SMTP("smtp.gmail.com")

    connection.starttls()

    connection.login(user=my_email, password=sending_password)

    connection.sendmail(from_addr=my_email, to_addrs=birthday_dict[today_tuple]["email"], msg=f"Subject: Happy birhtday \n\n Happy birhtday {file.replace('[NAME]', birthday_dict[today_tuple]['name'])}")
    connection.close()




