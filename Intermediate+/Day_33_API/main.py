import requests
from sunrise_sunset import day_night
import datetime as dt
import smtplib
import time

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

my_pos_dict = day_night()

iss_location = response.json()

my_pos = my_pos_dict['my_location']

iss_pos = iss_location['iss_position']

lat_range = [round(my_pos['lat'] - 5, 4), round(my_pos['lat'] + 5, 4)]
lon_range = [round(my_pos['lon'] - 5, 4), round(my_pos['lon'] + 5, 4)]

sunrise = int(my_pos_dict['sunrise'])
sunset = int(my_pos_dict['sunset'])

today = dt.datetime.now()
this_hour = today.hour

my_mail = "udemy3296@gmail.com"
my_pass = "ptkk vpgr zyhf vihw "
success = f"See up your head now!!\nYour position is: {my_pos['lat'], my_pos['lon']}\n ISS position is: {iss_pos['latitude'], iss_pos['longitude']}"
# failure = f"This is to check if this works\nYour position is: {my_pos['lat'], my_pos['lon']}\n ISS position is: {iss_pos['latitude'], iss_pos['longitude']}"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=my_pass)

    if this_hour >= sunset or this_hour < sunrise:
        send_mail = True
        while send_mail:
            time.sleep(60)
            if (lat_range[0] <= float(iss_pos['latitude']) <= lat_range[1] and lon_range[0] <= float(iss_pos['longitude']) <= lon_range[1]):
                connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=f"Subject:ISS Overhead\n\n{success}")
            else:
                send_mail = False
    # else:
    #     send_fail = True
    #     while send_fail: 
    #         time.sleep(10)
    #         connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=f"Subject:ISS Overhead\n\n{failure}")
            # The above else statement is for debugging

