from src import main
import time

class Game:
    def __init__(self):
        self.main = main.Main(title="Test game", wh=(400, 400), bgimg="background1d2.png")
        self.main.createActor("Actor1", 10, 10,
                              movekeys={"up": 25, "down": 39, "left": 38, "right": 40, "shift": 50},
                              speed=2, imglist={
                                                "up": ["up/up0.png", "up/up1.png", "up/up2.png", "up/up3.png", "up/up4.png", "up/up5.png"],
                                                "down": ["down/down0.png", "down/down1.png", "down/down2.png", "down/down3.png", "down/down4.png", "down/down5.png"],
                                                "left": ["left/left0.png", "left/left1.png", "left/left2.png", "left/left3.png", "left/left4.png", "left/left5.png"],
                                                "right": ["right/right0.png", "right/right1.png", "right/right2.png", "right/right3.png", "right/right4.png", "right/right5.png"],
                                                "standing": "standing/standing3.png",
                                                "Num": 5
                                                },
                              startimage="standing/standing3.png"
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
