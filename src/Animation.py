from . import Actor


class Animation(Actor.Actor):
    """
    Animation class for making particles
    and simple animated objects
    """

  def oneLoopSegment(self):
      """
      One loop segment that is called in main.loop().
      Updates animation.
      """
      if self.AnimationState >= len(self.imglist):
          self.AnimationState = self.AnimationState + 1
      self.changeImage(self.imglist[self.AnimationState])
