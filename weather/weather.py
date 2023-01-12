import requests
import os
import sys
import time

while True:
    try:
        os.system('clear')
        print("") #Spacing for LCD Screen
        print("") #Spacing for LCD Screen
        print(requests.get('https://wttr.in/Tustin?0').text)
        time.sleep(60)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        restart()