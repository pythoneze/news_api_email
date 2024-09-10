import requests as rqs

api_key = "24d8cdad812f41e9b31a606c73f7f6db"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-10&sortBy=publishedAt&apiKey=24d8cdad812f41e9b31a606c73f7f6db"

request = rqs.get(url)
content = request.json()
for article in content["articles"]:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}")
    print("---")
