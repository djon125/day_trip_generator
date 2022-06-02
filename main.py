location_for_trip = ['Miami', 'London', 'Las Vegas', 'Prague', 'Paris', 'San Diego', 'Sydney', 'Seattle', 'Munich', 'San Francisco']
mode_of_transportation = ['Train', 'Metro', 'Car', 'Bus', 'Uber', 'Bike']
restaurant_list = ['American Style', 'Tapas Style', 'Spanish Style', 'Mexican Style', 'Middle Eastern Style', 'Pub Style'] 
form_of_entertainment = ['Concert', 'Play', 'Museum', 'Art Gallery', 'Bar', 'Park']

import random as ran
#random choice list generated using import random
random_location = ran.choice(location_for_trip)
random_transport = ran.choice(mode_of_transportation)
random_entertainment = ran.choice(form_of_entertainment)
random_restaurant = ran.choice(restaurant_list)
