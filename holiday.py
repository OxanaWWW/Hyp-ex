def holidaycost(hotel_cost, plane_cost, car_rental):  # Calculate a user’s total holiday cost
    return hotel_cost + plane_cost + car_rental


def hotel_cost(num_nights):  # We indicate the cost of the night (the task does not ask to enter)
    return num_nights * 23  # Price (£)


def plane_cost(city_flight):
    if city_flight == "Berlin":  # We choose an example of a city ourselves
        price = 100  # Price (£)
    elif city_flight == "LA":
        price = 200  # Price (£)
    else:
        price = 130  # Price (£)
    return price


def car_rental(rent_days):  # The cost of renting a car is indicated
    return rent_days * 20  # Price (£)


num_nights = int(input("Enter the number of nights in the hotel:  "))
"""User enters the number of rental nights."""
city_flight = input("Enter the selected city:  ")
"""User enters the selected city."""
rent_days = int(input("Enter the number of rental days: "))
"""User enters the number of rental days."""

result_flight = plane_cost(city_flight)
result_hotel = hotel_cost(num_nights)
result_rent_days = car_rental(rent_days)
print(f'Price {holidaycost(result_hotel, result_flight, result_rent_days)} £')
'''
In the example we get the result:
Enter the number of nights in the hotel:  5
Enter the selected city:  Berlin
Enter the number of rental days: 4
Price 295 £
Enter the number of nights in the hotel:  4
Enter the selected city:  LA
Enter the number of rental days: 3
Price 352 £

'''