f = open("map.txt", "r")

data = f.read()

x = 0
y = 0
entities = []
entity_graphics = "#.Z@"  # WHITE LIST

for c in data:

    if c in entity_graphics:  # WHITE LIST
        entities.append({'graphic': c, 'x': x, 'y': y})
    x += 1
    if c == "\n":
        x = 0  # CARRIAGE RETURN
        y += 1  # LINE FEED
print(entities)
print(len(entities))


# datum = True
# while datum:
#     datum = f.read(1)
#     num = ord(datum)  # get ascii value
#     print(num)
#     print(datum)
#
# entities = [
#     {"x": 0, "y": 0, "v": "@"},
#     {"x": 0, "y": 0, "v": "Z"},
#     {"x": 0, "y": 0, "v": "#"},
# ]
#
