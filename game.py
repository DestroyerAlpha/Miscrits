from sys import exit
import random

def gender():
    ugender = raw_input(">")
    
    if ugender == 'Male':
        print "Please enter your name:"
        naming = raw_input(">")
        history(naming)
    
    elif ugender == 'Female':
        print "Please enter your name:"
        naming = raw_input(">")
        history(naming)
    
    elif ugender == 'Others':
        print "Please enter your name:"
        naming = raw_input(">")
        history(naming)
    
    else:
        print "We don't know what that means. Try entering Male, Female or Others" 
        gender(0)
    return naming

def start(value):
    print """
    Welcome Adventurer to the magical World of Miscria, 
    filled with magical creatures called Miscrits.
    An excellent game in Facebook, now in this python program. This is sure to have you hooked on for hours!.
    Please select your gender:-
    Male
    Female
    Others
    """
    gender()
    return
    
def history(name):
    
    print """The history of the land of Miscria is explored a lot and it is unknown how it was created and founded.
    It is known however that the land of Miscria belonged to the Miscrits.  
    Humanity came to Miscria long ago and settled there.  
    Some humans co existed with the miscrits while others became greedy and despised the miscrits 
    while believing that the power of the miscrits belongs to them.  
    These greedy humans became the magicites and they waged war on the miscrits for centuries. 
    This went on until you, %s who was not from Miscria woke up in that land and went on to
    defeat the magicites and one of their leaders, Apollo Nox.
    However, your journey was not over yet as you, %s is now looking for the essences and find a way to defeat the high priest who founded the magicites.
    """ %(name, name)
    proceed(0)
    return

def proceed(value):
    print "Do you want to proceed as the prophet who has come to rescue the 'Land of Miscria'"
    print "Yes"
    print "or, No"
    descision = raw_input(">")
    if descision == "Yes":
        commonplace()
    elif descision == "No":
        print "I knew you are not The ONE"
        exit(0)
    else:
        print "I don't know what that means"
        proceed(0)
    return

def commonplace():
    print "Good day, This is the common place of the Miscria. You can meet people here, Visit places, Go to battles and much more"
    print "What do you want to do?"
    print "Enter Left to search Miscrits and Right to go Home"

    where_to = raw_input(">")

    if where_to == 'Left':
        search(misc)
    elif where_to == "Right":
        home()
    else:
        print "I don't know what that means."
        commonplace()
    return
misc = ["Aeronox",'Aquanox','Aria','Arigato','Azteko','Barkley','Beelzebug','Beetor','Bibbly','Blazertooth','Bloombat','Bloomple','Blowpuffle','Blub','Bludger','Boltipede','Boltzee','Boo Blazertooth','Boomble','Brainzer','Breezycheeks','Bubblegup','Bubbles','Budillo','Bullo','Butterus']
crits = []
def search(misc):
    print "Searching for a miscrit"
    print "Found one!!!!"
    crit = random.choice(misc)
    print "You found %s" %crit
    crits.append(crit)
    aftermath()
    return

def aftermath():
    print "Do you want to search more?"
    Quest = raw_input('>')
    if Quest == "yes":
        search(misc)
    elif Quest == "no":
        commonplace()
    else:
        print "I don't know what that means, try removing caps."
        aftermath()
    return

def home():
    print "This is your home. here you can see all your miscrits."
    print crits
    commonplace()
    return
