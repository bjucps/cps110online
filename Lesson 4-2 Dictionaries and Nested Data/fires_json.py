import json

with open('fires.json') as fireFile:
    fileData = fireFile.read()
    
records = json.loads(fileData)

for rec in records:
    print(rec['street'], rec['station'])

    