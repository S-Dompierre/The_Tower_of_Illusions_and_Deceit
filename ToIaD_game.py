class Ending:
    ending_seen = 0

    def __init__(self, name):
        self.name = name
        self.is_seen = False
    
    def see_ending(self):
        if self.is_seen == False:
            Ending.ending_seen += 1
            self.is_seen = True
        pass

ending_list = []

def choice():
    choice = input("What do you do?")
    while choice != "1" and choice != "2":
        choice = input("This is not a valid input. Input either '1' or '2' to choose your action.")
    return int(choice)
