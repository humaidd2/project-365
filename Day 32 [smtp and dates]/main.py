# import smtplib
#
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()  # secures the line ie encryption
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:Hello\n\nThis is the body of the message")

#
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
#
# """Creating a datetime object"""
# my_birthday = dt.datetime(2002, 2, 22)
# print(my_birthday)


import datetime as dt
import random

today = dt.datetime.now().weekday()

if today == 5:
    with open("quotes.txt") as q:
        quotes = q.readlines()
        message = random.choice(quotes)
        print(message)