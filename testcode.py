# Item information and prices
items = {
    "bolletjes": {
        "price": 0.95,
        "amount": 0,
    },

    "liter": {
        "price": 9.8,
        "amount": 0
    },

    "hoorntje": {
        "price": 1.25,
        "amount": 0,
    },

    "bakje": {
        "price":  0.75,
        "amount": 0,
    },
}


toppings = {
    "geen": {
        "price": 0,
        "amount": 0,
    },
    
    "slagroom": {
        "price":0.5,
        "amount": 0,
    },
    
    "sprinkels": {
        "price":0.3,
        "amount": 0,
    },

    "caramel_saus": {
        "hoorntje": {
            "price": 0.6,
            "amount": 0
        },

        "bakje": {
            "price": 0.9,
            "amount": 0
        }
    }
}


buy_more = True # If the user did not choose to see the receipt

error_message = "Sorry dat is geen optie die we aanbieden..."

print("Welkom bij Papi Gelato") # Welcomes the user


# Get the role of the user
def user_role():
    role_choosing = True # If the user must choose a role

    roles = ("particulier", "zakelijk") # All the options for the role
    
    question = "Bent u " # Start the question

    # Add the options to the question
    for num, value in enumerate(roles):
        num += 1
        question += str(num) + ") " + value

        # If it is the last role
        if num == ( len(roles) - 1):
            question += " of "
        
    else:
        question += "? " # Add if all the options are added

    # If the user does not have a valid answer
    while role_choosing:
        role_num = input(question) # Ask the question

        # Check if the number the user has chosen is a valid option
        try:
            role_num = int(role_num) - 1

            role = roles[role_num]
        
        # If the role has not been found
        except (ValueError, IndexError):
            print("Vul een geldig getal voor een optie in")

        # If the role has been found
        else:
            role_choosing = False
    
    # If the question is over
    else:
        return role # Return the role the user has

# Ask the user how many scoops / litre he / she need
def user_ice(role: str):
    ice_choosing = True

    while ice_choosing:

        # Make the question
        if role == "particulier":
            question = "Hoeveel bolletjes wilt u? "
        
        else:
            question = "Hoeveel liter wilt u? "

        amount = input(question) # Ask the question 

        try:
            val = int(amount) # Check if its a number without decimal
        

        except ValueError:
            print(error_message)

        else:
            if val > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            else:
                ice_choosing = False # Stop the question

    else:
        return val # Return the amount

def scoop_flavours(scoops: int):
    choosing_flavours = True # Check if all the scoops have gotten a flavour
    flavour_chosen = False # Check per scoop if the flavour is chosen

    flavours = ("Aardbei", "Chocolada", "Munt", "Vanille") # All the flavours the user can choose from
    flavours_first = [] # First letter of the flavour

    question = "Welke smaak wilt u voor bolletje nummer {}? " # The start of the question

    # Make the question which flavour the user wants
    for flavour in flavours:
        flavours_first.append( flavour[0] ) # Add the first character of the flavour to the flavours_first array
        
        question += flavour[0] + ") " + flavour 

        if flavour < flavours[-2]:
            question += ", " 
        
        elif flavour == flavours[-2]:
            question += " of "
    else:
        question += "? "


    # Ask per scoop which flavour the user wants
    while choosing_flavours:
        
        for scoop in range(scoops):
            
            flavour_chosen = False # If the scoop has a flavour 
            
            scoop += 1 
            
            while not flavour_chosen:
                scoop_flavour = input( question.format(scoop) ).upper() # Ask the question

                try: 
                    flavours_first.index(scoop_flavour) # Check if the flavour is a valid option

                except ValueError:
                    print(error_message)
                
                # If the flavour is a valid option
                else:
                    flavour_chosen = True 
        
        # If all the scoops has a flavour
        else:
            choosing_flavours  = False 

def cone_choosing(scoops: int):
    cone_chosen = False # If the user did choose where he wants his scoops in

    question = "Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje? ".format(scoops).lower() # Question where the user wants his scoops in

    while not cone_chosen:
        cone = input(question)

        if cone == "a" or cone == "b":
            cone = "hoorntje" if cone == "a" else "bakje"
            cone_chosen = True
        
        else:
            print(error_message)

    # If the user made a choice where he wants his scoops in
    else:
        return cone # Return the cone that is chosen

def add_topping():
    topping_choosing = True

    toppings = ("geen", "slagroom", "sprinkels", "caramel Saus") # All the topping options
    options_first_char = ("a", "b", "c", "d") # The characters to choose the topping

    question = "Wat voor topping wilt u: " # Begin of the quesiton

    # Make the question with all the topping options
    for num, topping in enumerate(toppings):
        question += options_first_char[num].upper() + ") " + topping

        if num < ( len(toppings ) -2):
            question += ", "

        elif num == ( len(toppings ) -2):
            question += " of "
    else:
        question += "? "
    

    while topping_choosing:
        topping_char = input(question).lower()

        
        try:
            index = options_first_char.index(topping_char)

            topping = toppings[index].lower() # Get the topping the user has chosen

        except ValueError:
            print(error_message)

        else:
            topping_choosing = False

    else:
        topping = topping.replace(" ", "_") # If the topping has a space, it gets changed to "_"
        return topping # Return the topping that is chosen



def end_page(role:str, ice:int, cone:str=None):
    
    receipt_choosing = True # If the user must make a choice
    buy_more = True # If the user must choose if he want to buy more, or want to see the receipt

    if role == "particulier":
        question = f"Hier is uw {cone} met {ice} bolletje(s). Wilt u nog meer bestellen? (Y/N) "
    else:
        question = f"Hier is uw {ice} liter(s) ijs. Wilt u nog meer bestellen? (Y/N) "

    while receipt_choosing:
        answer = input(question).lower()

        if answer == "j":
            buy_more = True
            receipt_choosing = False
        
        elif answer == "n":
            buy_more = False
            receipt_choosing = False

        else:
            print(error_message)

    else:
        return buy_more

"""
def add_items(ice: int, cone: str, topping: str):
    # Scoops
    items['bolletjes']['amount'] += ice
    
    items[cone]['amount'] += 1 # Cone amount
    
    # Topping amount
    if topping == "caramel_saus":
        toppings[topping][cone]['amount'] += 1 # Topping amount
    
    else:
        toppings[topping]['amount'] += 1 # Topping amount
"""



role = user_role() # Ask which role the user has

# If the user does not want to see the receipt
while buy_more:
    ice = user_ice(role) # Ask the user how many scoops / litre he / she wants


    flavour = scoop_flavours(ice) # Ask which flavour the user wants per scoop

    # If the user is a customer
    if role != "zakelijk":
        # Ask the user which cone he want ( if the user chose more than 4 it is automatically a 'bakje' )
        if ice < 4:
            cone = cone_choosing(ice)
        else:
            cone = "bakje"
            print(f"Dan krijgt u van mij een {cone} met {ice} bolletjes")

            topping = add_topping()
    

    buy_more = end_page(role, ice, cone) # Ask the user if he / she wants to buy more

    #add_items(ice, cone, topping) # Add the items the user bought

# If the user does not want to buy more ice
else:
    print("Bedankt en tot ziens!")
