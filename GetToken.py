import requests
from getpass import getpass
import base64
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

username = input('Please provide username: ')
password = getpass('please enter your password: ')

message = username + ":" + password
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

autho = "Basic " + base64_message

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': autho

}

response = requests.request("POST", url, headers=headers, data=payload)

jsonResponse = response.json()

accessToken = jsonResponse['Token']

print(accessToken)

runsitehealth = input('Ask for site health? Y to continue, else to cancel')

print(runsitehealth)

if runsitehealth != 'Y':
    exit()
    print('You shouldn\'t see this message')
else:
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site-health"

    payload={}
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': accessToken

    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
