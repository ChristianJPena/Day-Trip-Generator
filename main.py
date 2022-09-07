
import random

# ""
# DONE(5 points): As a developer, I want to make at least three commits with descriptive messages.

# DONE(5 points): As a developer, I want to store my destinations, restaurants, mode of transporation, and entertainments in their own seperate lists. STRING

# ex. "New York City", "San Francisco" atleast 4. no relation between the destinations, restaurants, etc. 

# DONE(5 points): As a user, I want a destination to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destianation, restaurant, mode of transportation a form of entertainment if I don't like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. 

# x = ['x', 'x', 'x', 'x', 'x', 'X']

destination = ['Tampa', 'Miami', 'Orlando', 'Ft. Myers', 'Tallahassee', 'Jacksonville', 'Gainesville']
restaurant = ['Gekkō', 'La Perrada', 'Berns Steakhouse', 'Mz.Chezious', 'Junior Colombia Burger', 'Los Chapos Tacos']
mode_of_transportation = ['Plane', 'Train', 'Car', 'Streetcar', 'Bicycle', 'Uber']
form_of_entertainment = ['Amalie Arena Concert', 'Romantic Picnic at Honeymoon Island', 'Museums in Downtown Tampa', 'Anna Maria Island Beach', 'Universal Studios', 'Wynwood']

random_des = random.choice(destination)
random_res = random.choice(restaurant)
random_mot = random.choice(mode_of_transportation)
random_foe = random.choice(form_of_entertainment)

def day_trip_generator ():
    print(f"Destination: {random_des}")
    print(f"Restaurant: {random_res}")
    print(f"Transportation: {random_mot}")
    print(f"Entertainment: {random_foe}")

day_trip_generator()
travel_approval = input("Do you approve of your Day Trip?: (y/n) ")


while travel_approval == 'n':
    select_pop = input("Which Day Trip setting would you like to change? ")
    
    if select_pop == 'Destination':
        random_des = random.choice(destination)
        day_trip_generator()
    
    if select_pop == 'Restaurant':
        random_des = random.choice(restaurant)
        day_trip_generator()
 
    if select_pop == 'Transportation':
        random_des = random.choice(mode_of_transportation)
        day_trip_generator()

    if select_pop == 'Entertainment':
        random_des = random.choice(form_of_entertainment)
        day_trip_generator()
    
    travel_approval = input("Do you approve of your Day Trip?: (y/n) ")








