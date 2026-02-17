import requests
import json
key="b791a8809d534dea88362500261702"
state=input("enter name of state:")
url=f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={state}&days=1&aqi=no&alerts=no"

data=requests.get(url)
load=json.loads(data.text)

# if "location" in data:
#     city = data["location"]["name"]
#     print(city)
# else:
#     print("API Error:", data)
print(load['location']['name'])
print(load["current"]['temp_c'])
for info in load["forecast"]["forecastday"]:
    print("weather forecast  :",info['day']["maxtemp_c"])