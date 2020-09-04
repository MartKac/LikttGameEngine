from .Actor import *


class Wall(Actor):
    """
  Class for creating walls in the scene
  """

    def render(self, transparent=False):
        if transparent:
            print("aaa")
            self.box = self.canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="",
                                                    outline="")
            return

        if self.startimage is not None:
            """
      If the image is specified,
      make sprite with image.
      """

            img = self.startimage
            self.box = self.canvas.create_image(self.x, self.y, image=img)

        else:
            """
      if image is not specified, then make
      rectangle that is 10x10 and color it
      red.
      """

            self.box = self.canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="orange",
                                                    outline="")
