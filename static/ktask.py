# python will say it can't import from the following two sources.
# don't worry, this is because these modules are javascript modules, 
# and they will be loaded when this file is compiled with transcrypt.
# the CLI command to compile this file into transcrypt is
#
# transcrypt -b static/pong.py
#
# this will create a folder called __target__ with these files:
# -com.fabric.js
# -org.transcrypt.__runtime__.js
# -pong.js
# -pong.project
# pong.js is the file that will run the game, the other files support pong.js in the browser.
# ...
# to be compatible with the project structure flask expects, the __target__ folder 
# needs to be in /static

from org.transcrypt.stubs.browser import __pragma__, __new__, document, window, Math, Date, rgb
from com.fabricjs import fabric

__pragma__ ('skip')
__pragma__ ('noskip')
__pragma__ ('noalias', 'clear')

orthoWidth = 1000
orthoHeight = 750
fieldHeight = 650

enter, esc, space = 13, 27, 32

window.onkeydown = lambda event: event.keyCode != space # Prevent scrolldown on spacebar press

class Attribute:    # Attribute in the gaming sense of the word, rather than of an object
    def __init__ (self, exp):
        self.exp = exp                    # Attribute knows game it's part of
        self.exp.attributes.append (self)  # Game knows all its attributes
        self.install ()                     # Put in place graphical representation of attribute
        self.reset ()                       # Reset attribute to start position
                
    def reset (self):       # Restore starting positions or score, then commit to fabric
        self.commit ()      # Nothing to restore for the Attribute base class
                
    def predict (self):
        pass
                
    def interact (self):
        pass
        
    def commit (self):
        pass

    def install(self):
        pass

class Sprite(Attribute):   # Here, a sprite is an attribute that can move
    def __init__ (self, exp, width, height):
        self.width = width
        self.height = height
        Attribute.__init__ (self, exp)
        
    def install (self):     # The sprite holds an image that fabric can display
        self.image = __new__ (fabric.Rect ({
            'width': self.exp.scaleX (self.width), 'height': self.exp.scaleY (self.height),
            'originX': 'center', 'originY': 'center', 'fill': 'white'
        }))
        
    __pragma__ ('kwargs')
    def reset (self, vX = 0, vY = 0, x = 0, y = 0):
        self.vX = vX        # Speed
        self.vY = vY
        
        self.x = x          # Predicted position, can be commit, no bouncing initially
        self.y = y
        
        Attribute.reset (self)
    __pragma__ ('nokwargs')
    
    def commit (self):      # Update fabric image for asynch draw
        self.image.left = self.exp.orthoX (self.x)
        self.image.top = self.exp.orthoY (self.y)
        
    def draw (self):
        self.exp.canvas.add (self.image)

class Stimuli(Sprite):
    margin = 60 # Distance of stimuli from walls
    width = 50
    height = 50
    
    def __init__(self, exp, index):
        self.index = index  # gives eachs square an index
        Sprite.__init__ (self, exp, self.width, self.height)
        
        
    def reset(self):       # create a square and put it in a random position
        Sprite.reset(
            self,
            x = (-orthoWidth/2 + self.width) + (orthoWidth-self.width) * Math.random(),
            y = (-orthoHeight/2 + self.height) + (orthoHeight-self.height) * Math.random()
        )
    
        
class Fixation(Sprite):
    side = 8
    
    def __init__ (self, exp):
        Sprite.__init__ (self, exp, self.side, self.side)
        
class Experiment:
    def __init__ (self):
        self.pause = True                           # Start experiment in paused state
        self.keyCode = None
        
        self.textFrame = document.getElementById ('text_frame')
        self.canvasFrame = document.getElementById ('canvas_frame')
        self.buttonsFrame = document.getElementById ('buttons_frame')
        
        self.canvas = __new__ (fabric.Canvas ('canvas', {'backgroundColor': 'grey', 'originX': 'center', 'originY': 'center'}))
        self.canvas.onWindowDraw = self.draw        # Install draw callback, will be called asynch
        self.canvas.lineWidth = 2
        self.canvas.clear ()    

        self.set_size = 6
        self.attributes = []                        # All attributes will insert themselves here
        self.stimuli = [Stimuli(self, index) for index in range (self.set_size)]    # Pass game as parameter self
        self.fixation_point = Fixation(self)
        
        window.setInterval (self.update, 1)    # Install update callback, time in ms
        window.setInterval (self.draw, 20)      # Install draw callback, time in ms
        window.addEventListener ('keydown', self.keydown)
        window.addEventListener ('keyup', self.keyup)
        
        self.buttons = []
        
        for key in ('F', 'J','space'):
            button = document.getElementById (key)
            button.addEventListener ('mousedown', (lambda aKey: lambda: self.mouseOrTouch (aKey, True)) (key))  # Returns inner lambda
            button.addEventListener ('touchstart', (lambda aKey: lambda: self.mouseOrTouch (aKey, True)) (key))
            button.addEventListener ('mouseup', (lambda aKey: lambda: self.mouseOrTouch (aKey, False)) (key))
            button.addEventListener ('touchend', (lambda aKey: lambda: self.mouseOrTouch (aKey, False)) (key))
            button.style.cursor = 'pointer'
            button.style.userSelect = 'none'
            self.buttons.append (button)
        
            
        self.time = + __new__ (Date)
        
        self.start_exp_timer = self.time
        self.target_presented = bool
        self.isi_presented = bool
        self.all_presented = bool
        self.trial_set = bool
        self.target_color = []
        
        window.onresize = self.resize
        self.resize ()
        
    def install (self):
        for attribute in self.attributes:
            attribute.install ()
        
    def mouseOrTouch (self, key, down):
        if down:
            if key == 'space':
                self.keyCode = space
            elif key == 'enter':
                self.keyCode = enter
            else:
                self.keyCode = ord (key)
        else:
            self.keyCode = None
    
    def update (self):                          # Note that update and draw are not synchronized
        oldTime = self.time
        self.time = + __new__ (Date)
        self.deltaT = (self.time - oldTime) / 1000.

        self.update_squares()
        
        if self.pause:                          # If in paused state
            if self.keyCode == space:           #   If spacebar hit
                self.pause = False              #         Start playing
                
        else:                                   # Else, so if in active state
            for attribute in self.attributes:   #   Compute predicted values
                attribute.predict ()
            
            for attribute in self.attributes:   #   Correct values for bouncing and scoring
                attribute.interact ()
            
            for attribute in self.attributes:   #   Commit them to pyglet for display
                attribute.commit ()
            
            

    def update_squares(self):
        if self.pause:
            for square in self.stimuli:
                if square.image.fill != self.canvas.backgroundColor:
                    square.image.fill = self.canvas.backgroundColor
        
        else:
            
            self.delta_exp_timer = (self.time - self.start_exp_timer)
            
            if self.delta_exp_timer <= 1000:
                if self.trial_set != True:
                    for square in self.stimuli:

                        square.reset()

                        red = 255 * Math.random()
                        green = 255 * Math.random()
                        blue = 255 * Math.random()
                        color = f'rgb({red},{green},{blue})'

                        square.image.fill = color

                        if square == self.stimuli[0]:
                            self.target_color = square.image.fill


                    self.trial_set = True

            if 1000 < self.delta_exp_timer <= 1250:
                for square in self.stimuli:
                    if square.image.fill != self.canvas.backgroundColor:
                        square.image.fill = self.canvas.backgroundColor

        
            if 1250 < self.delta_exp_timer <= 2000:
                if self.target_presented != True:
                    for square in self.stimuli:
                        if square.index > 0:
                            square.image.fill = self.canvas.backgroundColor
                        else:
                            square.image.fill = self.target_color 

                    self.target_presented = True
            
            
            if 2000 < self.delta_exp_timer <= 2500:
                for square in self.stimuli:
                    if square.image.fill != self.canvas.backgroundColor:
                        square.image.fill = self.canvas.backgroundColor

                
            if 2500 < self.delta_exp_timer:
                self.start_exp_timer = self.time
                self.trial_set = False
                self.target_presented = False
                self.isi_presented = False
                self.all_presented = False
            
    def commit (self):
        for attribute in self.attributes:
            attribute.commit ()
        
    def draw (self):
        self.canvas.clear ()
        for attribute in self.attributes:
            attribute.draw ()
                
    def resize (self):
        self.pageWidth = window.innerWidth
        self.pageHeight = window.innerHeight
        
        self.textTop = 0

        if self.pageHeight > 1.2 * self.pageWidth:
            self.canvasWidth = self.pageWidth
            self.canvasTop = self.textTop + 300
        else:
            self.canvasWidth = 0.6 * self.pageWidth
            self.canvasTop = self.textTop + 200

        self.canvasLeft = 0.5 * (self.pageWidth - self.canvasWidth)
        self.canvasHeight = 0.6 * self.canvasWidth

        self.buttonsTop = self.canvasTop + self.canvasHeight + 50
        self.buttonsWidth = 500
            
        self.textFrame.style.top = self.textTop
        self.textFrame.style.left = self.canvasLeft + 0.05 * self.canvasWidth
        self.textFrame.style.width = 0.9 * self.canvasWidth
            
        self.canvasFrame.style.top = self.canvasTop
        self.canvasFrame.style.left = self.canvasLeft
        self.canvas.setDimensions ({'width': self.canvasWidth, 'height': self.canvasHeight})
        
        self.buttonsFrame.style.top = self.buttonsTop
        self.buttonsFrame.style.left = 0.5 * (self.pageWidth - self.buttonsWidth)
        self.buttonsFrame.style.width = self.canvasWidth
        
        self.install ()
        self.commit ()
        self.draw ()
        
    def scaleX (self, x):
        return x * (self.canvas.width / orthoWidth)
            
    def scaleY (self, y):
        return y * (self.canvas.height / orthoHeight)   
        
    def orthoX (self, x):
        return self.scaleX (x + orthoWidth // 2)
        
    def orthoY (self, y):
        return self.scaleY (orthoHeight - fieldHeight // 2 - y)
                
    def keydown (self, event):
        self.keyCode = event.keyCode
        
    def keyup (self, event):
        self.keyCode = None 
        
exp = Experiment()  # Create and run game
