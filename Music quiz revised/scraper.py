import json
import requests

# API endpoint
url = "https://spotify23.p.rapidapi.com/playlist/11TZ2XrVdUfnSY86nuZYy5?si=64fc0a83393c49ec"

# API key
headers = {
    'X-RapidAPI-Key': "bb1280d847mshbe866bad5c23d20p194029jsna188063b40ef",
    'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }

# Send GET request to API endpoint
response = requests.get(url, headers=headers)

# Load JSON data from API response
data = json.loads(response.text)

# Extract song names and artists from JSON data
songs = []
for item in data['tracks']['items']:
    song = item['track']['name']
    artist = item['track']['artists'][0]['name']
    songs.append([artist, song])

# Create a CSV file with songs and artists
import csv
with open("songs.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(songs)

print("CSV file created successfully.")
