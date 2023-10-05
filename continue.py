i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        continue

cars = ["Ford",
        "GMC", 
        "Tesla",
        "Volkswagen",
        "Toyota"]

for car in cars:
    if car == "Tesla":
        continue
    print(car)

