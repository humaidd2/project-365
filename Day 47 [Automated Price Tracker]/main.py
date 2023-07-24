import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.jumia.com.ng/nivea-nourishing-cocoa-body-lotion-for-women-400ml-pack-of-2-104325936.html"
response = requests.get(url=url).text
soup = BeautifulSoup(response, "lxml")
sel = soup.select(selector="div div span", class_="-b -ltr -tal -fs24 -prxs")
price = ""
for i in sel:
    try:
        if i.getText().split()[0] == "₦":
            price = i.getText()
            break
    except:
        pass
price = int(price.split()[1].replace(",",""))
if price < 5000:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: The price of your item is on a discount, hurry up and purchase it. Like: {url}. Goodluck")
