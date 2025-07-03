#apis
import requests


 
print("***RHYMING WORD GENERATOR*****")

endpoint = f"https://api.datamuse.com/words?ml=i%20am%20student"
 
response = requests.get(endpoint)
 
data = response.json()
 
if response.status_code == 200:
    for item in data:
        print(item.get('tags'))