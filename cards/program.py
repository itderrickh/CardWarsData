import json
 
f = open('hero.json')
data = json.load(f)
f.close()
 
for i in data:
    if "set" in i and i["set"] == "":
        print(i["name"])
    if "set" not in i:
        print(i["name"])
 
