calories = {
    'apple': 52,
    'banana': 89,
    'choco': 546
}

print(calories['apple'] > calories['banana'])

print('apple' in calories.keys())
print(52 in calories.values())

for key, value in calories.items():
    print(key) if value > 500 else None

print("list" in {"list": [1, 2, 3], "set": {1, 2, 3}})

customers  = [("John", 240000),
              ("Alice", 120000),
              ("Ann", 1100000),
              ("Zach", 44000)]
whales = [x for x,y in customers if y > 1000000]
print(whales)
