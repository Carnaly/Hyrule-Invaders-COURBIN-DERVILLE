class enemy:
    def __init__(self, name, mvt_speed, life_point):
        self.name = name
        self.speed = mvt_speed
        self.life = life_point

    def printname(self):
        print(self.name, self.speed, self.life)

class octorok(enemy):
    def __init__(self, mvt_speed, life_point):
        enemy.__init__(self, "octorok", mvt_speed, life_point)

#class moblin(enemy):
#    def __init__(self, mvt_speed, life_point):
#       enemy.__init__(self, "moblin", mvt_speed, life_point)

#class lynel(enemy):
#    def __init__(self, mvt_speed, life_point):
#        enemy.__init__(self, "lynel", mvt_speed, life_point)

x = octorok(10,1)
x.printname()