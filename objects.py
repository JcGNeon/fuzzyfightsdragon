class Dave(object):
    def __init__(self):
        self.hp = 250
        self.damage = 5
        self.dead = False
        self.carry_dagger = False
        self.carry_sword = False
        self.carry_axe = False
        self.has_dagger = False
        self.has_axe = False
        self.has_sword = False
    def use_dagger():
        if(self.carry_dagger == True):
            self.has_dagger = True
            self.has_sword = False
            self.has_axe = False
            if(self.has_dagger == True):
                self.damage += 10
            self.has_dagger = False
            self.damage -= 10
        elif(self.carry_dagger == False):
            print "You don't have the dagger.\n"
    def use_sword():
        if(self.carry_sword == True):
            self.has_sword = True
            self.has_axe = False
            self.has_dagger = False
            if(self.has_sword == True):
                self.damage += 50
            self.has_sword = False
            self.damage -= 50
        elif(self.carry_sword == False):
            print "You don't have the sword.\n"
    def use_axe():
        if(self.carry_axe == True):
            self.has_axe = True
            self.has_dagger = False
            self.has_sword = False
            if(self.has_axe == True):
                self.damage += 25
            self.has_axe = False
            self.damage -= 25
        elif(self.carry_axe == False):
            print "You don't have the axe.\n"
    def attack():
        print "Attacking...\n"
    def die():
        if(self.hp <= 0):
            self.dead = True
            print "You have died. GG. You get to start from scratch.\n"

class Golem(object):
    def __init__(self):
        self.hp = 75
        self.damage = 15
        self.dead = False
    def attack():
        Dave.hp -= self.damage
        print "You have been struck. You have %d HP remaining.\n" % Dave.hp
    def die():
        if(self.hp <= 0):
            self.dead = True
            print "You have killed the golem. He dropped an axe. Pick up axe? (y/n)\n"
            answer = raw_input()

            if((answer == 'y') | (answer == 'Y') | (answer == "yes") | (answer == "Yes")):
                Dave.carry_axe = True
                print "You have picked up the axe. You can now use it to kill things and manipulate your environment.\n"
            elif((answer == 'n') | (answer == 'N') | (answer == "no") | (answer == "No")):
                pass
            else:
                print "Invalid input. Try again.\n"

class Lobby_Manager(object):
    def __init__(self):
        self.hp = 5
        self.damage = 0
        self.dead = False
    def greeting():
        print """
        Welcome to the city of Blurnaghen. This is the lobby and I'm the manager. Things just haven't been the same around here since the dragon turned up. It's been terrorizing everyone and nothing has been able to stop it... You're planning on going into town at this time? You better take this dagger for self-defense. Good luck!
        """
        Dave.carry_dagger = True
    def die():
        if(self.hp <= 0):
            self.dead = True
            print "You killed an innocent bystander. You bastard!"

class Wolve(object):
    def __init__(self):
        self.hp = 25
        self.damage = 20
        self.dead = False

class Dragon(object):
    def __init__(self):
        self.hp = 1000
        self.damage = 25
        self.dead = False

class Unstable_rocks(object):
    def __init__(self):
        self.hp = 50
        self.damage = 900
        self.collapsed = False

class Sword_holder(object):
    def __init__(self):
        self.hp = 50
        self.damage = 50
        self.dead = False
