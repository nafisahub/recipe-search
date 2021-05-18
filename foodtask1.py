#import API

import requests

def recipe_search(ingredient):

# Register to get an APP ID and key https://developer.edamam.com/
    import os
    app_id = os.environ.get("APP_ID")
    app_key = os.environ.get("APP_KEY")
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

    data = result.json()
    return data['hits']

#The programme starts with the computer asking user questions. Use input for this.
name = input('What is your name?')
fave_food = input ('What is your favourite food?')
print ('Hello {} and welcome to Recipe search. I hope you are hungry and ready to make {} food today' .format(name, fave_food))


# Using Booleans to further understand what the user wants

#recipe_2 = input('Would you like to make a delicious meal today? y/n')
#yesPlease = recipe_2 == 'y'
#patience = input('Do you have the time and patience to make one of our recipes? y/n')
#IsPatient = patience == 'y'
#Use_site = recipe_2 and patience
#print ('You should go ahead and visit our site to make some delicious recipes:{}' .format(Use_site))
#Use If and If not for Booleans

visitSite = input('Would you like help making something delicious today (yes or no)?')
Wants_help = visitSite == 'yes'

patience = input('Do you have the patience to make something today (yes or no)')
hasPatience = patience == 'yes'

if visitSite and patience:
    print('Great, lets get started cooking something')

    if not visitSite and patience:
        print('This site might not be best for you. Budding Chefs only')


# If else statement to find out if they have enough ingredients

ingredient= int(input("how many ingredients do you have?"))

if ingredient >=  2:
    print("you can search for recipes")
else:
    print("you must have more than two ingredients to continue")


# Function to add the ingrdients

def list ():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['calories'])
        print()

list()


#Lists and Append

recipe_ideal = [

    "Mexican", "Thai", "Indian", "Chinese", "Nigerian", "Sri Lanken",
    ]
recipe_fave = input ('I hope you have enjoyed Recipe Search. Please add your fave type of cuisine to our list')

recipe_ideal.append(recipe_fave)


print(recipe_ideal)



#Alternative to the if else statement

#yield_1 = input ('Do you have more than one ingredient?')
#more_one = float(yield_1) <=  2.0

#print (' You have enough ingredients to make something delicious: {}' .format (more_one))