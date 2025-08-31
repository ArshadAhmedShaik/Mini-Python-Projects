import requests

api_key = f"--------API-KEY-HERE--------"
url = f"http://api.weatherapi.com/v1/current.json"
place = input("Enter city: ")
parameters = {
      "key": api_key,
      "q": place
}

r = requests.get(url, params = parameters)
data = r.json()

with open("fore_cast.txt", "w") as f:
     location = data.get("location", "N/A")
     current = data.get("current", "N/A")
     f.write(f"Location: {location.get("name", "N/A")}\n")
     f.write(f"Region: {location.get("region", "N/A")}\n")
     f.write(f"Country: {location.get("country", "N/A")}\n")
     f.write(f"-------------------------------------------\n")
     f.write(f"Temperature in Celcius: {current.get("temp_c", "N/A")}\n")
     f.write(f"Temperature in Farenheit: {current.get("temp_f", "N/A")}\n")
     f.write(f"-------------------------------------------\n")
     f.write(f"Condition:\n")
     f.write(f"{current.get("condition", "N/A").get("text", "N/A")}")

     
      


