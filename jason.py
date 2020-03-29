import json

# f = open("json.json", "x")
# f.close()

data = {"var1":"Ashish", "var2":"Kumar", "var3":52664, "var4": 987456321, 236:555}

with open("json.json", "w") as f:
    json.dump(data, f)

# with open("json.json", "w") as f:
#     x = json.dumps(data)
#     f.write(x)

with open("json.json", "r") as f:
    print(json.load(f))

# with open('json.json', 'r') as f:
#     print(json.loads(f.read()))
