import requests # This imports the package we just installed

print("Contacting the API...")

# We are sending a GET request to a public URL that returns a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# The API returns the data in JSON format (which looks exactly like our Python Dictionaries!)
joke_data = response.json()

# Let's print out the specific keys we want from the dictionary
print("Setup: " + joke_data["setup"])
print("Punchline: " + joke_data["punchline"])