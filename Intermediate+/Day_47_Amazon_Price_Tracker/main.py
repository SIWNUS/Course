from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv(".env")

my_mail = os.getenv("my_mail")
my_pass = os.getenv("my_pass")

url = "https://www.amazon.in/Instant-Pot-Duo-Mini-Programmable/dp/B00FLYWNYQ/ref=sr_1_1?crid=3FCHC3DMW2PC7&dib=eyJ2IjoiMSJ9.jBlIwI9-r3t2NCdtriybUyrC1_rbeYiOFa_DFYZlHFP19kfWfEqtodHP-umrLkg3gzpQWCH91mWpF3nShuMhJDpgCyBJVRtdj1r58H2pM99mBxN2UPWviZwFJsraUoqnKfEtqn3PIJoQN58f3vGNMAwDCg7DZx-O6vdzuNyDbQKPUbBvLJvdhp4IJ76Bd8fZJk7gQ8t4LKiRmzhhY5maZ6G5fDMIhu21Hukhs23840FkqfplXERtjEg7BHFLiL7Y2Km-ii2oIF2yXJ4JhEB6WrD5qq3AxtxbXtib3jyGRUg.V_BST0JUsJaYQfRcamePGDK5gb-WvIyCoaGuCJA4sAQ&dib_tag=se&keywords=Instant%2BPot%2BDuo%2BPlus%2B9-in-1%2BElectric%2BPressure%2BCooker%2C%2BSlow%2BCooker%2C%2BRice%2BCooker%2C%2BSteamer%2C%2BSaut%C3%A9%2C%2BYogurt%2BMaker%2C%2BWarmer%2B%26%2BSterilizer%2C%2BIncludes%2BApp%2BWith%2BOver%2B800%2BRecipes%2C%2BStainless%2BSteel%2C%2B3%2BQuart&nsdOptOutParam=true&qid=1730646852&sprefix=instant%2Bpot%2Bduo%2Bplus%2B9-in-1%2Belectric%2Bpressure%2Bcooker%2C%2Bslow%2Bcooker%2C%2Brice%2Bcooker%2C%2Bsteamer%2C%2Bsaut%C3%A9%2C%2Byogurt%2Bmaker%2C%2Bwarmer%2B%26%2Bsterilizer%2C%2Bincludes%2Bapp%2Bwith%2Bover%2B800%2Brecipes%2C%2Bstainless%2Bsteel%2C%2B3%2Bquart%2B%2Caps%2C239&sr=8-1&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
}

response = requests.get(url, headers=header)

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

item_name = soup.find(id = "productTitle").get_text().replace("/n", "").replace(",", ", ").replace("&", " & ")

with open("f.txt", "w") as fp:
    fp.write(item_name)

name = ""
with open("f.txt") as fp:
    title = fp.readlines()
    for item in title:
        name += item.strip()
        name += " "

target = 10000

cost = soup.select_one('.aok-offscreen:not([class*=" "])').get_text().strip()

price_amount = soup.find(name = "span", class_ = "a-price-whole").get_text().split(".")[0].strip()

value = price_amount.split(",")

price = ""
for num in value:
    price += num

if int(price) <= target:
    message = (f"Subject:Low Price Alert!!\n\n{name} is now {cost}. Buy it soon by clicking the link below:\n{url}").encode("utf-8")
    with SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(user=my_mail, password=my_pass)
        conn.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=message)
