
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(f"I have a {car['brand']} {car['model']} from {car['year']}")

car["year"] = 2020
print(f"Oops, it's actually from {car['year']}")

car["color"] = "red"
print(f"The car is {car['color']}")



birthdays = {"Alice": "Apr 1",
             "Bob": "Dec 12",
             "Carol": "Mar 4"}

for name, date in birthdays.items():
    print(f"{name} was born on {date}")

for name in birthdays:
    print(name)

if "Andreas" not in birthdays.keys():
    print("Andreas' birthday is not known :-(")


my_cars = [{"brand": "Ford", "model": "Mustang", "year": 1964},
           {"brand": "Tesla", "model": "Model S", "year": 2019},
           {"brand": "Volkswagen", "model": "Golf", "year": 2014}]

other_peoples_cars = {"Alice": ["Ford", "GMC"],
                      "Bob": ["Tesla", "Volkswagen"]}

other_peoples_cars["Alice"].append("Toyota")

