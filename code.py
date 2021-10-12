print("Welkom bij Papi Gelato") # Welcomes the user


def show_receipt(items):
    print(
        '---------["Papi Gelato"]---------'
        '\n'
    )





def add_items(scoops, cone_choice):
    items = "test"
    
    return items




def receipt_option(scoops, cone_choice):
    
    scoops_str = str(scoops)
    
    while True:

        buy_more = input("Hier is uw " + cone_choice + " met " + scoops_str + " bolletje(s). Wilt u nog meer bestellen? (Y/N): ").lower()


        if buy_more == "n":
            print("Bedankt en tot ziens!")
            
            return True
            
        if buy_more == "j" or buy_more == "n":
            break

        else: 
            print("Sorry, dat snap ik niet...")



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

    return coneChoice



def get_flavour(scoops):
    options = ""
    scoop = 1
    flavour_char = []

    flavours = ["Aardbei", "Chocolade", "Munt", "Vanille"] # All the flavours


    for flavour in flavours:
        flavour_char.append(flavour[0])


    for num, flavour in enumerate(flavours):
        options += flavour_char[num] + ") " + flavour 

        if num < 2:
            options += ", "
        
        elif num == 2:
            options += " of "
        

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
    while True:
        scoops = input("Hoeveel bolletjes wilt u? ") 

        try:
            scoops = int(scoops)

            if scoops < 0: 
                print("Sorry dat snap ik niet...")

            elif scoops > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            else: 
                break

        except ValueError:
            print("Sorry dat snap ik niet...")


    if scoops >= 4:
        print("Dan krijgt u van mij een bakje met", scoops , "bolletjes")


    return scoops




receipt = False


while not receipt:
    scoops = get_scoops() # Let the user choose the amount of scoops
    
    flavour_scoop = get_flavour(scoops) # Get the flavour per scoop

    if scoops < 4:
        cone_choice = get_coneChoice(scoops) # Question if the user wants a cone or a bucket 
    
    receipt = receipt_option(scoops, cone_choice) # Ask the user if he want to buy more, or if he wants the receipt

    items = add_items(scoops, cone_choice) # Add the items to the receipt

    if receipt:
        show_receipt(items) # Show the receipt to the usuer