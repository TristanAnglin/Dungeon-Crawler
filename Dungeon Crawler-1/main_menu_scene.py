from scene import *
from splash_scene import *
from globals import *
from classes import *
from inventory_scene import *
from spells_scene import *
from map_scene import *
from settings_scene import *
import ui

class MainMenu(Scene):
    def setup(self):
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.background = SpriteNode('assets/MainMenu/background.JPG',
                                      position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        
        
        self.basebar = SpriteNode('assets/MainMenu/gradient.JPG',
                                      position = (self.size_of_screen_x, 0),
                                      scale = 1,
                                      color = '#5f5f5f',
                                      size = (self.screen_center_x / 1.675, self.size_of_screen_y / 10),
                                      parent = self,
                                      anchor_point = (1, 0))
                                      
        
        self.inventoryicon = SpriteNode('assets/Icons/backpack.png',
                                      position = (self.size_of_screen_x, self.size_of_screen_y * 1.1 - self.size_of_screen_y),
                                      scale = 0.155,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.inventoryiconframe = SpriteNode('assets/Classes/frame-8-grey.png',
                                      position = (self.inventoryicon.position.x, self.inventoryicon.position.y),
                                      scale = 0.3,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.spellsicon = SpriteNode('assets/Icons/tome.png',
                                      position = (self.size_of_screen_x / 1.175, self.size_of_screen_y * 1.1 - self.size_of_screen_y),
                                      scale = 0.145,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.spellsiconframe = SpriteNode('assets/Classes/frame-8-grey.png',
                                      position = (self.spellsicon.position.x, self.inventoryicon.position.y),
                                      scale = 0.3,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.mapicon = SpriteNode('assets/Icons/map.png',
                                      position = (self.size_of_screen_x / 1.08, self.size_of_screen_y * 1.1 - self.size_of_screen_y),
                                      scale = 0.1425,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.mapiconframe = SpriteNode('assets/Classes/frame-8-grey.png',
                                      position = (self.mapicon.position.x, self.inventoryicon.position.y),
                                      scale = 0.3,
                                      parent = self,
                                      anchor_point = (1, 1))
        
        self.settingsicon = SpriteNode('assets/Icons/tools.png',
                                      position = (self.size_of_screen_x / 1.2875, self.size_of_screen_y * 1.1 - self.size_of_screen_y),
                                      scale = 0.155,
                                      parent = self,
                                      anchor_point = (1, 1))
                                      
        self.settingsiconframe = SpriteNode('assets/Classes/frame-8-grey.png',
                                      position = (self.settingsicon.position.x, self.inventoryicon.position.y),
                                      scale = 0.3,
                                      parent = self,
                                      anchor_point = (1, 1))

        self.NameAndClassDisplay = LabelNode(text = str(globals.Class) + ', ' + str(globals.Name),
                                      position = (0, 0),
                                      scale = 1,
                                      color = '#b3b3b3',
                                      font = ('Papyrus', 20),
                                      parent = self,
                                      anchor_point = (0, 0))
        
        self.CoinDisplay = LabelNode(text = '$' + str(globals.Coins),
                                      position = (0, self.size_of_screen_y * 1.0375 - self.size_of_screen_y),
                                      scale = 1,
                                      color = '#eac130',
                                      font = ('Papyrus', 20),
                                      parent = self,
                                      anchor_point = (0, 0))
                                      
        self.GemShardDisplay = LabelNode(text = str(globals.GemShards) + '*',
                                      position = (0, self.size_of_screen_y * 1.075 - self.size_of_screen_y),
                                      scale = 1,
                                      color = (.49, .0, .71),
                                      font = ('Papyrus', 20),
                                      parent = self,
                                      anchor_point = (0, 0))
                                      
                                      
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.CoinDisplay.text = '$' + str(globals.Coins)
        self.GemShardDisplay.text = str(globals.GemShards) + '*'
        # after 2 seconds, move to main menu scene
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.inventoryicon.frame.contains_point(touch.location) or self.inventoryiconframe.frame.contains_point(touch.location):
            run(InventoryScene(), LANDSCAPE)
        if self.spellsicon.frame.contains_point(touch.location) or self.spellsiconframe.frame.contains_point(touch.location):
            run(SpellsScene(), LANDSCAPE)
        if self.mapicon.frame.contains_point(touch.location) or self.mapiconframe.frame.contains_point(touch.location):
            run(MapScene(), LANDSCAPE)
        if self.settingsicon.frame.contains_point(touch.location) or self.settingsiconframe.frame.contains_point(touch.location):
            run(SettingsScene(), LANDSCAPE)
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
