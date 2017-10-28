import console
from scene import *
from classes import *
from splash_scene import *
from main_menu_scene import *
from globals import *
import ui

class ClassSelect(Scene):
    def setup(self):
        globals.Name = console.input_alert('Please enter your\ndesired username.', 'Your username must be between\n2-8 characters long.', '', 'Confirm', True)
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.classicons = []
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
                                      position = self.size / 2,
                                      scale = 1,
                                      color = '#6f6f6f',
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        self.title = LabelNode(text = 'Class Selection',
                                      position = (self.screen_center_x, self.screen_center_y * 1.9),
                                      color = '#ffffff',
                                      scale = 1,
                                      anchor_point = (0.5, 0),
                                      font = ('CopperPlate-Bold', 25),
                                      parent = self)
        self.selectclass = LabelNode(text = 'Select',
                                      position = (self.screen_center_x, self.screen_center_y * 1.675),
                                      color = '#ffffff',
                                      scale = 0,
                                      anchor_point = (0.5, 0),
                                      font = ('CopperPlate-Bold', 25),
                                      parent = self)
                                      
        self.classmelee = LabelNode(text = 'Melee',
                                      position = (self.screen_center_x * 1.65, self.screen_center_y * 1.9),
                                      color = '#ffffff',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        
        self.classranged = LabelNode(text = 'Ranged',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.9),
                                      color = '#ffffff',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.magebackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.75),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.mage = LabelNode(text = 'Mage',
                                      position = (self.magebackground.position.x, self.magebackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.shamanbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.6),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.shaman = LabelNode(text = 'Shaman',
                                      position = (self.shamanbackground.position.x, self.shamanbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        
        self.warlockbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.45),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.warlock = LabelNode(text = 'Warlock',
                                      position = (self.warlockbackground.position.x, self.warlockbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.druidbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.3),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.druid = LabelNode(text = 'Druid',
                                      position = (self.druidbackground.position.x, self.druidbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.paladinbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.screen_center_x * 1.65), self.screen_center_y * 1.75),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.paladin = LabelNode(text = 'Paladin',
                                      position = (self.paladinbackground.position.x / 1.005, self.paladinbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.deathknightbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.screen_center_x * 1.65), self.screen_center_y * 1.6),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.deathknight = LabelNode(text = 'DeathKnight',
                                      position = (self.deathknightbackground.position.x / 1.005, self.deathknightbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
                                      
        self.monkbackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.screen_center_x * 1.65), self.screen_center_y * 1.45),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.monk = LabelNode(text = 'Monk',
                                      position = (self.monkbackground.position.x / 1.005, self.monkbackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.roguebackground = SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.screen_center_x * 1.65), self.screen_center_y * 1.3),
                                      scale = 1.3,
                                      size = (self.classranged.size.x * 3, self.classranged.size.y * 2.5),
                                      anchor_point = (0.5, 0.5),
                                      parent = self)
        self.rogue = LabelNode(text = 'Rogue',
                                      position = (self.roguebackground.position.x / 1.005, self.roguebackground.position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('CopperPlate-Bold', 20),
                                      parent = self)
        self.TraitsDisplay = LabelNode(text = '',
                                      position = ((self.size_of_screen_x * 1.05 - self.size_of_screen_x), self.screen_center_y * 1.15),
                                      color = '#23ffe2',
                                      scale = 0.925,
                                      anchor_point = (0, 1),
                                      font = ('Papyrus', 20),
                                      parent = self)
                                      
        self.classicons = (SpriteNode('shp:BlackSmoke00',
                                     position = (self.screen_center_x, self.screen_center_y * 1.55),
                                     scale = 0.4,
                                     alpha = 0,
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
                                     
        self.classiconsframe = (SpriteNode('assets/Classes/frame-8-grey.png',
                                     position = (self.screen_center_x, self.screen_center_y * 1.55),
                                     scale = 0,
                                     alpha = 1,
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
                                     
        self.classmainstattitle = (LabelNode(text = '',
                                     position = (self.screen_center_x, self.screen_center_y * 1.375),
                                     scale = 1,
                                     alpha = 1,
                                     color = '#ffffff',
                                     font = ('CopperPlate-Bold', 15),
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
                                     
        self.classmainresourcetitle = (LabelNode(text = '',
                                     position = (self.screen_center_x, self.screen_center_y * 1.275),
                                     scale = 1,
                                     alpha = 1,
                                     color = '#ffffff',
                                     font = ('CopperPlate-Bold', 15),
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
                                     
        self.classmainstat = (LabelNode(text = '',
                                     position = (self.screen_center_x, self.screen_center_y * 1.32),
                                     scale = 1,
                                     alpha = 1,
                                     color = '#23ffe2',
                                     font = ('Papyrus', 15),
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
                                     
        self.classmainresource = (LabelNode(text = '',
                                     position = (self.screen_center_x, self.screen_center_y * 1.225),
                                     scale = 1,
                                     alpha = 1,
                                     color = '#23ffe2',
                                     font = ('Papyrus', 15),
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        if len(globals.Name) < 2 or len(globals.Name) > 8:
            globals.Name = 'oooo'
            globals.Name = console.input_alert('Please enter your username.', 'Keep the length between 2-8', '', 'Confirm', True)
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
                
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.classicons.frame.contains_point(touch.location) or self.classiconsframe.frame.contains_point(touch.location):
            globals.ClassSelected = 1
            self.dismiss_modal_scene()
        if self.mage.frame.contains_point(touch.location) or self.magebackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Mage/MagePassive.png')
            self.classmainstat.text = str(MainStatMage)
            self.classmainresource.text = str(ResourceMage)
            self.mage.color = '#009bff'
            globals.Class = 'Mage'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionMage) + str('\n\nTrait two: \n') + str(trait2descriptionMage) + str('\n\nTrait three: \n') + str(trait3descriptionMage) + str('\n\nTrait four: \n') + str(trait4descriptionMage))
        if self.warlock.frame.contains_point(touch.location) or self.warlockbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Warlock/WarlockPassive.png')
            globals.Class = 'Warlock'
            self.classmainstat.text = str(MainStatWarlock)
            self.classmainresource.text = str(ResourceWarlock)
            self.warlock.color = '#009bff'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionWarlock) + str('\n\nTrait two: \n') + str(trait2descriptionWarlock) + str('\n\nTrait three: \n') + str(trait3descriptionWarlock) + str('\n\nTrait four: \n') + str(trait4descriptionWarlock))
        if self.druid.frame.contains_point(touch.location) or self.druidbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Druid/DruidPassive.png')
            globals.Class = 'Druid'
            self.classmainstat.text = str(MainStatDruid)
            self.classmainresource.text = str(ResourceDruid)
            self.druid.color = '#009bff'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionDruid) + str('\n\nTrait two: \n') + str(trait2descriptionDruid) + str('\n\nTrait three: \n') + str(trait3descriptionDruid) + str('\n\nTrait four: \n') + str(trait4descriptionDruid))
        if self.shaman.frame.contains_point(touch.location) or self.shamanbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Shaman/ShamanPassive.png')
            globals.Class = 'Shaman'
            self.classmainstat.text = str(MainStatShaman)
            self.classmainresource.text = str(ResourceShaman)
            self.shaman.color = '#009bff'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionShaman) + str('\n\nTrait two: \n') + str(trait2descriptionShaman) + str('\n\nTrait three: \n') + str(trait3descriptionShaman) + str('\n\nTrait four: \n') + str(trait4descriptionShaman))
        if self.monk.frame.contains_point(touch.location) or self.monkbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Monk/MonkPassive.png')
            globals.Class = 'Monk'
            self.classmainstat.text = str(MainStatMonk)
            self.classmainresource.text = str(ResourceMonk)
            self.monk.color = '#009bff'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionMonk) + str('\n\nTrait two: \n') + str(trait2descriptionMonk) + str('\n\nTrait three: \n') + str(trait3descriptionMonk) + str('\n\nTrait four: \n') + str(trait4descriptionMonk))
        if self.rogue.frame.contains_point(touch.location) or self.roguebackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Rogue/RoguePassive.png')
            globals.Class = 'Rogue'
            self.rogue.color = '#009bff'
            self.classmainstat.text = str(MainStatRogue)
            self.classmainresource.text = str(ResourceRogue)
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionRogue) + str('\n\nTrait two: \n') + str(trait2descriptionRogue) + str('\n\nTrait three: \n') + str(trait3descriptionRogue) + str('\n\nTrait four: \n') + str(trait4descriptionRogue))
        if self.deathknight.frame.contains_point(touch.location) or self.deathknightbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/DeathKnight/DeathKnightPassive.png')
            self.classmainstat.text = str(MainStatDeathKnight)
            self.classmainresource.text = str(ResourceDeathKnight)
            self.deathknight.color = '#009bff'
            globals.Class = 'Death Knight'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionDeathKnight) + str('\n\nTrait two: \n') + str(trait2descriptionDeathKnight) + str('\n\nTrait three: \n') + str(trait3descriptionDeathKnight) + str('\n\nTrait four: \n') + str(trait4descriptionDeathKnight))
        if self.paladin.frame.contains_point(touch.location) or self.paladinbackground.frame.contains_point(touch.location):
            self.blacktext()
            self.classicons.texture = Texture('assets/Classes/Paladin/PaladinPassive.png')
            self.paladin.color = '#009bff'
            self.classmainstat.text = str(MainStatPaladin)
            self.classmainresource.text = str(ResourcePaladin)
            globals.Class = 'Paladin'
            self.TraitsDisplay.text = (str('Trait one: \n') + str(trait1descriptionPaladin) + str('\n\nTrait two: \n') + str(trait2descriptionPaladin) + str('\n\nTrait three: \n') + str(trait3descriptionPaladin) + str('\n\nTrait four: \n') + str(trait4descriptionPaladin))
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
        
    def blacktext(self):
        self.paladin.color = 'black'
        self.druid.color = 'black'
        self.rogue.color = 'black'
        self.deathknight.color = 'black'
        self.monk.color = 'black'
        self.warlock.color = 'black'
        self.shaman.color = 'black'
        self.mage.color = 'black'
        self.classiconsframe.scale = 0.4
        self.selectclass.scale = 1
        self.classmainresourcetitle.text = 'Resource'
        self.classmainstattitle.text = 'Primary stat'
        self.classicons.alpha = 1
    
