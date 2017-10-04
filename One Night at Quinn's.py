def Intro():
    #print a main menu and instructions.
    print("====================================================================================================================================================================================================")
    print("One Night at Quinn's")
    print("====================================================================================================================================================================================================")
    Commands()
    Location()
    Event()
    Description()
    Directions()


def Commands():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Commands:")
    print("'help' - Get list of commands.")
    print("'look' - Get description of surroundings.")
    print("'where' - Get current location.")
    print("'bag' - Get list of your Inventory.")
    print("'search' - Search the room more thouroughly for items.")
    print("'go [direction]'")
    print("'take [item]'")
    print("====================================================================================================================================================================================================")

def Location():
    #print your current location.
    print("====================================================================================================================================================================================================")
    print("You are in " + rooms[currentRoom]["name"] + ".")
    #print item if there is one.
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"] + ".")
    #print the people in the room if there are any.
    if "people" in rooms[currentRoom]:
        if len(rooms[currentRoom]["people"]) == 1:
            print(str(rooms[currentRoom]["people"]) + " is in the room.")
        if len(rooms[currentRoom]["people"]) >= 2:
            print(str(rooms[currentRoom]["people"]) + " are in the room.")
    else:
        print("No one is in the room with you.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def Inventory():
    #print your inventory.
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Inventory : " + str(inventory))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def Description():
    #print description of current room.
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(rooms[currentRoom]["description"])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def Directions():
    #print directions out of current room.
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(rooms[currentRoom]["directions"])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def Search():
    #print what they find by searching.
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(rooms[currentRoom]["search"])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def Event():
    #print the last event.
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(events[currentEvent]["event"])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#an inventory, which is initially empty.
inventory = []

#a dictionary linking a room to other room positions, as well as what each room contains.
rooms = {
           1 : { "name" : "the Upstairs Living Room" ,
                 "description" : "You see a large brown sectional wrapping around an area pointing at a TV and a computer monitor. Both are displaying the same random video for some reason." ,
                 "directions" : "There are two doors, the one that leads to the front yard is to the North and the back yard is to the South. \nThe kitchen is to the East and there is a small hallway leading West to the bathroom and upstairs bedrooms." ,
                 "north" : 6,
                 "east" : 8,
                 "south" : 7,
                 "west" : 2 } ,

           2 : { "name" : "the Small Hallway in Living Room" ,
                 "first" : "Yes" ,
                 "description" : "There are a few posters and christmas lights leading into the tiny hallway. Other than that there isn't much to see." ,
                 "directions" : "There are three doors. The door to the North leads to Riley's room, the door to the South leads to Tristan's room, and the door to the West leads to the bathroom. You can return to the living room to the East" ,
                 "north" : 3,
                 "east" : 1,
                 "south" : 5,
                 "west" : 4, } ,

           3 : { "name" : "Riley's Room" ,
                 "first" : "Yes" ,
                 "description" : "Riley's room is full of his stuff. The general things you would expect to find in a room." ,
                 "directions" : "There is only one door, leading South back to the hallway." ,
                 "south" : 2 } ,

           4 : { "name" : "the Upstairs Bathroom" ,
                 "first" : "Yes" ,
                 "description" : "A pretty plain bathroom. Surprisingly clean considering the only people living upstairs are Riley and Tristan..." ,
                 "directions" : "There is only one door, leading East back to the hallway." ,
                 "east" : 2 } ,
           
           5 : { "name" : "Tristan's Room" ,
                 "first" : "Yes" ,
                 "description" : "Tristan's room is full of his stuff, The general things you would expect to find in a room." ,
                 "directions" : "There is only one door, leading North back to the hallway." ,
                 "search" : "You find a briefcase with a combination lock keeping it closed." ,
                 "search item" : "briefcase" ,
                 "north" : 2 } ,

           6 : { "name" : "the Front Yard" ,
                 "first" : "Yes" ,
                 "description" : "The front yard is in pretty good shape, some dead grass here and there but not too bad. Our story takes place back inside the house." ,
                 "directions" : "The front door leading in to the living room is to the south. The yard loops around the house and has a door going into the garage going West." ,
                 "south" : 1,
                 "west" : 10 } ,

           7 : { "name" : "the Back Yard" ,
                 "first" : "Yes" ,
                 "description" : "The back yard is a bit of a mess." ,
                 "directions" : "There is only one door, the sliding glass door leading back into the house to the North." ,
                 "item" : "shovel" ,
                 "north" : 1 } ,

           8 : { "name" : "the Upstairs Kitchen" ,
                 "first" : "Yes" ,
                 "description" : "A fairly clean kitchen. There is a sink, a stove, and some cupboards and drawers." ,
                 "people" : ["Quinn"] ,
                 "directions" : "There is a door along the East wall that leads out into the garage. The living room is to the West and there is a staircase leading down." ,
                 "search" : "You find a knife in a drawer." ,
                 "search item" : "knife" ,
                 "down" : 9,
                 "east" : 10,
                 "west" : 1 } ,
           
           9 : { "name" : "the Stairwell" ,
                 "first" : "Yes" ,
                 "description" : "The stairs are a bit cluttered but clear enough to walk on." ,
                 "directions" : "Up the stairs is one kitchen and down them is a different kitchen." ,
                 "up" : 8,
                 "down" : 11 } ,

           10 : { "name" : "the Garage" ,
                  "first" : "Yes" ,
                  "description" : "Full of art supplies of various sorts and posters of all kinds." ,
                  "directions" : "There are three doors. The door to the East leads out to the front yard, the door to the South leads to the back yard, and the door to the West leads back inside the house." ,
                  "east" : 6,
                  "south" : 7,
                  "west" : 8 } ,

           11 : { "name" : "the Downstairs Kitchen" ,
                  "first" : "Yes" ,
                  "description" : "Same as upstairs, not a whole lot of interest. There is also a washer and dryer down here. The main feature is the giant heater in the middle of the room." ,
                  "directions" : "The staircase leads back up to the upstairs and there are two doors. The door to the North leads into the downstairs living room and the door to the West goes into Quinn and Gabby's room." ,
                  "up" : 9,
                  "north" : 12,
                  "west" : 13 } ,

           12 : { "name" : "the Downstairs Living Room" ,
                  "first" : "Yes" ,
                  "description" : "Some comfy couches pointed at an old TV." ,
                  "directions" : "There are three doors. The door to the East leads to the bathroom, the door to the South leads back into the kitchen, and the door to the West leads into the spare bedroom." ,
                  "east" : 14,
                  "south" : 11,
                  "west" : 15 } ,

           13 : { "name" : "Quinn and Gabby's Room" ,
                  "first" : "Yes" ,
                  "description" : "A bunch of clothes tossed all over the place with a mattress in the middle of the room." ,
                  "directions" : "There is only one door, leading back East into the kitchen." ,
                  "east" : 11 } ,

           14 : { "name" : "the Downstairs Bathroom" ,
                  "first" : "Yes" ,
                  "description" : "A large bathroom with a shower, toilet, and sink." ,
                  "directions" : "There is only one door, leading back West into the living room." ,
                  "west" : 12 } ,

           15 : { "name" : "the Spare Room" ,
                  "first" : "Yes" ,
                  "description" : "No one currently lives here, has a few old waterlogged boxes." ,
                  "directions" : "There is only one door, leading back East into the living room." ,
                  "east" : 12 } ,
                 

        }

#a dictionary of the Events in the game.
events = {
           1 : {"name" : "Introduction" ,
                "event" : "You arrive at Quinn's house to a scene of misery and despair. Poor Stuart has been murdered. \nYou are the only person who has arrived at the house since it happened. Anyone could be the murderer. \nYou are standing in the living room of the house. You have been told that all calls to the police haven't been going through."} ,

           2 : {"name" : "Greeting" ,
                "event" : "As you walk into the kitchen you find Quinn with his head in his hands. He looks up at you suddenly, it is clear he is distraught. Fresh tears run down his face. \n\"How could this have happened!?\" he shouts. \"I can't hardly think right now, go talk to Gabby out back.\""} ,

           3 : {"name" : "Strange sounds from out back" ,
                "event" : "You hear what sounds like someone digging coming from the back yard."} ,

           4 : {"name" : "Quinn acting strange" ,
                "event" : "Quinn seems surprised to see you back so soon. He was washing his hands. \"Uh.. did you talk to Gabby? I didn't hear you go outside...\""} ,

           5 : {"name" : "Signs of Digging" ,
                "event" : "It looks like someone has been digging here. When they heard you opening the door they must have ran off..."}

        }

#start the player in room 6.
currentRoom = 1
#set the game to the first Event
currentEvent = 1

Intro()

#loop infinitely
while True:

    #set the chain of events.
    if currentEvent == 1:
        rooms[8].update({"event" : 2})
    elif currentEvent == 2:
        rooms[1].update({"event" : 3})
    elif currentEvent == 3:
        rooms[8].update({"event" : 4})
        rooms[7].update({"event" : 5})
    elif currentEvent == 5:
        if "event" in rooms[8]:
            del rooms[8]["event"]
    
    #get the player's next 'move'
    move = input(">").lower().split()

    #if they type 'help'
    if move[0] == "help":
        Commands()

    #if they type 'where'
    if move[0] == "where":
        Location()


    #if they type 'look'
    if move[0] == "look":
        Description()
        Directions()
        if "item" in rooms[currentRoom]:
            print("You see a " + rooms[currentRoom]["item"] + ".")
        else:
            pass


    #if they type 'bag'
    if move[0] == "bag":
        Inventory()

    #if they type 'search'
    if move[0] == "search":
        if "search" in rooms[currentRoom]:
            Search()
        else:
            print("You don't find anything interesting.")

    
    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to this one.
            currentRoom = rooms[currentRoom][move[1]]
            Location()
            #check to see if this is the first time the player has entered this room.
            if "first" in rooms[currentRoom]:
                #if true, print description and directions out of the room. After this, player can call them up with the commands.
                Description()
                Directions()
                del rooms[currentRoom]["first"]
            #check to see if there is an event in the room the player hasn't already seen.
            if "event" in rooms[currentRoom]:
                #if true, set current event to this one.
                currentEvent = rooms[currentRoom]["event"]
                Event()
                del rooms[currentRoom]["event"]
        #if there is no door (link) to the new room
        else:
            print("You can't go that way!")

    #if they type 'take' first
    if move[0] == "take":
        #check if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]["item"]:
            #add the item to their inventory
            inventory += [move[1]]
            #display a success message
            print("You got the " + str(move[1]) + "!")
            #delete the item from the room
            del rooms[currentRoom]["item"]

        #otherwise, check if the room contains a search item, and the item is the one they want to get
        elif "search item" in rooms[currentRoom] and move[1] == rooms[currentRoom]["search item"]:
            #add the item to their inventory
            inventory += [move[1]]
            #display a success message
            print("You got the " + str(move[1]) + "!")
            #delete the item from the room
            del rooms[currentRoom]["search item"]
            del rooms[currentRoom]["search"]
            
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print("There isn't a " + move[1] + " to take!")
