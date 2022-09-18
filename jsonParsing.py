import json

with open('mJson.json') as json_file:
    data= json.load(json_file)
    print(data['controller'][0])
    print(data['controller'][1])

    print("\nPrinting nested dicitonary as a key- value pair\n")
    for i in data['controller']:
        print("Name:", i['name'])
        print("Price:", i['price'])
        if  'error' in i:
            print("error msg:", i['error'])
