import requests 

query = input("Enter your query: ")
api="-------api-key----------"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-30&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)

data = r.json()
articles = data["articles"]

with open("news.txt", "w", encoding="utf-8") as f:
  i = 1
  f.write(f"Total articles fetched: {data['totalResults']}\n")
  for index,article in enumerate(articles):
      source = article["source"]
      name = source["name"]
      f.write("-------------------------------------------------\n")
      f.write(f"Article {index+1}:\n")
      f.write(f"Name : {name}\n")
      f.write(f"Author: {article['author']}\n")
      f.write(f"Title: {article['title']}\n")
      f.write(f"URL: {article['url']}\n")
      f.write("\n")
      f.write(f"{article['content']}\n")
      f.write("-------------------------------------------------")
      i += 1




