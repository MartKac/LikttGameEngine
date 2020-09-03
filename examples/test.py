from src import main


class Main:
    def __init__(self):
        self.m = main.Main(bgcolor="green", wh=(500, 500))
        self.m.createActor("actor1", 10, 10, w=10, h=10,
                           movekeys={"up": 25, "down": 39, "left": 38, "right": 40}, speed=5)
        self.m.createWall("wall1", 50, 50, w=40, h=40)
        self.m.createWallsAround()

    def start(self):
        self.m.start()


a = Main()
a.start()
