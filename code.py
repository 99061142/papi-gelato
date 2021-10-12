print("Welkom bij Papi Gelato") # Welcomes the user


def user_receipt(items):
    
    # Show the user the receipt
    print(
        '---------["Papi Gelato"]---------'
        '\n'
    )





def add_items(scoops, cone_choice):
    
    items = "test"
    
    return items # Return the item array




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

            if scoops < 0: 
                print("Sorry dat snap ik niet...")

            elif scoops > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            else: 
                break # Go out of the loop

        except ValueError:
            print("Sorry dat snap ik niet...")


    if scoops >= 4:
        print("Dan krijgt u van mij een bakje met", scoops , "bolletjes")


    return scoops # Return the amount of scoops




show_receipt = False # Variable if the receipt must be shown


# Loop all the questions ( if the user did not choose to see the receipt )
while not show_receipt:
    scoops = get_scoops() # Let the user choose the amount of scoops

    get_flavour(scoops) # Get the flavour per scoop

    if scoops < 4:
        cone_choice = get_coneChoice(scoops) # Question if the user wants a cone or a bucket 

    show_receipt = receipt_option(scoops, cone_choice) # Ask the user if he want to buy more, or if he wants the receipt

    items = add_items(scoops, cone_choice) # Add the items to the receipt

    if show_receipt:
        user_receipt(items) # Show the receipt to the usuer