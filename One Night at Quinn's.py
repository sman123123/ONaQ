def Intro():
    #print a main menu and instructions.
    print("============================================")
    print("RPG Game")
    print("============================================")
    Commands()
    Location()


def Commands():
    print("Commands:")
    print("'help' - Get list of commands.")
    print("'look' - Get description of surroundings.")
    print("'location' - Get current location.")
    print("'go [direction]'")
    print("'get [item]'")

def Location():
    #print your current location.
    print("--------------------------------------------")
    print("You are in the " + rooms[currentRoom]["name"] + ".")
    #print item if there is one.
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"] + ".")
    print("--------------------------------------------")

def Inventory():
    #print your inventory.
    print("--------------------------------------------")
    print("Inventory : " + str(inventory))
    print("--------------------------------------------")


def Description():
    #print description of current room.
    print(rooms[currentRoom]["description"])

#an inventory, which is initially empty.
inventory = []

#a dictionary linking a room to other room positions
rooms = {
           1 : { "name" : "Upstairs Living Room" ,
                 "description" : "-" ,
                 "north" : 6
                 "east" : 8,
                 "south" : 7,
                 "west" : 2 } ,

           2 : { "name" : "Small Hallway in Living Room" ,
                 "description" : "-" ,
                 "north" : 3,
                 "east" : 1,
                 "south" : 5,
                 "west" : 4,
                 "item" : "sword" } ,

           3 : { "name" : "Riley's Room" ,
                 "description" : "-" ,
                 "south" : 2 } ,

           4 : { "name" : "Upstairs Bathroom" ,
                 "description" : "-" ,
                 "east" : 2 } ,
           
           5 : { "name" : "Tristan's Room" ,
                 "description" : "-" ,
                 "north" : 2 }

           6 : { "name" : "Front Yard" ,
                 "description" : "-" ,
                 "south" : 1 }

           7 : { "name" : "Back Yard" ,
                 "description" : "-" ,
                 "north" : 1 }

           8 : { "name" : "Upstairs Kitchen" ,
                 "description" : "-" ,
                 "south" : 9,
                 "west" : 1 }
           
           9 : { "name" : "Stairwell" ,
                 "description" : "-" ,
                 "up" : 8,
                 "down" : 10 }

           10 : { "name" : "Downstairs Kitchen" ,
                 "description" : "-" ,
                 "north" : 9 }
                 

        }

#start the player in room 1.
currentRoom = 1

Intro()

#loop infinitely
while True:
    
    #get the player's next 'move'
    #.split() breaks it up into a list array
    #eg typing 'go east' would give the list
    #['go','east']
    move = input(">").lower().split()

    #if they type 'help'
    if move[0] == "help":
        Commands()

    #if they type 'location'
    if move[0] == "location":
        Location()


    #if they type 'look'
    if move[0] == "look":
        Description()
        if "item" in rooms[currentRoom]:
            print("You see a " + rooms[currentRoom]["item"] + ".")
        else:
            pass


    #if they type 'inventory'
    if move[0] == "inventory":
        Inventory()

    
    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to this one
            currentRoom = rooms[currentRoom][move[1]]
            Location()
        #if there is no door (link) to the new room
        else:
            print("You can't go that way!")

    #if they type 'get' first
    if move[0] == "get":
        #check if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add the item to their inventory
            inventory += [move[1]]
            #display a success message
            print("You got the " + str(move[1]) + "!")
            #delete the item from the room
            del rooms[currentRoom]["item"]
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print("There isn't a " + move[1] + " to get!")
