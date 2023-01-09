import requests
import os
from pyfiglet import figlet_format

os.system('clear')

##########################
# MODIFY VALUES BELOW ONLY
##########################

ip_address = '10.6.0.50'
data = {
    'text': 'CHECK DISCORD!',
    'color': '88,101,242' #r,b,g
}

##########################


url = 'http://{}/api/show-text'.format(ip_address)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
print(figlet_format("SENDING...", font = "digital"))

requests.post(url, json=data, headers=headers)

os.system('clear')

os.system("python3 ~/pi-attention/weather/weather.py")