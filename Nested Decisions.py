# task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# task 2
    
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":  
    action = input("Light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You illuminate the cave and find ancient artifacts!")
    elif action == "proceed in the dark":
        print("You stumble upon a hidden passage!")
       

# task 3
            
if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You illuminate the cave and find ancient artifacts!")
    elif action == "proceed in the dark":
        print("You stumble upon a hidden passage!")
    else:
        pass











