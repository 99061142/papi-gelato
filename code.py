print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.") # Welcomes the user


# Ask the user if he wants to buy more
def get_receipt(scoops, choice):

    # Loops the question
    while True:
        receiptChoise = input("Hier is uw " + choice + " met " + scoops + " bolletje(s). Wilt u nog meer bestellen? (Y/N) ").lower()


        if receiptChoise == "j" or receiptChoise == "n":
            break # Go out of the loop

        else:
            print("Sorry, dat snap ik niet...")

    if receiptChoise == "j":
        get_scoops() # Go back to the question for the scoops, if the user wants to buy more
    
    else:
        print("Bedankt en tot ziens!")




# Ask the user where he wants his cone in
def get_coneChoice(scoops):

    # Loops the question
    while True:

        coneChoice = input("Wilt u deze " + scoops  + " bolletje(s) in A) een hoorntje of B) een bakje? ").lower()

        if coneChoice == "a" or coneChoice == "b":
            break # Go out of the loop

        else:
            print("Sorry dat snap ik niet...")


    coneChoice = "hoorntje" if coneChoice == "a" else "bakje" # Make the value the option the user has chosen 

    receipt = get_receipt(scoops, coneChoice) # Receipt + ask if the user wants to buy more



def get_flavour(scoops):
    first_chars = ["a", "c", "m", "v"] # First character of the flavours

    flavours_chosen = 0

    while int(scoops) > flavours_chosen: 

        flavour = input("Welke smaak wilt u voor bolletje nummer {X}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ").lower()    


        try:
            first_chars.index(flavour) # Check if the user has given a correct character
        
        except:
            print("Sorry dat snap ik niet...")
                

        else:
            flavours_chosen += 1 # Add 1 flavour to the total flavours chosen

    get_coneChoice(scoops) # Question if the user wants a cone or a bucket




# Ask the amount of scoops the user wants
def get_scoops():

    # Loops the question
    while True:
        
        scoops = input("Hoeveel bolletjes wilt u? ") 

        try:
            val = int(scoops)


            if val > 0 and val <= 3:
                break # Go out of the loop
            
            elif value <= 8:
                print("“Dan krijgt u van mij een bakje met " + scoops +  " bolletjes”")
            
            elif val > 8:
                print("Sorry, zulke grote bakken hebben we niet")

            else:
                print("Sorry dat snap ik niet...")
        
        except:
            print("Sorry dat snap ik niet...")

    get_flavour(scoops) # Question which flavour the user wants


get_scoops() # Let the user choose the amount of scoops