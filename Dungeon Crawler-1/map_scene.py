from random import *
from classes import *
from globals import *
from scene import *
from Dungeons import *
import time

class MapScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.DungeonSize1 = 0
        self.DungeonSize2 = 0
        self.Touch1 = 0
        self.Touch2 = 0
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.background = SpriteNode('assets/Icons/woodback.PNG',
                                      position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        self.Dungeon1 = SpriteNode('assets/Icons/Dungeon1Icon.PNG',
                                      position = (self.size_of_screen_x * 1.15 - self.size_of_screen_x, self.size_of_screen_y * 1.15 - self.size_of_screen_y),
                                      scale = 0.2,
                                      parent = self)
        
        self.Dungeon2 = SpriteNode('assets/Icons/Dungeon2Icon.PNG',
                                      position = (self.size_of_screen_x * 1.285 - self.size_of_screen_x, self.size_of_screen_y * 1.475 - self.size_of_screen_y),
                                      scale = 0.2,
                                      parent = self)
        
                                      
    def update(self):
        #this method is called, hopefully, 60 times a second
        #if globals.Dungeon1 == 1:
            #self.dismiss_modal_scene()
        #if globals.Dungeon2 == 1:
            #self.dismiss_modal_scene()
            pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.DungeonSize1 == 0 and self.Touch2 == 0:
            if self.Dungeon1.frame.contains_point(touch.location):
                self.Dungeon1.scale = self.Dungeon1.scale * 1.2
                self.DungeonSize1 = 1
                self.Touch1 = 1
        if self.DungeonSize2 == 0 and self.Touch1 == 0:
            if self.Dungeon2.frame.contains_point(touch.location):
                self.Dungeon2.scale = self.Dungeon2.scale * 1.2
                self.DungeonSize2 = 1
                self.Touch2 = 1
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if not self.Dungeon1.frame.contains_point(touch.location):
            self.Touch1 = 0
        if not self.Dungeon2.frame.contains_point(touch.location):
            self.Touch2 = 0
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.Touch1 == 1:
            self.present_modal_scene(Dungeons())
            globals.Dungeon1 = 1
        if self.Touch2 == 1:
            self.present_modal_scene(Dungeons())
            globals.Dungeon2 = 1
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
