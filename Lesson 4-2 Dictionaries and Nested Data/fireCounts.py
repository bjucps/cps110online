import json

with open('fires.json') as jsonFile:
    jsonData = jsonFile.read()

records = json.loads(jsonData)


# Zip Code: Count
fireCounts = {}

for rec in records:
    zipCode = rec['zip']
    fireCounts[zipCode] = fireCounts.get(zipCode, 0) + 1

for zipCode in sorted(fireCounts):
    count = fireCounts[zipCode]
    print(f"{zipCode}: {count}")

