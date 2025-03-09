from bs4 import BeautifulSoup
import requests
with open("weather.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

rows = soup.find_all("tr")[1:]
weather_data = []
temeprature = 0
for row in rows:
    columns = row.find_all('td')
    day_of_week = columns[0].text
    temperature = int(columns[1].text.replace("Â°C", ""))
    precipitation = columns[2].text

    weather_data.append([day_of_week, temperature, precipitation])

#1 Task exec
print(weather_data)

hottest_temp = weather_data[0][1]
hottest_day = weather_data[0][1]

for day, temp, condition in weather_data:

    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day
#2 Task exec
print(f"Hottest temp: {hottest_temp} on {hottest_day} ")

sunny_day = []
total_temp = 0
num_of_days = len(weather_data)
for day, temp, condition in weather_data:
    total_temp += temp
    if condition == "Sunny":
        sunny_day.append(day)
average_temp = total_temp / num_of_days
#3 Task 3 exec
print(sunny_day)
#4 Task 4 exec
print(f"Average: {average_temp}")



