import datetime as dt
import random
import smtplib

import pandas

my_email = ''
my_password = ""

month = dt.datetime.now().month
day = dt.datetime.now().day
today = (month, day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

for b_month, b_day in birthday_dict:
    birth_date = (b_month, b_day)
    if birth_date == today:
        name = birthday_dict[birth_date]["name"]
        email = birthday_dict[birth_date]["email"]
        random_letter = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(random_letter, mode="w") as letter:
            letter = letter.read()
            updated_letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("mail.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=updated_letter)