def car_info(number_of_cars, cars):
    number_of_cars += 1
    cars.append("Toyota")
    return number_of_cars
    

number_of_cars = 3
cars = ["Audi", "BMW", "Ford"]

number_of_cars = car_info(number_of_cars, cars)

print(number_of_cars)
print(cars)

