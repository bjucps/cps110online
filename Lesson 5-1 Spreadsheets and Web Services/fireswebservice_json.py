# Dependencies:
#   pip install requests

# Hartford Fire Incidents API: https://dev.socrata.com/foundry/data.hartford.gov/824e-9vse

# Run this program with a zip code command line argument:
#  python fireswebservice_json.py 06106


import requests
import sys

query = ''
if len(sys.argv) == 2:
    query = '?zip=' + sys.argv[1]

url = 'https://data.hartford.gov/resource/824e-9vse.json' + query

response = requests.get(url)

if response.status_code != 200:
    print('Problem downloading results')
    exit()

records = response.json()

for rec in records:
    print(rec.get('street'), rec.get('station'))

    