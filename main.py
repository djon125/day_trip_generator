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

def location_picker(random_location):
    location = ran.choice(location_for_trip)
    finalized = True
    while finalized:
        location_select = input(f'Let\'s plan your trip! Do you want to go to {location}? y/n: ')
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
    while finalized:
        restaurant_select = input(f'Next, what style of restaurant do you want? {restaurant}? y/n: ')
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
    while finalized:
        transport_select = input(f'Now, what form of transportation do you want to use? {transport}? y/n: ')
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
    while finalized:  
        entertainment_select = input(f'Finally, what form of entertainment do you want? {entertainment} y/n: ') 
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
    while finalized:
        location_select = input(f'Would you like to confirm your selecected location: {location} y/n: ')
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
    while finalized:
        restaurant_select = input(f'Would you like to confirm the restaurant style: {restaurant} y/n: ')
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
    while finalized:
        transport_select = input(f'Would you like to confirm your transportation method: {transport} y/n: ')
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
    while finalized:  
        entertainment_select = input(f'Would you like to confirm your entertainment: {entertainment} y/n: ') 
        if entertainment_select == 'n' or entertainment_select == 'no':
            entertainment = ran.choice(form_of_entertainment)
            print(f'No worries, pick again:')
            continue
        elif entertainment_select == 'y' or entertainment_select == 'yes':
            print('Great! Thanks for confirming! Let\'s see what you chose:')
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
print(f'You will enjoy a trip to {location_fin} where you will love a {restaurant_fin} meal, get there by {transport_fin} and be entertained by {entertainment_fin}! Have fun!')
