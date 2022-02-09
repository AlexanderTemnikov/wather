import requests
from bs4 import BeautifulSoup
import http.client
import json

s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
})


def load_user_data(month, city, session):
    url = 'https://world-weather.ru/archive/russia/' + city + '/' + month + '/'
    # print(url)
    request = session.get(url)
    return request.text


def get_weather(html, month):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find_all('td', class_='weather-temperature archive_c')
    value1 = quotes[0].text
    value2 = quotes[1].text
    sum = (int(value1) + int(value2)) / 2
    return sum


years = ['2012']
cities = ['tomsk']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

citiesOutput = {}

for city in cities:
    yearsOutput = {}

    for year in years:
        monthsOutput = {}
        for month in months:
            response = load_user_data(month, city, s)
            with open('./page_%s.html' % (month), 'w', encoding="utf-8") as output_file:
                # output_file.write(response)
                weather = get_weather(response, month)
                monthsOutput[month] = weather

        yearsOutput[year] = monthsOutput

    citiesOutput[city] = yearsOutput
print(citiesOutput)


conn = http.client.HTTPConnection('127.0.0.1', 8000)
headers = {'Content-type': 'application/json'}
json_data = json.dumps(citiesOutput)
conn.request('POST', '/weather_set/', json_data, headers)
response = conn.getresponse()
print(response.read().decode())


