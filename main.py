import requests as rqs
from send_email import send_email

topic = "tesla"

api_key = "24d8cdad812f41e9b31a606c73f7f6db"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

try:
    response = rqs.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    content = response.json()

    articles = content.get("articles", [])[:20]
    body_lines = []

    for article in articles:
        body_lines.append(
            f"Title: {article.get('title', 'No Title')}\n"
            f"Description: {article.get('description', 'No Description')}\n"
            f"Url: {article.get('url', 'No URL')}\n"
        )
    
    body = "\n".join(body_lines)
    send_email(body)
    
except rqs.RequestException as e:
    print(f"An error occurred: {e}")
