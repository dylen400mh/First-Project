print("Choose Your Adventure: Zombie Apocalypse") #title
print("========================================")
print()
print("The date is June 17, 2051. Today is the day that a zombie apocalypse") #intro
print("breaks out in the city of Toronto, Ontario.")
print("Unfortunately, you only have the option to bring your close family")
print("members along with you.")
print()

name = input("What is your name? ") #ask for name
print("Hey there,",name+". You better get ready because you don't have much time!")
print()
parent = False #rooms start out unsearched
out = False
kitch = False
bath = False
foy = False
living = False
hallway = False
brother = False
family = 0 #counter to break up of first loop when all family members are found
place = "bedroom" #starting location
guesses = 0 #counts how many guesses it takes to find family members
distance = 50 #the distance the zombies are from the house
win = False #variable for winning will remain false until game is won

def zombie():
    if distance == 0: #if zombies reach house, game over
        print()
        print("The zombies have arrived at your home. Unfortunately,")
        print("they take over and you are unable to survive.")
        print()
    else:
        print()
        print("The zombies are",distance,"metres away from your house!") #inform player how far away zombies are
        print("You must act quickly.")
        print()

def invalid(): #function for if an answer is invalid
    print("Invalid answer. Please try again.")
    print()
    
print("Before you stock up on supplies, you must find your family")
print("members first.")

while True: #first loop
    if place == 'bedroom': #bedroom
        zombie()
        print("Across from your bedroom is your parents' room,")
        print("down the hall to your right is your brother's room, and down")
        print("the hall to your left takes you to the main part of the house,")
        print("which consists of the kitchen, living room, bathroom, and foyer.")
        print()
        choice = input("Would you like to 1. Check your parents' bedroom 2. Check your brother's bedroom 3. Walk down the hall towards the main part of the house ")
        print()
        if choice == "1":
            place = "parentroom" #move to parent room
        elif choice == "2":
            place = "brotherroom" #move to brother room
        elif choice == "3":
            place = "hall" #move to hall
        else:
            invalid()

    elif place == "parentroom": #parent room
        if parent == False: #checks in parent's room if mother isn't found
            family += 1
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You walk into your parents' room and find your mother there,") #find mother
            print("but not your father.")
            print("You warn your mother about the emergency that was announced on")
            print("TV. It turns out she is completely oblivious to what is going on.")
            print()
            print("Mother: I cannot believe this is happening! I'll start packing essentials.")
            if family == 3: #escape clause if all family members are found
                break
            parent = True
        else:
            print("You have already found your mother in her room.")
        zombie()
        if distance == 0:
            break
        print("You continue to look around the house.")
        print()
        choice = input("Would you like to 1. Step outside on the patio 2. Walk down the hall towards the main part of the house 3. Check your brother's room ")
        print()
        if choice == "1":
            place = "outside" #move to outside
        elif choice == "2":
            place = "hall" #move to hall
        elif choice == "3":
            place = "brotherroom" #move to brother room
        else:
            invalid()

    elif place == "outside": #outside
        if out == False: #checks outside if father isn't found
            family += 1
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You step outside and see your father's head poking out from the ground.") #find father
            print("It is at that moment when you notice that he is standing")
            print("inside a bunker.")
            print()
            print("Father: Hey buddy. Do you like the bunker? I made it when")
            print("you were very young in case something like this ever")
            print("happened. What are you waiting for? We don't have")
            print("much time to waste.")
            if family == 3: #escape clause if all family members are found
                break
            print("After finding your father, you step back inside.")
            out = True
        else:
            print("You have already found your father outside.")
        zombie()
        if distance == 0:
            break
        print("You have the option to enter through your parents' room")
        print("or the kitchen.")
        print()
        choice = input("Would you like to 1. Enter your parents' room 2. Enter the kitchen ")
        print()
        if choice == "1":
            place = "parentroom" #move to parent room
        elif choice == "2":
            place = "kitchen" #move to kitchen
        else:
            invalid()

    elif place == "kitchen": #kitchen
        if kitch == False:
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You take a step into the kitchen. Nobody is here.")
            kitch = True
        else:
            print("You have already searched this room.")
        zombie()
        if distance == 0:
            break
        print("Across from the kitchen is the living room and further down the")
        print("hall is the foyer. You can find the bathroom on your way to")
        print("the foyer. The other way down the hall leads to the bedrooms.")
        print("There also is a patio door that heads outside.")
        print()
        choice = input("Would you like to 1. Check the living room 2. Walk down to the foyer and bathroom 3. Enter the hall 4. Step outside ")
        print()
        if choice == "1":
            place = "living room" #move to living room
        elif choice == "2":
            while True:
                ans = input("Would you like the check the bathroom on your way to the foyer?(y/n) ")
                print()
                if ans == 'y' or ans == 'Y' or ans == "yes" or ans == "Yes":
                    print("Alright, let's check the bathroom.")
                    place = 'bathroom' #move to bathroom
                    break
                elif ans == 'n' or ans == 'N' or ans == "no" or ans == "No":
                    print("No worries, let's check the foyer.")
                    place = "foyer" #move to foyer
                    break
                else:
                    invalid() #repeat if answer is invalid
                print()
        elif choice == "3":
            place = "hall" #move to hall
        elif choice == "4":
            place = "outside" #move to outside
        else:
            invalid()

    elif place == "bathroom": #bathroom
        if bath == False: #checks bathroom if brother isn't found
            family += 1
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("Oh. It looks like someone is in the bathroom.")
            print("That must be your brother.")
            bname = input("What is his name? ") #ask for brother's name
            print()
            print("You:",bname+", hurry up! We need to go!")
            print(bname+": Why? What's going on?")
            print("You: Did you not hear about the zombie apocalypse?")
            print(bname+": No way! I'll be out as soon as possible.")
            if family == 3: #escape clause if all family members are found
                break
            bath = True
        else:
            print("You have already found",bname,"in the bathroom.")
        zombie()
        if distance == 0:
            break
        choice = input("Would you like to 1. Go down the hall 2. Check the foyer ")
        print()
        if choice == "1":
            place = "hall" #move to hall
        elif choice == "2":
            place = "foyer" #move to foyer
        else:
            invalid()

    elif place == "foyer": #foyer 
        if foy == False:
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("It looks like nobody is in the foyer.")
            foy = True
        else:
            print("You have already checked the foyer.")
        zombie()
        if distance == 0:
            break
        choice = input("Would you like to 1. Check the living room 2. Enter the hall ")
        print()
        if choice == "1":
            place = "living room" #move to living room
        elif choice == "2":
            while True:
                ans = input("Would you like the check the bathroom on your way down the hall?(y/n) ")
                print()
                if ans == 'y' or ans == 'Y' or ans == "yes" or ans == "Yes":
                    print("Alright, let's check the bathroom.")
                    print()
                    place = 'bathroom' #move to bathroom
                    break
                elif ans == 'n' or ans == 'N' or ans == "no" or ans == "No":
                    print("No worries, let's check the hall.")
                    print()
                    place = "hall" #move to hall
                    break
                else:
                    invalid() #repeat if answer is invalid
                print()
        elif choice == "3":
            place = "hall" #move to hall
        else:
            invalid()
            
    elif place == "living room": #living room
        if living == False:
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You step into the living room. Nobody is here;")
            print("however, you see the TV on and you notice that")
            print("there are already zombies nearby.")
            living = True
        else:
            print("You have already searched the living room.")
        zombie()
        if distance == 0:
            break
        choice = input("Would you like to 1. Go to the foyer 2. Enter the hall ")
        print()
        if choice == "1":
            place = "foyer" #move to foyer
        elif choice == "2":
            place = "hall" #move to hall
        else:
            invalid()

    elif place == "hall": #hall
        if hallway == False:
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You enter the hall that connects both halves of the house.")
            print("Nobody is in sight.")
            hallway = True
        else:
            print("You have already searched the hall.")
        zombie()
        if distance == 0:
            break
        print("One part of the hall connects to the foyer, bathroom,")
        print("living room, and the kitchen, and the other way leads")
        print("to the bedrooms.")
        print()
        choice = input("Would you like to 1. Head to the foyer 2. Check the living room 3. Go to the kitchen 4. Check your parents' room 5. Check your brother's room ")
        print()
        if choice == "1":
            while True:
                ans = input("Would you like the check the bathroom on your way to the foyer?(y/n) ")
                print()
                if ans == 'y' or ans == 'Y' or ans == "yes" or ans == "Yes":
                    print("Alright, let's check the bathroom.") #move to bathroom
                    print()
                    place = 'bathroom'
                    break
                elif ans == 'n' or ans == 'N' or ans == "no" or ans == "No":
                    print("No worries, let's check the foyer.")
                    print()
                    place = "foyer" #move to foyer
                    break
                else:
                    print("Invalid answer. Please try again.") #repeat if answer is invalid
                print()
        elif choice == "2":
            place = "living room" #move to living room
        elif choice == "3":
            place = "kitchen" #move to kitchen
        elif choice == "4":
            place = "parentroom" #move to parents' room
        elif choice == "5":
            place = "brotherroom" #move to brother's room
        else:
            invalid()

    elif place == "brotherroom": #brother's room
        if brother == False:
            guesses += 1
            distance -= 10 #limited guesses with counter
            print("You head towards your brother's room. As you push open")
            print("the door, you realize he isn't there.")
            brother = True
        else:
            print("You have already searched your brother's room.")
        zombie()
        if distance == 0:
            break
        print("You decide to turn around and check elsewhere.")
        print()
        choice = input("Would you like to 1. Head down the hall 2. Check your parents' room ")
        print()
        if choice == "1":
            place = "hall" #move to hall
        elif choice == "2":
            place = "parentroom" #move to parent's room
        else:
            invalid()

if family == 3:
    print()
    print("Congratulations,",name+". You have found all of your family members")
    print("in",guesses,"attempts!")
    print("Now that you have found all of your famly members, let's go stock up on supplies.")
    print()
    choice = input("Would you like to 1. Go to Walmart 2. Go to the local market ")
    print()
    if choice == "1":
        print("Okay, let's go to Walmart.")
        place = "walmart" #move to walmart
    elif choice == "2":
        print("Sounds good! Let's go to the local market.")
        place = "market" #move to karket
    else:
        invalid()

    while True: #second loop
        if place == "market": #market
            inFile = open("isp.txt","r") #create link to txt file
            title = inFile.readline().rstrip("\n")
            product = inFile.readline().rstrip("\n")
            price = inFile.readline().rstrip("\n")
            print("You arrive at the market and are prompted with this catalogue:") #create catalogue for market
            print()
            print(title.center(30))
            print("".center(30,"-"))
            while product != "":
                print(product.ljust(15,"."),price.rjust(15,"."))
                product = inFile.readline().rstrip("\n")
                price = inFile.readline().rstrip("\n")
            inFile.close() #close file

            print()
            print("Unfortunately, you only have $35 to spend, so your money must be spent wisely.")

            bal = 35 #assign variable for money left to spend
            receipt = [""]*5 #create an array to use for a receipt

            for x in range(5): #for loop to add values to array
                if bal == 0:
                    print()
                    print("You have no money left!")
                    break
                elif bal != 0:
                    while True:
                        print()
                        item = input("What item do you wish to buy?('Done' to exit) ")
                        if item == 'done' or item == 'Done': #escape clause
                            break
                        elif item == 'Chicken' or item == 'chicken': #chicken
                            if bal < 20:
                                print("Not enough money!")
                            else:
                                print("Purchasing chicken.")
                                receipt[x] = 'Chicken' #add chicken to receipt
                                bal -= 20 #charge for chicken
                                break
                        elif item == 'Bread' or item == 'bread': #bread
                            if bal < 10:
                                print("Not enough money!")
                            else:
                                print("Purchasing bread.")
                                receipt[x] = 'Bread' #add bread to receipt
                                bal -= 10 #charge for bread
                                break
                        elif item == 'fruit' or item == 'Fruit': #fruit
                            if bal < 5:
                                print("Not enough money!")
                            else:
                                print("Purchasing fruit.")
                                receipt[x] = 'Fruit' #add fruit to receipt
                                bal -= 5 #charge for fruit
                                break
                        elif item == 'vegetables' or item == 'Vegetables': #vegetables
                            if bal < 4:
                                print("Not enough money!")
                            else:
                                print("Buying vegetables.")
                                receipt[x] = 'Vegetables' #add vegetables to receipt
                                bal -= 4 #charge for vegetables
                                break
                        elif item == 'Water' or item == 'water': #water
                            if bal < 2:
                                print("Not enough money!")
                            else:
                                print("Buying water.")
                                receipt[x] = 'Water' #add water to receipt
                                bal -= 2 #charge for water
                                break
                        else:
                            print("Not an option.")
                    if item == 'done' or item == 'Done':
                        break
                    print(bal,"dollars remaining.")
            print()
            print("Here is what you purchased:") #print receipt
            print("".ljust(20,"-"))
            for x in receipt:
                print(x)
            print("Total: $"+str(35-bal))
            print("".ljust(20,"-"))
            print()
            print("You have a final balance of",bal,"dollars!")#return final balance
            print()
            win = True
            break
            
        elif place == "walmart": #walmart
            print("You arrive at Walmart and you notice it is a disaster.")
            print("You also notice an old man struggling to carry his supplies.")
            print()
            choice = input("Would you like to 1. Help the man 2. Ignore the man and get your supplies 3. Leave and go to the market instead ")
            print()
            if choice == "1": #help the man
                print("You decide to go help the man. It appears that he has already")
                print("been infected by a zombie, thus infecting you too.")
                print()
                win = False #game ends
                break
            elif choice == "2":
                print("You decide to ignore the man so you are able to gather")
                print("supplies. It turns out this whole building has been")
                print("infected by zombies.")
                print()
                choice = input("Would you like to 1. Leave and go to the market instead 2. Attempt to gather supplies ")
                print()
                if choice == "1":
                    print("Alright, let's go the the market instead.")
                    place = "market" #move to market
                elif choice == "2":
                    print("You decide to stay at Walmart to gather supplies.")
                    print("While in the meat aisle, you get cornered by ten")
                    print("zombies. Unfortunately, you are unable to escape.")
                    print()
                    win = False #game ends
                    break
                else:
                    invalid()
            elif choice == "3":
                print("Alright, let's go to the market instead.")
                place = "market" #move to market
            else:
                invalid()

if win == True:
    print("Now that you have grabbed food and water, you should head back")
    print("to your shelter to protect your family.")
    print("Good luck out there,",name+"!")
    print()
    print("CONGRATULATIONS! You found all your family members and") #winning message
    print("you were able to provide supplies for them in time!")
    print()
    print("YOU WON! Thanks for playing 'Choose Your Adventure:")
    print("Zombie Apocalypse!")

elif win == False:
    print("Sorry! Unfortunately, you were unable to survive the") #losing message
    print("zombie apocalypse...")
    print()
    print("YOU LOST! Thanks for playing 'Choose Your Adventure:")
    print("Zombie Apocalypse!")

        
        
        
