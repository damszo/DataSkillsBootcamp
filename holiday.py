# Defining a function to calculate the cost of a flight based on the destination.

def plane_cost(city):
    if city_flight == "Rome":
        return 200
    elif city_flight == "Warsaw":
        return 150
    elif city_flight == "Paris":
        return 140
    else:
        return "Invalid city"
    
# Defining a function to calculate the cost of a hotel based on the number of nights.

def hotel_cost(num_nights):
    hotel_price_per_night = 80
    total_hotel_cost = num_nights * hotel_price_per_night
    return total_hotel_cost

# Defining a function to calculate the cost of a car rental based on the number of days.

def car_rental(rental_days):
    daily_car_rental_cost = 40
    total_car_rental_cost = rental_days * daily_car_rental_cost
    return total_car_rental_cost

# Defining a function to calculate the total cost of a holiday.

def holiday_cost(plane_cost, hotel_cost, car_rental):
    total_plane_cost = plane_cost(city_flight)
    total_hotel_cost = hotel_cost(num_nights)
    total_car_rental = car_rental(rental_days)
    total_cost_holidays = total_plane_cost + total_hotel_cost + total_car_rental
    return total_cost_holidays

# Getting user input for the destination city, number of hotel nights, and number of car rental days.

city_flight = input("Which city would you like to fly to? Rome, Warsaw or Paris? ")
num_nights = int(input("How many nights will you be staying? "))
rental_days = int(input("How many days will you be hiring a car for? "))

# Printing out all the details about the holiday in a readable way.

print("Your holiday cost breakdown: ")
print("- Flight cost £:", plane_cost(city_flight))
print("- Hotel cost £:", hotel_cost(num_nights))
print("- Car rental cost £:", car_rental(rental_days))
print(f"Total cost of your holidays will be £:", holiday_cost(plane_cost, hotel_cost, car_rental))