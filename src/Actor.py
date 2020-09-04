from PIL import ImageTk


class Actor:
    """
    class for creating spirits
    in the scene
    """

    def __init__(self, canvas, x, y, w, h, startimage=None, movekeys=None, speed=1, shiftspeed=1, imglist=None):

        print(shiftspeed)

        # Animation

        self.imglist = imglist
        self.Animationstate = 0
        self.lastdir = None

        # Moving

        self.speed = speed

        # Canvas and position

        self.canvas = canvas

        self.x = int(x)
        self.y = int(y)

        self.w = w
        self.h = h

        self.startimage = startimage

        self.movekeys = movekeys
        self.box = None

    def changeImage(self, img):
        self.canvas.itemconfig(self.box, image=img)

    def render(self, transparent=False):
        if not transparent:
            if self.startimage is not None:
                """
                If the image is specified,
                make sprite with image.
                """

                img = ImageTk.PhotoImage(file=self.startimage)
                self.box = self.canvas.create_image(self.x, self.y, image=img)

            else:
                """"
                if image is not specified, then make
                rectangle that is 10x10 and color it
                red.
                """

                self.box = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill="red",
                                                        outline=""
                                                        )

                self.w = 10
                self.h = 10
        if transparent:
            self.box = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill="", outline="")

    def getCoords(self):
        """
        Returns x and y argument of self.box
        """

        c = self.canvas.coords(self.box)

        x = c[0]
        y = c[1]

        self.x = x
        self.y = y
        return x, y

    def movement(self, keys, obstacles):
        """
        Movement function will move the character
        and also change the animation state
        """

        if self.movekeys is not None:
            if self.movekeys["up"] in keys:
                self.moveIfPossible(0, -self.speed, obstacles)
                self.lastdir = "up"

            if self.movekeys["down"] in keys:
                self.moveIfPossible(0, self.speed, obstacles)
                self.lastdir = "down"

            if self.movekeys["left"] in keys:
                self.moveIfPossible(-self.speed, 0, obstacles)
                self.lastdir = "left"

            if self.movekeys["right"] in keys:
                self.moveIfPossible(self.speed, 0, obstacles)
                self.lastdir = "right"
            else:
                self.lastdir = None

    def moveIfPossible(self, dx, dy, obstacles):
        """
        Move the spirit, if there are not any
        obstacles in the way
        ( self.Walls, other obstacles )
        """

        if self.wouldIntersectAny(dx, dy, obstacles):
            pass
        if not self.wouldIntersectAny(dx, dy, obstacles):
            self.Move(dx, dy)

    def Move(self, x, y):
        """
        Move box
        """

        self.canvas.move(self.box, x, y)
        self.x, self.y = self.getCoords()

    def changeMovementNum(self):
        if self.Animationstate != len(self.imglist):
            self.Animationstate = self.Animationstate + 1
        else:
            self.Animationstate = 0

    def movementRender(self):
        """
        This function takes state of
        movement animation state
        (integer)
        end changes image of the spirit
        """
        if self.imglist is not None:
            if self.lastdir == "up":
                self.changeImage(ImageTk.PhotoImage(file=self.imglist["up"][self.Animationstate]))
            if self.lastdir == "down":
                self.changeImage(ImageTk.PhotoImage(file=self.imglist["down"][self.Animationstate]))
            if self.lastdir == "left":
                self.changeImage(ImageTk.PhotoImage(file=self.imglist["left"][self.Animationstate]))
            if self.lastdir == "right":
                self.changeImage(ImageTk.PhotoImage(file=self.imglist["right"][self.Animationstate]))
            else:
                self.changeImage(ImageTk.PhotoImage(file=self.imglist["standing"]))

    def intersectsX(self, b):
        """
        Checks for intersection with
        another object on axis X
        """

        if b.x >= self.x + self.w:
            return False
        if self.x >= b.x + b.w:
            return False
        return True

    def intersectsY(self, b):
        """
        Checks for intersection with
        another object on axis Y
        """

        if b.y >= self.y + self.h:
            return False
        if self.y >= b.y + b.h:
            return False
        return True

    def intersects(self, b):
        """
        Checks for intersection
        with another object on
        both x and y axis
        """

        return self.intersectsX(b) and self.intersectsY(b)

    def wouldIntersect(self, dx, dy, b):
        """
        Checks if spirit would
        intersects with selected object
        """

        self.x = self.x + dx
        self.y = self.y + dy
        result = self.intersects(b)
        self.x = self.x - dx
        self.y = self.y - dy
        return result

    def wouldIntersectAny(self, dx, dy, b):
        """
        Checks if spirit would
        intersects with any object
        """

        for obj in b:
            if self.wouldIntersect(dx, dy, b[obj]):
                return True
        return False
