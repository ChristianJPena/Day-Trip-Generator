import random

# ""
# DONE(5 points): As a developer, I want to make at least three commits with descriptive messages.

# DONE(5 points): As a developer, I want to store my destinations, restaurants, mode of transporation, and entertainments in their own seperate lists. STRING

# ex. "New York City", "San Francisco" atleast 4. no relation between the destinations, restaurants, etc. 

# DONE(5 points): As a user, I want a destination to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# DONE(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# DONE(15 points): As a user, I want to be able to randomly re-select a destianation, restaurant, mode of transportation a form of entertainment if I don't like one or more of those things.

# DONE(10 points): As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. 

# x = ['x', 'x', 'x', 'x', 'x', 'X']

destination = ['Tampa', 'Miami', 'Orlando', 'Ft. Myers', 'Tallahassee', 'Jacksonville', 'Gainesville']
restaurant = ['Gekkō', 'La Perrada', 'Berns Steakhouse', 'Mz.Chezious', 'Junior Colombia Burger', 'Los Chapos Tacos']
mode_of_transportation = ['Plane', 'Train', 'Car', 'Streetcar', 'Bicycle', 'Uber']
form_of_entertainment = ['Amalie Arena Concert', 'Romantic Picnic at Honeymoon Island', 'Museums in Downtown Tampa', 'Anna Maria Island Beach', 'Universal Studios', 'Wynwood']

print("")


def welcome_message():
    print("It's Labor Day weekend, do you have your plans set?")
    print("")
    print("No?! Dont worry! Our Day Trip Generator will rescue you!")
    print("Below, the generator will provide you with with a random Destination, Restaurant, Transportation, and Entertainment!")
    print("and you will also have the ability to change a plan if you dont like it!")
    print("")
    print("Let's Begin!")

print("")
welcome_message()

def day_trip_generator (random_des,random_mot,random_res,random_foe):
    print(f"Destination: {random_des}")
    print(f"Restaurant: {random_res}")
    print(f"Transportation: {random_mot}")
    print(f"Entertainment: {random_foe}")

print("")


def trip_confirmation():
    random_des = random.choice(destination)
    random_res = random.choice(restaurant)
    random_mot = random.choice(mode_of_transportation)
    random_foe = random.choice(form_of_entertainment)
    day_trip_generator(random_des,random_mot,random_res,random_foe)
    print("")
    user_choice = input("Do you approve of your Day Trip?: (y/n) ")
    if user_choice == 'y' or user_choice == 'Y':
        print("")
        print(f'Congrats! you will be heading to {random_des}, arriving by {random_mot} where you will eat at {random_res} and afterwards, enjoy {random_foe} for entertainment!')
        print("")
        print("Be Safe & Happy Travels!")
        print("")
        travel_approval = False
    elif user_choice == 'n'or user_choice == 'N':
        travel_approval = True
        while travel_approval == True:     
            print("")
            select_pop = input("Which Day Trip setting would you like to change? Enter 1 for a new destination, 2 for a new Restaurant, 3 for a new Transportaiton, 4 for a new Entertainment option, and 5 to confirm your choices: ")
            print("")

            if select_pop == '1':
                random_des = random.choice(destination)
                day_trip_generator(random_des,random_mot,random_res,random_foe)
            
            elif select_pop == '2':
                random_res = random.choice(restaurant)
                day_trip_generator(random_des,random_mot,random_res,random_foe)
        
            elif select_pop == '3':
                random_mot = random.choice(mode_of_transportation)
                day_trip_generator(random_des,random_mot,random_res,random_foe)

            elif select_pop == '4':
                random_foe = random.choice(form_of_entertainment)
                day_trip_generator(random_des,random_mot,random_res,random_foe)

            elif select_pop == '5':
                print(f'Congrats! you will be heading to {random_des}, arriving by {random_mot} where you will eat at {random_res} and afterwards, enjoy {random_foe} for entertainment!')
                print("")
                print("Be Safe & Happy Travels!")
                print("")
                travel_approval = False
        


trip_confirmation()





