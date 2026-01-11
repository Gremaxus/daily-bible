import requests
import json

url = "https://rest.api.bible/v1/bibles?include-full-details=false"

headers = {'api-key': '-YOUR API KEY GOES HERE-'}

response = requests.request("GET", url, headers=headers)

req = requests.get(url)

#print(response.text)

if response.status_code == 200:
    data = response.json()
    json_data = json.dumps(data, indent=4) # NOT SURE IF THIS IS EVEN USEFUL?? DOESN'T WORK THE WAY INTENDED USING JSON_DATA, BUT USING DATA FOR JSON.DUMP DOES #
    with open("example_run.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)



print(data)

#TODO: Implement daily functions with some sort of randomizer and notification process

#TODO: Specify King James Version

#TODO: Simple GUI or some sort of GUI so it's not just a text box. Have set to run on startup of PC, have it be a persistent banner for desktop or something.

#TODO: Daily scripture sent to phone. Full chapter? Full book? Unsure yet, but this will help create consistency with study