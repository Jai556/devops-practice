#version = "1.0"
import json
import requests

# 1. READ THE CONFIGURATION
print("Reading config...")
with open("config.json", "r") as file:
    config = json.load(file)

api_url_to_call = config["api_url"]

# 2. CALL THE API
print("Calling API at: " + api_url_to_call)
response = requests.get(api_url_to_call)
joke_data = response.json()

# Format the data into a single sentence
log_message = "Joke fetched: " + joke_data["setup"] + " ... " + joke_data["punchline"] + "\n"

# 3. SAVE THE RESULT TO A LOG FILE
print("Saving to log file...")

# 'a' stands for 'append'. It adds to the end of the file instead of deleting what was there.
with open("system_log.txt", "a") as log_file:
    log_file.write(log_message)

print("Process complete! Check your folder for system_log.txt.")