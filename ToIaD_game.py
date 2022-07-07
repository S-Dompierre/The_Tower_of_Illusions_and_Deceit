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
        return ("End {number} - {name}".format(number = self.number, name = self.name))
    
    def see_ending(self):
        if self.is_seen == False:
            Ending.ending_seen += 1
            self.is_seen = True
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
    return int(choice)
