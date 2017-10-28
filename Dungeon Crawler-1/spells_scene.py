from random import *
from classes import *
from globals import *
from scene import *
import time
import console

class SpellsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
                                      position = self.size / 2,
                                      scale = 1,
                                      color = '#6f6f6f',
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        
        self.classtraitsbackground = SpriteNode('assets/MainMenu/gradient.JPG',
                                      position = (self.screen_center_x, self.size_of_screen_y),
                                      scale = 0.3,
                                      color = '#0088a0',
                                      size = (self.size_of_screen_x / 2.15, self.size_of_screen_y / 3),
                                      anchor_point = (0.5, 1),
                                      parent = self)
                                      
        self.classtraits = LabelNode(text = 'Traits',
                                      position = (self.screen_center_x, self.size_of_screen_y * 1.945 - self.size_of_screen_y),
                                      scale = 1,
                                      color = '#23ffe2',
                                      font = ('Papyrus', 25),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.classtraitsframe = SpriteNode('assets/Classes/frame-8-grey.png',
                                      position = (self.screen_center_x, self.size_of_screen_y),
                                      scale = 0.3,
                                      color = '#006274',
                                      size = (self.size_of_screen_x / 2.15, self.size_of_screen_y / 3),
                                      anchor_point = (0.5, 1),
                                      parent = self)
                                      
        self.Trait1Show = SpriteNode('assets/Classes/Mage/MageTrait1.PNG',
                                      position = (self.screen_center_x * 1.5 - self.screen_center_x, self.screen_center_y * 1.45),
                                      scale = 0.15,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait2Show = SpriteNode('assets/Classes/Mage/MageTrait2.PNG',
                                      position = (self.screen_center_x * 1.5, self.screen_center_y * 1.45),
                                      scale = 0.15,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait3Show = SpriteNode('assets/Classes/Mage/MageTrait3.PNG',
                                      position = (self.screen_center_x, self.screen_center_y * 1.15),
                                      scale = 0.15,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait4Show = SpriteNode('assets/Classes/Mage/MageTrait4.PNG',
                                      position = (self.screen_center_x, self.screen_center_y / 1.75),
                                      scale = 0.15,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait1Cover = SpriteNode(position = (self.screen_center_x * 1.5 - self.screen_center_x, self.screen_center_y * 1.45),
                                      scale = 1.25,
                                      alpha = 0,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
       
        self.Trait2Cover = SpriteNode(position = (self.screen_center_x * 1.5, self.screen_center_y * 1.45),
                                      scale = 1.25,
                                      alpha = 0,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait3Cover = SpriteNode(position = (self.screen_center_x, self.screen_center_y * 1.15),
                                      scale = 1.25,
                                      alpha = 0,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait4Cover = SpriteNode(position = (self.screen_center_x, self.screen_center_y / 1.75),
                                      scale = 1.25,
                                      alpha = 0,
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
                                      
        self.Trait1Text = LabelNode(text = str(globals.Trait1Curr) + ' / 3',
                                      position = (self.Trait1Show.position.x * 1.1965, self.Trait1Show.position.y / 1.1225),
                                      color = '#23ffe2',
                                      anchor_point = (0.5, 0.5),
                                      font = ('Papyrus', 16),
                                      parent = self)
        
        self.Trait2Text = LabelNode(text = str(globals.Trait2Curr) + ' / 3',
                                      position = (self.Trait2Show.position.x * 1.0665, self.Trait2Show.position.y / 1.1225),
                                      color = '#23ffe2',
                                      anchor_point = (0.5, 0.5),
                                      font = ('Papyrus', 16),
                                      parent = self)
        
        self.Trait3Text = LabelNode(text = str(globals.Trait3Curr) + ' / 1',
                                      position = (self.Trait3Show.position.x * 1.1, self.Trait3Show.position.y / 1.1575),
                                      color = '#23ffe2',
                                      font = ('Papyrus', 16),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        
        self.Trait4Text = LabelNode(text = str(globals.Trait4Curr) + ' / 1',
                                      position = (self.Trait4Show.position.x * 1.1, self.Trait4Show.position.y / 1.37525),
                                      color = '#23ffe2',
                                      font = ('Papyrus', 16),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
                                      
        if globals.Class == 'Mage':
            self.Trait1Show.texture = Texture('assets/Classes/Mage/MageTrait1.PNG')
            self.Trait2Show.texture = Texture('assets/Classes/Mage/MageTrait2.PNG')
            self.Trait3Show.texture = Texture('assets/Classes/Mage/MageTrait3.PNG')
            self.Trait4Show.texture = Texture('assets/Classes/Mage/MageTrait4.PNG')
        if globals.Class == 'Shaman':
            self.Trait1Show.texture = Texture('assets/Classes/Shaman/ShamanTrait1.PNG')
            self.Trait2Show.texture = Texture('assets/Classes/Shaman/ShamanTrait2.PNG')
            self.Trait3Show.texture = Texture('assets/Classes/Shaman/ShamanTrait3.PNG')
            self.Trait4Show.texture = Texture('assets/Classes/Shaman/ShamanTrait4.PNG')
            
    def update(self):
        #this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.Trait1Cover.frame.contains_point(touch.location):
            self.TouchTrait(globals.Class, 'one')
        if self.Trait2Cover.frame.contains_point(touch.location):
            self.TouchTrait(globals.Class, 'two')
        if self.Trait3Cover.frame.contains_point(touch.location):
            if globals.Trait1Curr == 3 or globals.Trait2Curr == 3:
                self.TouchTrait(globals.Class, 'three')
        if self.Trait4Cover.frame.contains_point(touch.location):
            if globals.Trait3Curr == 1:
                self.TouchTrait(globals.Class, 'four')
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
        
    def TouchTrait(self, Class, Trait):
        if Trait == 'one':
            self.Current = globals.Trait1Curr
            self.Interval = 3
            if Class == 'Mage':
                self.MaxTraitAmount = trait1Mage*3
                self.Sentence = 'You have a small chance to gain a charge of ice when you damage an enemy. When you collect 10 charges, you will explode killing all enemies in a 15ft range.'
            if Class == 'Shaman':
                self.MaxTraitAmount = trait1Shaman*3
                self.Sentence = 'A significant chance when attacked to heal yourself for 60% of the damage taken in the past 5 seconds, over 2 seconds.'
                
            
            
            
            
            self.Heading = '[ Trait ' + str(Trait) + ' ]\nMaximum - ' + str(self.MaxTraitAmount) + '%\nCurrent - ' + str(globals.T1A) + '%'
        if Trait == 'two':
            self.Current = globals.Trait2Curr
            self.Interval = 3
            if Class == 'Mage':
                self.MaxTraitAmount = trait2Mage*3
                self.Sentence = 'Increase your versatility significantly.'
            if Class == 'Shaman':
                self.MaxTraitAmount = trait2Shaman*3
                self.Sentence = 'Increase your maximum health significantly.'
            
            
            
            
            self.Heading = '[ Trait ' + str(Trait) + ' ]\nMaximum - ' + str(self.MaxTraitAmount) + '%\nCurrent - ' + str(globals.T2A) + '%'
        if Trait == 'three':
            self.Current = globals.Trait3Curr
            self.Interval = 1
            if Class == 'Mage':
                self.Sentence = 'A chance to deal additional damage when you hit an enemy.'
            if Class == 'Shaman':
                self.Sentence = 'When you deal damage, there is a small chance to call on the aspect of the wolf, granting a 20% increased damage buff for 5 seconds.'
            
            
            
            self.Heading = '[ Trait ' + str(Trait) + ' ]'
        if Trait == 'four':
            self.Current = globals.Trait4Curr
            self.Interval = 1
            if Class == 'Mage':
                self.Sentence = 'Slow the attack and movement speed of enemies that touch you for a short duration. When you slow an enemy that is not already affected by movement impairing effects, you will heal yourself.'
            if Class == 'Shaman':
                self.Sentence = 'When you take damage, there is a small chance to call on the aspect of the bear, granting 20% reduced damage taken for 5 seconds.'
            
            self.Heading = '[ Trait ' + str(Trait) + ' ]'
        globals.UpgradeTraitCost = 1000 + (450 * globals.Trait1Curr) + (450 * globals.Trait2Curr) + (2350 * globals.Trait3Curr)
        if self.Current == self.Interval:
            self.TraitPopUp = console.alert(self.Heading, self.Sentence)
        else:
            self.TraitPopUp = console.alert(self.Heading, self.Sentence, 'Purchase [$' + str(globals.UpgradeTraitCost) + ']')
        if self.TraitPopUp == 1:
            if globals.Coins >= globals.UpgradeTraitCost:
                globals.Coins = globals.Coins - globals.UpgradeTraitCost
                if Trait == 'one':
                    globals.Trait1Curr = globals.Trait1Curr + 1
                    globals.T1A = globals.T1A + self.MaxTraitAmount/3
                    self.Trait1Text.text = str(globals.Trait1Curr) + ' / 3'
                if Trait == 'two':
                    globals.Trait2Curr = globals.Trait2Curr + 1
                    globals.T2A = globals.T2A + self.MaxTraitAmount/3
                    self.Trait2Text.text = str(globals.Trait2Curr) + ' / 3'
                if Trait == 'three':
                    globals.Trait3Curr = globals.Trait3Curr + 1
                    globals.T3A = globals.T3A + self.MaxTraitAmount
                    self.Trait3Text.text = str(globals.Trait3Curr) + ' / 1'
                if Trait == 'four':
                    globals.Trait4Curr = globals.Trait4Curr + 1
                    globals.T4A = globals.T4A + self.MaxTraitAmount
                    self.Trait4Text.text = str(globals.Trait4Curr) + ' / 1'
            
