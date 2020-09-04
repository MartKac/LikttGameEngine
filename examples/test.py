from src import main


class Game:
    def __init__(self):
        self.main = main.Main(title="Test game", wh=(400, 400))
        self.main.createActor("Actor1", 10, 10,
                              movekeys={"up": 25, "down": 39, "left": 38, "right": 40, "shift": 50},
                              speed=10
                              )
        self.main.createWallsAround()

    def loop(self):
        self.main.window.after(30, self.loop)

        # loop in main

        self.main.loopSegment()

    def start(self):
        self.loop()
        self.main.start()


if __name__ == '__main__':
    a = Game()
    a.start()
