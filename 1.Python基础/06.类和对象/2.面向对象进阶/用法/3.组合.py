class Turtle:

    def __init__(self, x=3):
        self.num = x


class Fish:

    def __init__(self, x):
        self.num = x


class Pool:

    def __init__(self, x, y):
        self.turtle = Turtle(x)  #
        self.fish = Fish(y)

    def print_num(self):
        print("水池里有乌龟%d只,小鱼%d条！" % (self.turtle.num, self.fish.num))


pool = Pool(1, 10)
pool.print_num()
pool2 = Turtle()
print(pool2.num)
