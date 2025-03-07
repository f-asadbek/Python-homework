import requests

api_key = "5fe23939ff48d0e9fa6ff98d6d95d8ee"
url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}"
response = requests.get(url)
print(response.json())