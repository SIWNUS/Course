import requests

def day_night():
    response1 = requests.get(url="http://ip-api.com/json")
    response1.raise_for_status()
    data1 = response1.json()

    parameters = {}
    parameters['lat'] = data1['lat']
    parameters['lng'] = data1['lon']
    parameters['time_format'] = 24

    response2 = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
    response2.raise_for_status()
    data2 = response2.json()

    sunrise = data2['results']['sunrise'].split(':')[0]
    sunset = data2['results']['sunset'].split(':')[0]

    return {'sunrise': sunrise, 'sunset': sunset, 'my_location': {'lat': data1['lat'], 'lon': data1['lon']}}

