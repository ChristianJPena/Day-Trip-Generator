
import random

# ""
# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transporation, and entertainments in theri own seperate lists. STRING

# ex. "New York City", "San Francisco" atleast 4. no relation between the destinations, restaurants, etc. 

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destianation, restaurant, mode of transportation a form of entertainment if I don't like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. 

# x = ['x', 'x', 'x', 'x', 'x', 'X']

destination = ['Bali', 'Dominican Republic', 'Iceland', 'Italy', 'Colombia', 'New Zealand']
restaurant = ['Gekkō', 'Andy Tropical', 'MamaSushi', 'Genos Phillycheese steak', 'Olive Garden', 'Gekkō']
mode_of_transportation = ['plane', 'train', 'car', 'teleportation', 'bicycle', 'uber']
form_of_entertainment = ['Concert', 'Romantic Picnic', 'Museums', 'Beach', 'Theme Park', 'Spa']

random_des = random.choice(destination)
random_res = random.choice(restaurant)
random_mot = random.choice(mode_of_transportation)
random_foe = random.choice(form_of_entertainment)

print(random_des)
print(random_res)
print(random_mot)
print(random_foe)


