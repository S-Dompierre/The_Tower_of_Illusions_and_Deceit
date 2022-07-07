import sys
import time

def slowprint(str):
	for letter in str + '\n':
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(1./90)

class Ending:
    ending_seen = 0

    def __init__(self, name, number):
        self.name = name
        self.is_seen = False
        self.number = number
    
    def __repr__(self):
        return ("\nEnd {number} - {name}\n".format(number = self.number, name = self.name))
    
    def see_ending(self):
        if self.is_seen == False:
            Ending.ending_seen += 1
            self.is_seen = True
        slowprint(self.__repr__())
        slowprint("You have seen {ending} of the 4 endings.\n\n".format(ending = Ending.ending_seen))
        pass

ending_1 = Ending("Climbing", 1)
ending_2 = Ending("Traps", 2)
ending_3 = Ending("Poison", 3)
ending_4 = Ending("The Top", 4)
ending_5 = Ending("Go Home (Secret Ending)", 5)

def choice():
    choice = input("What do you do?")
    while choice != "1" and choice != "2":
        choice = input("This is not a valid input. Input either '1' or '2' to choose your action.")
    return (choice)

slowprint("Legends are told of a Tower that can grant you whatever you wish for, should you reach the top. Few people are able to find it, however. Its place in the land is ever-changing, never in the same region twice. They call it the Tower of Illusions and Deceit, for you should never trust a single thing you see while inside.\n\nYou are an adventurer that roams the land, and on a starry night like many other in the wild, you chance upon a dark shape. When you approach, you recognize the telltale signs of the Tower of Illusions and Deceit. Black stone, darker than the night itself, extending to the sky seemingly until the end of the universe. A small ebony door the only way to enter. Now that it is in front of you, you have to go inside.\n\n1) Go inside")

while Ending.ending_seen != 5:
    if Ending.ending_seen == 0:
        choice_1 = input("What do you do?")
        while choice_1 != "1":
            choice_1 = input("This is not a valid input. Input '1' to choose your action.")
    elif Ending.ending_seen > 0 and Ending.ending_seen < 3:
        slowprint("You are at the door of the Tower of Illusions and Deceit, its black stone, darker than the night itself, extending to the sky seemingly until the end of the universe. You feel as if you've been here before, but can't remember exactly when or why.\n\n1)Go inside")
        choice_1 = input("What do you do?")
        while choice_1 != "1":
            choice_1 = input("This is not a valid input. Input '1' to choose your action.")
    elif Ending.ending_seen == 4:
        slowprint("You've unlocked access to the 5th secret ending. Replay the game to find it!\n")
        slowprint("You are at the door of the Tower of Illusions and Deceit, its black stone, darker than the night itself, extending to the sky seemingly until the end of the universe. You feel as if you've been here before, but can't remember exactly when or why. But you also feel that you've seen all there is to see.\n\n1)Go inside\n2)Go back")
        choice_1 = choice()
    
    if choice_1 == "1":
        pass
    if choice_1 == "2":
        slowprint("2) You go back without entering the tower. Life goes on. Your life isn't exciting, but it is fulfilling. You often wonder about what would've happened had you entered the tower. Would you have incalculable riches? Maybe. Sometimes, you regret. But more often than not, you're happy with the life that you have. Some things are better left as dreams.")
        ending_5.see_ending()
        continue

    slowprint("1) You open the wooden door and cautiously go inside. As soon as you pass the entrance, the door suddenly closes behind you. You try to go back outside, but the door is stuck. No choice but to go forward. The first floor seems rather empty. The only thing you can see are two stairways tucked away at opposite corners, one going upwards and one going downwards.\n\n1)Go upwards\n2)Go downwards")
    choice_2 = choice()
    if choice_2 == "1":
        slowprint("1) The legends say that you need to reach the top, so you should go upwards... right? As you climb the stairs, you see through the arrowslits that the ground is getting further and further away. So you keep going. And going. And going. And going. You no longer feel hunger nor tiredness. The end of the staircase always seems to be around the corner, but you never reach it. So you keep going. And going.")
        ending_1.see_ending()
        continue
    if choice_2 == "2":
        pass

    slowprint("2) You decide to go down the flight of stairs. After a couple of minutes, you reach the next floor. The floor is reminiscent of a decrepit cathedral, with three long aisles separated by two rows of dilapidated columns. The only light source is a flickering campfire, around which you see figure scuttling haphazardly. Looking more carefully, they seem to be small green men with pointed ears clothed only in loincloths. Goblins! Two choices present themselves to you. You could approach cautiously the goblins, but you are sure to be found by them. Or you could sneak past the goblins, creeping between the columns.\n\n1)Approach the goblins\n2)Sneak past the goblins")
    choice_3 = choice()
    if choice_3 == "1":
        pass
    if choice_3 == "2":
        slowprint("2) It is known that goblins are dangerous and unpredictable creatures. The safest bet would, of course, be to sneak past them. So you crouch behind a column, going quickly and quietly from one to the next. The goblins seem absorbed by whatever it is they're doing, mumbling between themselves. So you successfully sneak past them. You let out a sigh of relief. You're safe! Or so you believe until you step on a loose stone that sinks into the floor. The ground opens up like the maw of a beast. So you plummet into darkness.")
        ending_2.see_ending()
        continue

    slowprint("1) You decide to approach the goblins. As you get closer to the campfire, they all stop moving, turning towards you. After a minute of staring at each other, one of them pulls out a scrap of paper, looks at it and then recites to you: \"Ahem. Welcome to the Tower of Illusions and Deceit™. We hope you find what you are looking for in The Tower™. Please follow my colleagues and I to proceed in your journey. And beware of traps!\" As the goblin stops speaking, he and his companions stand in a row and move in a convoluted pattern to the next staircase. You follow carefully behind them, making sure that you step exactly where the goblins have passed. You swiftly thank your guides and proceed to the next floor.\n\nYou seem to be in a banquet hall of sorts, much better lit than the last floor. The tables are overflowing with decadent food that you would expect to find in a palace. Dazzled, you find it abnormal that this floor seems to be empty. Wait. You spot what appears to be the host feasting alone in the main seat. A large man, with rings on each of his oil-stained finger and dressed in a silk tunic. As he sees you enter, he gestures to you to come and sit with him. While you come closer, he says to you: \"Welcome to my floor. I know that you must be in a hurry, but before you go, at least have a toast with me!\" The host pushes a cup filled to the brim with what looks to be wine and scrutinizes you with his beady eyes. You notice that the cup that he passed you is faintly bubbling and smoking. It doesn't look very safe. What if you took his cup?\n\n1)Take the host's cup\n2)Take your cup")
    choice_4 = choice()
    if choice_4 == "1":
        slowprint("1) The cup that the host handed to you is pretty suspicious... you promptly take the further cup and raise it to toast the host. He freezes, then gives you a meaningful smile and raises his glass. \"To your success!\" You both empty your cup. The wine has a very powerful fragrance and is slightly spicy. Very spicy. You feel your throat burning. \"Being the immortal host of the tower, I have to find ways to entertain myself. I like to taste the various mortal poisons of the land. So, what do you think of this cocktail?\" Before you can answer, your vision turns black and you lose consciousness.")
        ending_3.see_ending()
        continue
    if choice_4 == "2":
        pass

    slowprint("2) You take the cup handed to you and raise it. \"To your success!\" You both empty your cup. As you taste the wine, you find it to be the best one you've ever drunk. It's rich and mellow taste linger in your mouth. As he watches you enjoy your cup, the host tells you: \"I'm somewhat of an amateur winemaker. How do you find my wine?\" You praise his drink to the heavens, then bid him farewell and proceed to the staircase behind him.\n\nYou've reached the top of the tower. Or is it the bottom? You're not sure anymore. Looking through the stained glass depicting fantastical creatures, you see the forest far below you. The top floor is empty except for a white throne that seems to be made of porcelain. So you sit on it. And your destiny changes. Everything you hoped for at your fingertips. As you live the life of your dreams, you always feel as though you're in an illusion. But if you're happy, does it really matter?")
    ending_4.see_ending()
    continue




    