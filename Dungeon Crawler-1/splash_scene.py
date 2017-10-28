from scene import *
import ui
import time
import random
from globals import *
from map_scene import *
from class_select import *
from main_menu_scene import *
from inventory_scene import *

class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.touchedworld = 0
        self.start_time = time.time()
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
                                      position = self.size / 2,
                                      scale = 1,
                                      color = '#6f6f6f',
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        self.worldimg = SpriteNode('assets/SplashScene/world.PNG',
                                     position = self.size / 2,
                                     scale = 0.25,
                                     parent = self)
        
    def update(self):
        #this method is called, hopefully, 60 times a second
        if self.touchedworld == 1:
            if time.time() - self.start_time >= 1:
                self.touchedworld = 0
                self.present_modal_scene(ClassSelect())
        if globals.ClassSelected == 1:
            globals.ClassSelected = 0
            self.present_modal_scene(MainMenu())
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.worldimg.frame.contains_point(touch.location):
            self.start_time = time.time()
            self.worldimg.run_action(Action.scale_to(0, 1))
            self.worldimg.run_action(Action.rotate_by(3.2, 3))
            self.worldimg.run_action(Action.fade_to(0, 3))
            self.touchedworld = 1
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
