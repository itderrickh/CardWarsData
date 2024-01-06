import json
import os

def dothing(file, counter):
    f1 = open(file, "r")
    dataString = f1.read()
    f1.close()

    data = json.loads(dataString)

    for d in data:
        d["id"] = counter
        counter += 1

    f2 = open(file, "w")
    f2.write(json.dumps(data, indent=2))
    f2.close()
    return counter

c = 0
c = dothing("hero.json", c)
c = dothing("landscape.json", c)
c = dothing("creature.json", c)
c = dothing("spell.json", c)
c = dothing("building.json", c)