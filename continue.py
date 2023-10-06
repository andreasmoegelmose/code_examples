i = 0
while i < 10:
    if i == 5:
        continue
    print(i)
    i += 1

cars = ["Ford",
        "GMC", 
        "Tesla",
        "Volkswagen",
        "Toyota"]

for car in cars:
    if car == "Tesla":
        continue
    print(car)

