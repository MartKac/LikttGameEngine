from tkinter import *
from PIL import ImageTk
from . import Actor
from . import Wall

'''
Main script. Without it
the game engine wouldn't run.
'''

has_prev_key_release = None

class Main:
  def __init__(self, canvas=None, window=None, wh=None, bgcolor=None, bgimg=None, title=None):
    # Variables
    
    self.iter = 0
    
    self.last_key = None
    
    # create window and canvas if needed
    
    if canvas == None and window == None:
      self.window = Tk()
      if wh == None:
        self.canvas = Canvas(self.window)
      else:
        self.canvas = Canvas(self.window, width=wh[0], height=wh[1])
    else:
      self.canvas = canvas
    
    if title != None:
      self.window.title(title)
    else:
      self.window.title("LTGE")
    

    
    # BG color
    
    self.canvas.config(bg="black")
    
    if bgcolor != None:
      self.canvas.configure(bg=bgcolor)
    
    if bgimg != None:
      # BG image
      
      bgimage = ImageTk.PhotoImage(file=bgimg)
      
      self.canvas.config(bg=bgimage)
    
    
    
    # Actors
    
    self.Actors = {}
    
    # Walls
    
    self.Walls = {}
    
    # keys
    
    self.keys = {}
    
    # Key bindings
    
    self.window.bind("<KeyPress>", lambda e:self.KeyDownDebounce(e))
    self.window.bind("<KeyRelease>", lambda e:self.KeyUpDebounce(e))
    
  
  def loop(self):
    '''
    main.loop() function will handle movement and
    will call the animations in Actor.py
    '''
    
    self.window.after(30, self.loop)
    
    # iter
    
    if self.iter >= 1000:
      self.iter = 0
    else:
      self.iter = self.iter+1
    
    for actor in self.Actors:
      self.Actors[actor].Movement(self.keys, self.Walls)
    
  
  def ChangeBgImage(self, bgimg):
    '''
    this function will change the background image 
    of the canvas. It takes as an argument path to the image.
    '''
    
    bgimage = ImageTk.PhotoImage(file=bgimg)
      
    self.canvas.config(bg=bgimage)
  
  def ChangeBgColor(self, bgcolor):
    '''
    this function will change the background color 
    of the canvas. It takes as an argument name of the color
    for example:
    'black'
    but also
    #FFFFFF
    '''
    
    self.canvas.config(bg=bgcolor)
  
  def CreateActor(self, name, x, y, movekeys=None, w=0, h=0, speed=1):
    '''
    Create a fully working Actor ( spirit ) in the scene
    '''
    
    if name not in self.Actors:
      if movekeys != None:
        self.Actors[name] = Actor.Actor(self.canvas, x, y, w, h, movekeys=movekeys, speed=speed)
        self.Actors[name].Render()
        return 0
      elif movekeys == None:
        self.Actors[name] = Actor.Actor(self.canvas, x, y, w, h, speed=speed)
        self.Actors[name].Render()
        return 0
    return 1
  
  def CreateWall(self, name, x, y, movekeys=None, w=0, h=0, transparent=False):
    '''
    Creates a wall in the scene
    '''
    
    if name not in self.Walls:
      if movekeys != None:
        self.Walls[name] = Wall.Wall(self.canvas, x, y, w, h, movekeys=movekeys)
        self.Walls[name].Render(transparent=transparent)
        return 0
      elif movekeys == None:
        self.Walls[name] = Wall.Wall(self.canvas, x, y, w, h)
        self.Walls[name].Render(transparent=transparent)
        return 0
    return 1
  
  def CreateWallsAround(self):
    
    
    x = self.canvas.winfo_reqwidth()-2
    y = self.canvas.winfo_reqheight()-2
    
    self.Walls["~AroundWall1"] = Wall.Wall(self.canvas, -1, 0, 1, y)
    self.Walls["~AroundWall2"] = Wall.Wall(self.canvas, x+1, 0, 1, y)
    
    self.Walls["~AroundWall3"] = Wall.Wall(self.canvas, 0, -1, x, 1)
    self.Walls["~AroundWall4"] = Wall.Wall(self.canvas, 0, y+1, x, 1)
    
  
  def MoveActorWithConsideringWalls(self, name, x, y):
    '''
    moves actor with stoping before walls
    '''
    
    if name in self.Actors:
      self.Actors[name].MoveIfPossible(x, y, self.Walls)
    else:
      raise NameError("Name is not in the actor list ( main.Actors )")
  
  def MoveActorWithoutConsideringWalls(self, name, x, y):
    '''
    moves actor without stoping before walls
    '''
    
    if name in self.Actors:
      self.Actors[name].Move(x, y)
    else:
      raise NameError("Name is not in the actor list ( main.Actors )")
  
  def MoveWall(self, name, x, y):
    '''
    Moves wall
    '''
    
    if name in self.Walls:
      self.Walls[name].Move(x, y)
    else:
      raise NameError("Name is not in the wall list ( main.Walls )")
  
  # Keys
  
  def KeyDownDebounce(self, e):
    global has_prev_key_release
    if has_prev_key_release:
      self.window.after_cancel(has_prev_key_release)
      has_prev_key_release = None
    self.KeyDown(e)  

  def KeyUpDebounce(self, e):
    global has_prev_key_release
    has_prev_key_release = self.window.after_idle(self.KeyUp, e)

  def KeyDown(self, e):
    if e.keycode not in self.keys:
      self.keys[e.keycode] = e.keysym
    self.last_key = e.keycode  

  def KeyUp(self, e):
    has_prev_key_release = None
    if e.keycode in self.keys:
      del self.keys[e.keycode]
  
  # start
  
  def Start(self):
    '''
    Starts windows mainloop and loop
    '''
    
    self.loop()
    self.canvas.grid()
    self.window.mainloop()
