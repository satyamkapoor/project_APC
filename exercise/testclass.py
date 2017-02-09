class Car():

    def __init__(self):
        self.bcd = "Huhuhuh"
        self.mom = "mommy"

    def printmom(self):
        return self.mom

class Redona(Car):
    def __init__(self):
        super(Redona,self).__init__()
        print("namaste")

    def printmom(self):
        return "redona shouts"

    def __str__(self):
        return "{}jkjkjk".format(self.mom)



c=Redona()
print(c)
