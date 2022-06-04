location_for_trip = ['Miami', 'London', 'Las Vegas', 'Prague', 'Paris', 'San Diego', 'Sydney', 'Seattle', 'Munich', 'San Francisco']
mode_of_transportation = ['Train', 'Metro', 'Car', 'Bus', 'Uber', 'Bike', 'Plane']
restaurant_list = ['American Style', 'Tapas Style', 'Spanish Style', 'Mexican Style', 'Middle Eastern Style', 'Pub Style', 'German Style', 'Indian Style', 'Mediterranean style', 'French Style'] 
form_of_entertainment = ['Concert', 'Play', 'Museum', 'Art Gallery', 'Bar', 'Park', 'Movie', 'Festival', 'Club', 'Sporting Event']

import random as ran
#random choice list generated using import random
random_location = ran.choice(location_for_trip)
random_transport = ran.choice(mode_of_transportation)
random_entertainment = ran.choice(form_of_entertainment)
random_restaurant = ran.choice(restaurant_list)

def location_picker(random_location):
    location = ran.choice(location_for_trip)
    finalized = True
    print('Let\'s plan your trip!  Do you want to go to:')
    while finalized:
        location_select = input(f'{location}? y/n: ')
        if location_select == 'n' or location_select =='no':
            location = ran.choice(location_for_trip)
            print('No worries, how about:')
            continue
        elif location_select == 'y' or location_select == 'yes':
            print('Great choice!')
            return location
        else:
            print('that is not a valid response, try again ')

def restaurant_picker(random_restaurant):
    restaurant = ran.choice(restaurant_list)
    finalized = True
    print(f'Next, what sytle of restaurant do you want:')
    while finalized:
        restaurant_select = input(f'{restaurant}? y/n: ')
        if restaurant_select == 'n' or restaurant_select == 'no':
            restaurant = ran.choice(restaurant_list)
            print('No worries, how about:')
            continue
        elif restaurant_select == 'y' or restaurant_select == 'yes':
            print('Awesome!')
            return restaurant
        else:
            print('that is not a valid response, try again ')
    
def transport_picker(random_transport):
    transport = ran.choice(mode_of_transportation)
    finalized = True
    print('Now, what form of transportation do you want to use:')
    while finalized:
        transport_select = input(f'{transport}? y/n: ')
        if transport_select == 'n' or transport_select == 'no':
            transport = ran.choice(mode_of_transportation)
            print(f'No worries, how about:')
            continue
        elif transport_select == 'y' or transport_select == 'yes':
            print('Another great choice!')
            return transport 
        else:
            print('that is not a valid response, try again ')

def entertainment_picker(random_entertainment):
    entertainment = ran.choice(form_of_entertainment)
    finalized = True
    print('Finally, what form of entertainment do you want:')
    while finalized:  
        entertainment_select = input(f'{entertainment}? y/n: ') 
        if entertainment_select == 'n' or entertainment_select == 'no':
            entertainment = ran.choice(form_of_entertainment)
            print(f'No worries, try this:')
            continue
        elif entertainment_select == 'y' or entertainment_select == 'yes':
            print('Great pick! Almost done! All we need to do is confirm your picks!')
            return entertainment 
        else:
            print('that is not a valid response, try again ')
def final_location_picker(random_location):
    location = confirmed_location
    finalized = True
    print('Would you like to confirm your selected location:')
    while finalized:
        location_select = input(f'{location} y/n: ')
        if location_select == 'n' or location_select =='no':
            location = ran.choice(location_for_trip)
            print('No worries, pick again:')
            continue
        elif location_select == 'y' or location_select == 'yes':
            print('Great choice!')
            return location
        else:
            print('that is not a valid response, try again ')

def final_restaurant_picker(random_restaurant):
    restaurant = confirmed_restaurant
    finalized = True
    print('Would you like to confirm the restaurant style:')
    while finalized:
        restaurant_select = input(f'{restaurant} y/n: ')
        if restaurant_select == 'n' or restaurant_select == 'no':
            restaurant = ran.choice(restaurant_list)
            print('No worries, pick again:')
            continue
        elif restaurant_select == 'y' or restaurant_select == 'yes':
            print('Awesome!')
            return restaurant
        else:
            print('that is not a valid response, try again ')

def final_transport_picker(random_transport):
    transport = confirmed_transportation
    finalized = True
    print('Would you like to confirm your transportation method:')
    while finalized:
        transport_select = input(f'{transport} y/n: ')
        if transport_select == 'n' or transport_select == 'no':
            transport = ran.choice(mode_of_transportation)
            print(f'No worries pick again:')
            continue
        elif transport_select == 'y' or transport_select == 'yes':
            print('Super!')
            return transport 
        else:
            print('that is not a valid response, try again ')

def final_entertainment_picker(random_entertainment):
    entertainment = confirmed_entertainment
    finalized = True
    print('Would you like to confirm your entertainment:')
    while finalized:  
        entertainment_select = input(f'{entertainment} y/n: ') 
        if entertainment_select == 'n' or entertainment_select == 'no':
            entertainment = ran.choice(form_of_entertainment)
            print(f'No worries, pick again:')
            continue
        elif entertainment_select == 'y' or entertainment_select == 'yes':
            print('Great! Thanks for confirming! Let\'s see the trip you chose:')
            return entertainment 
        else:
            print('that is not a valid response, try again ')

#calling my functions
confirmed_location = location_picker(random_location)
confirmed_restaurant = restaurant_picker(random_entertainment)
confirmed_transportation = transport_picker(random_transport)
confirmed_entertainment = entertainment_picker(random_entertainment)
                                                                 
#calling my confirmation functions
location_fin = final_location_picker(random_location)
restaurant_fin = final_restaurant_picker(random_restaurant)
transport_fin = final_transport_picker(random_transport)
entertainment_fin = final_entertainment_picker(random_entertainment)
# I put all 4 funciton calls down here and build a big print statment to display the entire trip to the user!
print(f'You will start your trip to {location_fin} where you will get there by {transport_fin}, eat a delicious {restaurant_fin} meal and enjoy entertainment at {entertainment_fin}! Have fun!')


#(5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!