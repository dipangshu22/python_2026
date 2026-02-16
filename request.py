import requests
import json
query=input("enter your topic")
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-01-16&sortBy=publishedAt&apiKey=242ad85a3af04231993e7e51ae1269d9"
data=requests.get(url)
load=json.loads(data.text)
for topic in load["articles"]:
    print(topic["title"])
    print("description:>>>",topic["description"])
    print(".......................................")
