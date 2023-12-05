import requests
import json
import re
import os
from urllib.request import urlopen
import time

name = input("What is your first name? ")

agify_api = f"https://api.agify.io/?name={name}"
agify_response = requests.get(agify_api)
agify_response_json = agify_response.json()

with open('my_agify_info.json', 'w', encoding ='utf8') as json_file:
    json.dump(agify_response_json, json_file, allow_nan=True)
    agify_file = open('my_agify_info.json', 'w')
    agify_file.close()

age = agify_response_json['age']

print(f'''Agify.io predicts your age based on your name.
They predict you are {age} years young!!!''')
time.sleep(5)
print()

whois_api = "http://ipwho.is/8.8.8.8"
whois_response = requests.get(whois_api)
whois_response_json = whois_response.json()
region = whois_response_json['region']
city = whois_response_json['city']
print(f'''According to ipwho.is Google's IP address 8.8.8.8
has a geolocation of {city}, {region}.''')
print()
time.sleep(5)
print("Now checking to see if you have the latest version of Terraform downloaded.")

tf_url = 'https://releases.hashicorp.com/terraform/index.json'
tf_response = requests.get(tf_url)
data = tf_response.json()
versions = {k: v for k, v in data.items() if k == 'versions'}
builds = versions.get('versions')
build_keys = []
for key in builds.keys():
  build_keys.append(key)
pattern = r"(?:^[1-9]\.[1-9]\.[1-9]$)"
stable = []
for i in build_keys:
  match = re.search(pattern, i)
  if match:
    stable.append(i)
latest_version = stable[-1]

filename = f"terraform_{latest_version}_linux_amd64.zip"
latest_url = f"https://releases.hashicorp.com/terraform/{latest_version}/terraform_{latest_version}_linux_amd64.zip "
current_directory = os.getcwd()
file_list = os.listdir(current_directory)

if filename in file_list:
  print("You already have the latest Linux amd64 version of Terraform downloaded.")
else:
  with urlopen(latest_url) as file:
    content = file.read()
  with open(filename, 'wb') as download:
    print("Downloading the latest Linux amd64 version of Terraform to your current working directory.")
    download.write(content)
    print("Download Complete!")
time.sleep(5)
os.system('clear')
print("That's All Folks!")
