#!/usr/bin/py

import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XDMQc60lGis")
soupObj1 = BeautifulSoup(page.content, 'html.parser')

seven_day = soupObj1.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="temp").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img")
desc = img['title']

#print(desc)  # Weather Data broken down to small chunks Above 
             # Redirection in code results, small datums to full on data dump
             # Weather Data mined and shown all at once below
#print("\n")
#print("\n")
#print("\n")

#tombstoneContainer = seven_day.find(class_="tombstone-container")
#period_tags = tombstoneContainer.find_all(class_="period-name")
#print(period_tags[0].select("br"))

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#print(short_descs)
#print(temps)
#print(descs)

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs,

    })
print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')

print(temp_nums)
print("\n")
print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("low") # Select the rows that happen at night
weather["is_night"] = is_night

print("\n")
print(is_night)
print("\n")


