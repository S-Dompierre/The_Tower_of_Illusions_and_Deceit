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