# LikttGameEngine (LTGE)
A simple 2D game engine for Python-Tkinter

## Contacts
Be sure to ask for questions, contact me on mkac003@gmail.com
It may take some time before i reply, i am sorry for that,
and please do not spam.

Before you ask for help with use of LTGE, read the Usage part

## Usage

To use LikttGameEngine, download LikttGameEngine.zip and unpack it in your script's folder. Rename it to 'LikttGameEngine'
open a file in your folder and import it this way:
```python
from LikttGameEngine.src import main
```
Then you can start creating your game.

### Creating a Actor
If you want to have a player or different entity in your scene, actor will create a spirit in your scene.

##### Warning!

Do not create actor by calling:
```python
myactor = Actor()
```
Create it using main's createActor function.
```python
main = Main()

name = "Actor 1"

x = 50
y = 50

main.CreateActor(name, x, y)
```
This example will create a new Actor in the scene.

#### Moving the Actor
We have an actor in our scene, but we cant move it, there are many ways to move the actor.

##### Moving by pressing keys
We need our user to move the player around, without that, the game would be boring.
In this example we are going to bind moving to keys `WASD` and `Left Shift`.
```python
main = Main()

name = "Actor1"

x = 50
y = 50

main.createActor(name, x, y, movekeys={"up": 25, "down": 39, "left": 38, "right": 40, "shift": 50})

```
##### Moving by calling a function
If you want to create bots, automatically moved enemies and others, you may need to use `moveActorWithConsideringWalls` or `moveActorWithoutConsideringWalls`.
Example:
```
main = Main()

name = "Actor1"

x = 50
y = 50

main.createActor(name, x, y)
main.moveActorWithConsideringWalls(name, 10, 0)
```
This will move the actor with name `Actor1` by 10 pixels.
