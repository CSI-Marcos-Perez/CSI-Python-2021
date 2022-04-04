import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Yks9mijMJEZ")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id = "seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")

tonight = forecast_items[1]
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
print(period)
short_desc = tonight.find(class_="short-desc").get_text()
print(short_desc)
temp = tonight.find(class_="temp temp-low").get_text()
print(temp)