# All the information about the items, and the value the user has given
items = {
    "bolletjes": {
        "price": 1.1,
        "amount": 0,
    },
    
    "hoorntje": {
        "price": 1.25,
        "amount": 0,
    },
    
    "bakje": {
        "price": 0.75,
        "amount": 0,
    },

    "total": 0
}


# All the prices for the toppings
topping_items = {
    "geen": 0,

    "slagroom": 0.5,

    "sprinkels": 0.3,

    "caramel saus": {
        "hoorntje": 0.6,
        "bakje": 0.9
    },

    "amount": 0,

    "total": 0
}


show_receipt = False # Variable if the receipt must be shown




print("Welkom bij Papi Gelato") # Welcomes the user



# Show the receipt to the user
def user_receipt(items):

    item_Options = list( items.keys() ) # Get all the keys of the items
    
    # Total price for the receipt, and change it to have always 2 decimals
    total = items['total'] + topping_items['total']
    total = f'{total:.2f}'

    # Total price for the toppings
    toppingTotal = topping_items['total']
    toppingTotal = f'{toppingTotal:.2f}'

    # Amount of different toppings
    toppingAmount = topping_items['amount']
    toppingAmount_str = str(toppingAmount)


    # Show the user the receipt
    print('---------["Papi Gelato"]---------') # Receipt head

    # Loop all the keys of the items ( except the total ) 
    for i in range( len(items) - 1):

        itemName = item_Options[i] # Get the name of the item

        # Amount of the item
        itemAmount = items[itemName]['amount']
        itemAmount_str = str(itemAmount)
        
        # Price per item
        itemPrice = items[itemName]['price']
        itemPrice_str = str(itemPrice)

        # Total price ( amount * price )
        totalPrice = itemAmount * itemPrice

        totalPrice_str = f'{totalPrice:.2f}' # Let the total always be 2 decimals
        
        # Print the calculation on the receipt ( if its > 0 )
        if totalPrice > 0:
            print(itemName + "     " + itemAmount_str + " * " + itemPrice_str +  " = €" + totalPrice_str)
    
    if topping_items['total'] > 0:
        print("Topping     " + toppingAmount_str + " + " + toppingTotal + " = €" + toppingTotal)


    # Show the total price under the items
    print('                             ---- +')
    print('Totaal                   = €' + total)




# Add the items to the receipt
def add_items(scoops, cone_choice, topping):
    
    if scoops >= 4:
        items['bakje']['amount'] += 1 # Add to the bakje

    else:
        items[cone_choice]['amount'] += 1 # Add to the cone or the bucket

    items['bolletjes']['amount'] += scoops # Add the amount of scoops

    # Add the price to the total price
    items['total'] += items[cone_choice]['price'] # Add the price of the cone
    items['total'] += items['bolletjes']['price'] * scoops # Add the price of the scoop(s)
    

    # Add the price of the topping to the total topping price
    
    if topping == "caramel saus":
        topping_items['total'] += topping_items[topping][cone_choice]
    
    else:
        topping_items['total'] += topping_items[topping]


    if topping != "geen":
        topping_items['amount'] += 1 # Add the amount of toppings chosen


    return items # Return the items




def receipt_option(scoops, cone_choice):
    
    scoops_str = str(scoops)
    
    while True:

        buy_more = input("Hier is uw " + cone_choice + " met " + scoops_str + " bolletje(s). Wilt u nog meer bestellen? (ja/nee): ").lower()


        if buy_more == "ja" or buy_more == "nee":

            if buy_more == "nee":
                print("Bedankt en tot ziens!")

            show_receipt = False if buy_more == "ja" else True  # Give a value to check if the user wants the receipt

            break # Go out of the loop

        else: 
            print("Sorry, dat snap ik niet...")

    return show_receipt # Return if the user wants the receipt 




def get_topping():

    options = "" # All the options the user can choose


    toppings = list( topping_items.keys() ) # All the toppingss

    topping_char = ["A", "B", "C", "D"] # First characters to choose form


    # Put all the options into the string
    for num in range( len(toppings) - 2):
        options += topping_char[num] + ") " + toppings[num].capitalize()

        if num < 2:
            options += ", "

        elif num == 2:
            options += " of "


    while True:
        question_str = "Wat voor topping wilt u: " + options + "?: " # Make a string for the input
        
        topping = input(question_str).upper()

        try:
            num = topping_char.index(topping) # Check if the user has given a correct character
            topping = toppings[num] # Get the topping

        except ValueError:
            print("Sorry dat snap ik niet...")

        else:
            break # Break the loop


    return topping # Return the topping the user has chosen



# Ask the user where he wants his cone in
def get_coneChoice(scoops):

    scoop_str = str(scoops)
    
    question_str = "Wilt u deze " + scoop_str +  " bolletje(s) in A) een hoorntje of B) een bakje?: "
    
    while True:

        coneChoice = input(question_str).lower()

        if coneChoice == "a" or coneChoice == "b":
            break # Go out of the loop

        else:
            print("Sorry dat snap ik niet...")


    coneChoice = "hoorntje" if coneChoice == "a" else "bakje" # Make the value the option the user has chosen 

    return coneChoice # Return the users choice if he wants a cone or a bucket



# Ask which flavour the user wants per scoop
def get_flavour(scoops):

    options = "" # All the options the user can choose
    scoop = 1 # Total flavours chosen
    flavour_char = [] # First character of the flavours array

    flavours = ["Aardbei", "Chocolade", "Munt", "Vanille"] # All the flavours


    # Add the first character of the flavours in an array
    for flavour in flavours:
        flavour_char.append(flavour[0])


    # Put all the options into the string
    for num, flavour in enumerate(flavours):
        options += flavour_char[num] + ") " + flavour 

        if num < 2:
            options += ", "

        elif num == 2:
            options += " of "


    # Loop through the question
    while scoop <= scoops:

        scoop_str = str(scoop)

        question_str = "Welke smaak wilt u voor bolletje nummer " + scoop_str + "? " + options + "?: "

        flavour = input(question_str).upper()

        try:
            flavour_char.index(flavour) # Check if the user has given a correct character

        except ValueError:
            print("Sorry dat snap ik niet...")


        else:
            scoop += 1 # Add 1 flavour to the total flavours chosen




# Ask the amount of scoops the user wants
def get_scoops():

    # Loop through the question
    while True:

        scoops = input("Hoeveel bolletjes wilt u? ") 

        try:
            scoops = int(scoops)

            if scoops > 0: 
                break # Go out of the loop

            elif scoops > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            else:
                print("Sorry dat snap ik niet...")

        except ValueError:
            print("Sorry dat snap ik niet...")


    if scoops >= 4:
        print("Dan krijgt u van mij een bakje met", scoops , "bolletjes")


    return scoops # Return the amount of scoops




# Loop all the questions ( if the user did not choose to see the receipt )
while not show_receipt:
    scoops = get_scoops() # Let the user choose the amount of scoops

    get_flavour(scoops) # Get the flavour per scoop


    if scoops < 4:
        cone_choice = get_coneChoice(scoops) # Question if the user wants a cone or a bucket 
    
    else:
        cone_choice = "bakje" # If the user has 4-8 scoops, it gets automatically a bakje


    topping = get_topping() # Ask for a topping

    show_receipt = receipt_option(scoops, cone_choice) # Ask the user if he want to buy more, or if he wants the receipt

    items = add_items(scoops, cone_choice, topping) # Add the items to the receipt

    if show_receipt:
        user_receipt(items) # Show the receipt to the user