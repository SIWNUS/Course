##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
import pandas as pd

my_mail = "udemy3296@gmail.com"
my_pass = "ptkk vpgr zyhf vihw"

# 1. Update the birthdays.csv
to_send = pd.read_csv('birthdays.csv')
send_list = to_send.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
for item in send_list:
    if item['month'] == today.month and item['day'] == today.day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_list = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
        with open(random.choice(letter_list)) as data:
            content = data.readlines()
            content[0] = content[0].replace('[NAME]', item['name'])
        with open('send_letter.txt', 'w') as send_data:
            send_data.writelines(content)
        with open('send_letter.txt') as tosend:
            letter = tosend.read()
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_pass)
            connection.sendmail(from_addr=my_mail, to_addrs=item['email'], msg=f"Subject:Happy Birthday to you, {item['name']}.\n\n{letter}")
