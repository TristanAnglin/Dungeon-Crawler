from random import *
from classes import *
from globals import *
from map_scene import *
from scene import *
from inventory_scene import *
import time

class GemUse(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.Framing = []
        self.Back = []
        self.Item = []
        self.Frame = []
        self.Text = []
        self.EligibleGemUse = []
        self.checking = 0
        for items in globals.Inventory:
            if items.Type == 'Helmet' or items.Type == 'Chestplate' or items.Type == 'Weapon' or items.Type == 'Offhand':
                if items.NumOfSockets > 0:
                    self.EligibleGemUse.append(items)
        for items in globals.EquippedSlot1:
            if items.NumOfSockets > 0:
                self.EligibleGemUse.append(items)
        for items in globals.EquippedSlot2:
            if items.NumOfSockets > 0:
                self.EligibleGemUse.append(items)
        for items in globals.EquippedSlot3:
            if items.NumOfSockets > 0:
                self.EligibleGemUse.append(items)
        for items in globals.EquippedSlot4:
            if items.NumOfSockets > 0:
                self.EligibleGemUse.append(items)
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
            	                        position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        for DrawFrames in range(7):
            self.Framing.append(SpriteNode('assets/MainMenu/gradient.JPG',
                                      position = (self.screen_center_x * 1.45 - self.screen_center_x, self.screen_center_y),
                                      scale = 0.5 * 0.4,
                                      parent = self,
                                      color = (.9, .9, .9), 
                                      alpha = 0))
        
            self.Back.append(SpriteNode('assets/MainMenu/gradient.JPG',
                                      position = (self.screen_center_x * 1.45 - self.screen_center_x, self.screen_center_y),
                                      scale = 0.5 * 0.4,
                                      parent = self,
                                      color = (.9, .9, .9), 
                                      alpha = 0))
        
            self.Item.append(SpriteNode(position = (self.screen_center_x * 1.45 - self.screen_center_x, self.screen_center_y),
                                      scale = 0.5,
                                      parent = self,
                                      color = (.9, .9, .9), 
                                      alpha = 0))
        
            self.Frame.append(SpriteNode(position = (self.screen_center_x * 1.45 - self.screen_center_x, self.screen_center_y),
                                      scale = 0.5,
                                      parent = self,
                                      color = (.9, .9, .9), 
                                      alpha = 0))
        
            self.Text.append(LabelNode(position = (self.screen_center_x * 1.45 - self.screen_center_x, self.screen_center_y),
                                      text = 'Sup\n\n',
                                      scale = 1,
                                      font = ('CopperPlate', 12),
                                      parent = self,
                                      color = ('#00ffd8'), 
                                      alpha = 0))
                                      
        if len(self.EligibleGemUse) > 0:
            self.setupitems(self.Frame[0], self.Back[0], self.Item[0], 0, 0.5)
        if len(self.EligibleGemUse) > 1:
            self.setupitems(self.Frame[1], self.Back[1], self.Item[1], 1, 0.75)
        if len(self.EligibleGemUse) > 2:
            self.setupitems(self.Frame[2], self.Back[2], self.Item[2], 2, 0.9)
        if len(self.EligibleGemUse) > 3:
            self.setupitems(self.Frame[3], self.Back[3], self.Item[3], 3, 1)
        if len(self.EligibleGemUse) > 4:
            self.setupitems(self.Frame[4], self.Back[4], self.Item[4], 4, 0.9)
        if len(self.EligibleGemUse) > 5:
            self.setupitems(self.Frame[5], self.Back[5], self.Item[5], 5, 0.75)
        if len(self.EligibleGemUse) > 6:
            self.setupitems(self.Frame[6], self.Back[6], self.Item[6], 6, 0.5)
        
    def update(self):
        #this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        self.TouchStart = touch.location.x
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if self.TouchStart < touch.location.x:
            pass
        if self.TouchStart > touch.location.x:
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
        
    def setupitems(self, Which, WhichBack, WhichItem, Slot, WhichScale):
        Which.texture = Texture('assets/Classes/frame-8-grey.png')
        Which.alpha = 1
        Which.scale = (0.4 * WhichScale)
        WhichBack.size = Which.size
        WhichBack.scale = Which.scale
        WhichBack.alpha = 1
        WhichBack.color = self.EligibleGemUse[Slot].ItemColor
        if self.EligibleGemUse[Slot].Type == 'Helmet':
            WhichItem.texture = Texture('assets/Icons/helmet.png')
        if self.EligibleGemUse[Slot].Type == 'Chestplate':
            WhichItem.texture = Texture('assets/Icons/armor.png')
        if self.EligibleGemUse[Slot].Type == 'Weapon':
            WhichItem.texture = Texture(self.EligibleGemUse[Slot].Image)
        if self.EligibleGemUse[Slot].Type == 'Offhand':
            WhichItem.texture = Texture('assets/Icons/shieldSmall.png')
        WhichItem.size = Which.size
        WhichItem.scale = Which.scale
        WhichItem.alpha = 1
        
    def MovingItems(self, WhichSlot, WhichDirection, WhichAmount, Time):
        
            if WhichDirection == '+':
                self.Frame[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Frame[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Back[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Back[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Item[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Item[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Text[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Text[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
            elif WhichDirection == '-':
                self.Frame[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Frame[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Back[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Back[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Item[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Item[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
                self.Text[WhichSlot].run_action(Action.move_to(self.Framing[WhichAmount].position.x, self.Framing[WhichAmount].position.y, Time))
                self.Text[WhichSlot].run_action(Action.scale_to(self.Framing[WhichAmount].scale, Time))
        
