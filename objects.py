class Dave(object):
    def __init__(self):
        self.hp = 250
        self.damage = 5
        self.sword = 50
        self.dagger = 10
        self.axe = 25
        self.dead = False
        self.has_axe = False
        self.has_sword = False

class Golem(object):
    def __init__(self):
        self.hp = 75
        self.damage = 15
        self.dead = False
    
class Lobby_Manager(object):
    def __init__(self):
        self.hp = 5
        self.damage = 0
        self.dead = False

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
