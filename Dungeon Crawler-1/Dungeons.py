from random import *
from classes import *
from globals import *
from map_scene import *
from scene import *
import time

class Dungeons(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.dungeon1setup = 0
        self.dungeon2setup = 0
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
            	                        position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        
    def update(self):
        #this method is called, hopefully, 60 times a second
        if globals.Dungeon1 == 1 and self.dungeon1setup == 0:
            self.dungeon1settingup()
            self.dungeon1setup = 1
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def dungeon1settingup(self):
        self.Tile1 = SpriteNode('assets/GameScene/base1.PNG',
            	                        position = self.size / 2,
                                      scale = 0.35,
                                      parent = self)
                                      
        self.Tile2Left = SpriteNode('assets/GameScene/base1.PNG',
            	                        position = (self.Tile1.position.x / 1.2125, self.Tile1.position.y / 1.1575),
                                      scale = 0.35,
                                      parent = self)
                                      
        self.Tile3Left = SpriteNode('assets/GameScene/base1.PNG',
            	                        position = (self.Tile2Left.position.x / (1.2125 + 0.0575), self.Tile2Left.position.y / (1.1575 + 0.0305)),
                                      scale = 0.35,
                                      parent = self)
        
        self.Tile4Left = SpriteNode('assets/GameScene/base1.PNG',
            	                        position = (self.Tile3Left.position.x / (1.2125 + 0.157), self.Tile3Left.position.y / (1.1575 + 0.0745)),
                                      scale = 0.35,
                                      parent = self)
        
        
                                      
