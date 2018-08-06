import console
from scene import *
from classes import *
from splash_scene import *
from main_menu_scene import *
from globals import *
import ui

class ClassSelect(Scene):
    def setup(self):
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.Titles = []
        self.ClassTitles = []
        self.ClassBackgrounds = []
        self.ClassIcons = []
        self.background = SpriteNode('assets/SplashScene/spacebackground.JPG',
                                      position = self.size / 2,
                                      scale = 1,
                                      color = '#6f6f6f',
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
        for titles in range(6):
            self.Titles.append(SpriteNode('assets/Classes/ClassSelection.PNG',
                                      position = (self.screen_center_x, self.screen_center_y * 1.9),
                                      scale = 0.3,
                                      anchor_point = (0.5, 0),
                                      parent = self))
        self.TitleAttributes(1, 0, 1, (self.screen_center_x, self.screen_center_y * 1.675), 'assets/Classes/Select.PNG', (0.5, 0))
        self.TitleAttributes(2, 0.25, 1, (self.screen_center_x * 1.65, self.screen_center_y * 1.9), 'assets/Classes/Melee.PNG', (0.5, 0.5))
        self.TitleAttributes(3, 0.25, 1, (self.size_of_screen_x * 1.175 - self.size_of_screen_x, self.screen_center_y * 1.9), 'assets/Classes/Ranged.PNG', (0.5, 0.5))
        self.TitleAttributes(4, 0.175, 0, (self.screen_center_x, self.screen_center_y * 1.375), 'assets/Classes/PrimaryStat.PNG', (0.5, 0.5))
        self.TitleAttributes(5, 0.175, 0, (self.screen_center_x, self.screen_center_y * 1.275), 'assets/Classes/Resource.PNG', (0.5, 0.5))
        
        self.Backsize = (self.Titles[3].size.x / 2.1, self.Titles[3].size.y / 2.65)
        
        for classbackgrounds in range(8):
            #Mage
            self.ClassBackgrounds.append(SpriteNode('assets/SplashScene/backgroundtext.PNG',
                                      position = ((self.size_of_screen_x * 1.175 - self.size_of_screen_x), self.screen_center_y * 1.775),
                                      scale = 1.3,
                                      size = (self.Backsize),
                                      anchor_point = (0.5, 0.5),
                                      parent = self))
        #Shaman
        self.ClassBackgroundAttributes(1, (self.size_of_screen_x * 1.175 - self.size_of_screen_x, self.screen_center_y * 1.6))
        #Witch Doctor
        self.ClassBackgroundAttributes(2, (self.size_of_screen_x * 1.175 - self.size_of_screen_x, self.screen_center_y * 1.425))
        #Druid
        self.ClassBackgroundAttributes(3, (self.size_of_screen_x * 1.175 - self.size_of_screen_x, self.screen_center_y * 1.25))
        #Paladin
        self.ClassBackgroundAttributes(4, (self.screen_center_x * 1.65, self.screen_center_y * 1.775))
        #Death Knight
        self.ClassBackgroundAttributes(5, (self.screen_center_x * 1.65, self.screen_center_y * 1.6))
        #Monk
        self.ClassBackgroundAttributes(6, (self.screen_center_x * 1.65, self.screen_center_y * 1.425))
        #Rogue
        self.ClassBackgroundAttributes(7, (self.screen_center_x * 1.65, self.screen_center_y * 1.25))
        
        for classtitles in range(13):
            self.ClassTitles.append(LabelNode(text = 'Mage',
                                      position = (self.ClassBackgrounds[0].position.x, self.ClassBackgrounds[0].position.y * 1.025),
                                      color = '#000000',
                                      scale = 1,
                                      anchor_point = (0.5, 0.5),
                                      font = ('Bodoni 72', 20),
                                      parent = self))
        self.ClassTitleAttributes(1, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[1].position.x, self.ClassBackgrounds[1].position.y * 1.025), 'Shaman')
        self.ClassTitleAttributes(2, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[2].position.x, self.ClassBackgrounds[2].position.y * 1.025), 'Witch Doctor')
        self.ClassTitleAttributes(3, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[3].position.x, self.ClassBackgrounds[3].position.y * 1.025), 'Druid')
        self.ClassTitleAttributes(4, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[4].position.x, self.ClassBackgrounds[4].position.y * 1.025), 'Paladin')
        self.ClassTitleAttributes(5, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[5].position.x, self.ClassBackgrounds[5].position.y * 1.025), 'Death Knight')
        self.ClassTitleAttributes(6, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[6].position.x, self.ClassBackgrounds[6].position.y * 1.025), 'Monk')
        self.ClassTitleAttributes(7, '#000000', ('Bodoni 72', 20), (self.ClassBackgrounds[7].position.x, self.ClassBackgrounds[7].position.y * 1.025), 'Rogue')
        self.ClassTitleAttributes(8, '#73d8e7', ('Bodoni 72', 17), (self.screen_center_x, self.screen_center_y * 1.33), '')
        self.ClassTitleAttributes(9, '#73d8e7', ('Bodoni 72', 17), (self.screen_center_x, self.screen_center_y * 1.225), '')
        self.ClassTitleAttributes(10, '#73d8e7', ('Bodoni 72', 20), (self.size_of_screen_x * 1.05 - self.size_of_screen_x, self.screen_center_y * 1.15), '')
        self.ClassTitleAttributes(11, '#73d8e7', ('Bodoni 72', 17), (self.screen_center_x / 1.325, self.screen_center_y * 1.6), '')
        self.ClassTitleAttributes(12, '#73d8e7', ('Bodoni 72', 17), (self.screen_center_x * 1.25, self.screen_center_y * 1.6), '')
        self.ClassTitles[10].anchor_point = (0,1)
        self.ClassTitles[11].anchor_point = (0.5,1)
        self.ClassTitles[12].anchor_point = (0.5,1)
        
        for classicons in range(2):
            self.ClassIcons.append(SpriteNode('shp:BlackSmoke00',
                                     position = (self.screen_center_x, self.screen_center_y * 1.55),
                                     scale = 0.4,
                                     alpha = 0,
                                     anchor_point = (0.5, 0.5),
                                     parent = self))
        self.ClassIconsAttributes(1, 'assets/Classes/frame-8-grey.png', 0, 1)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
                
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.ClassIcons[0].frame.contains_point(touch.location) or self.ClassIcons[1].frame.contains_point(touch.location):
            globals.ClassSelected = 1
            self.dismiss_modal_scene()
        self.CheckWhichClass(touch, 'Mage', self.ClassTitles[0], self.ClassBackgrounds[0], '#80cdff', LeftStatsMage, RightStatsMage, 'assets/Classes/Mage/MagePassive.png', MainStatMage, ResourceMage, trait1descriptionMage, trait2descriptionMage, trait3descriptionMage, trait4descriptionMage)
        
        self.CheckWhichClass(touch, 'Shaman', self.ClassTitles[1], self.ClassBackgrounds[2], '#80ffcd', LeftStatsShaman, RightStatsShaman, 'assets/Classes/Shaman/ShamanPassive.png', MainStatShaman, ResourceShaman, trait1descriptionShaman, trait2descriptionShaman, trait3descriptionShaman, trait4descriptionShaman)
        
        self.CheckWhichClass(touch, 'Witch Doctor', self.ClassTitles[2], self.ClassBackgrounds[2], '#cfaaff', LeftStatsWitchDoctor, RightStatsWitchDoctor, 'assets/Classes/WitchDoctor/WitchDoctorPassive.png', MainStatWitchDoctor, ResourceWitchDoctor, trait1descriptionWitchDoctor, trait2descriptionWitchDoctor, trait3descriptionWitchDoctor, trait4descriptionWitchDoctor)
        
        self.CheckWhichClass(touch, 'Druid', self.ClassTitles[3], self.ClassBackgrounds[3], '#96ff80', LeftStatsDruid, RightStatsDruid, 'assets/Classes/Druid/DruidPassive.png', MainStatDruid, ResourceDruid, trait1descriptionDruid, trait2descriptionDruid, trait3descriptionDruid, trait4descriptionDruid)
        
        self.CheckWhichClass(touch, 'Paladin', self.ClassTitles[4], self.ClassBackgrounds[4], '#ff80c2', LeftStatsPaladin, RightStatsPaladin, 'assets/Classes/Paladin/PaladinPassive.png', MainStatPaladin, ResourcePaladin, trait1descriptionPaladin, trait2descriptionPaladin, trait3descriptionPaladin, trait4descriptionPaladin)
        
        self.CheckWhichClass(touch, 'Death Knight', self.ClassTitles[5], self.ClassBackgrounds[5], '#ff5555', LeftStatsDeathKnight, RightStatsDeathKnight, 'assets/Classes/DeathKnight/DeathKnightPassive.png', MainStatDeathKnight, ResourceDeathKnight, trait1descriptionDeathKnight, trait2descriptionDeathKnight, trait3descriptionDeathKnight, trait4descriptionDeathKnight)
        
        self.CheckWhichClass(touch, 'Monk', self.ClassTitles[6], self.ClassBackgrounds[6], '#d5f9ff', LeftStatsMonk, RightStatsMonk, 'assets/Classes/Monk/MonkPassive.png', MainStatMonk, ResourceMonk, trait1descriptionMonk, trait2descriptionMonk, trait3descriptionMonk, trait4descriptionMonk)
        
        self.CheckWhichClass(touch, 'Rogue', self.ClassTitles[7], self.ClassBackgrounds[7], '#ff8500', LeftStatsRogue, RightStatsRogue, 'assets/Classes/Rogue/RoguePassive.png', MainStatRogue, ResourceRogue, trait1descriptionRogue, trait2descriptionRogue, trait3descriptionRogue, trait4descriptionRogue)
        
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
        
    def BlackText(self):
        self.ClassTitles[0].color = 'black'
        self.ClassTitles[1].color = 'black'
        self.ClassTitles[2].color = 'black'
        self.ClassTitles[3].color = 'black'
        self.ClassTitles[4].color = 'black'
        self.ClassTitles[5].color = 'black'
        self.ClassTitles[6].color = 'black'
        self.ClassTitles[7].color = 'black'
        self.ClassIcons[1].scale = 0.4
        self.Titles[1].scale = 0.3
        self.Titles[4].alpha = 1
        self.Titles[5].alpha = 1
        self.ClassIcons[0].alpha = 1
    
    def TitleAttributes(self, WhichSlot, Scale, Alpha, Position, Image, Anchor):
        self.Titles[WhichSlot].texture = Texture(Image)
        self.Titles[WhichSlot].position = Position
        self.Titles[WhichSlot].scale = Scale
        self.Titles[WhichSlot].alpha = Alpha
        self.Titles[WhichSlot].anchor_point = Anchor
        
    def ClassBackgroundAttributes(self, WhichSlot, Position):
        self.ClassBackgrounds[WhichSlot].position = Position
        
    def ClassTitleAttributes(self, WhichSlot, Color, Font, Position, Text):
        self.ClassTitles[WhichSlot].text = Text
        self.ClassTitles[WhichSlot].position = Position
        self.ClassTitles[WhichSlot].font = Font
        self.ClassTitles[WhichSlot].color = Color
        
    def CheckWhichClass(self, touch, Class, ClassText, ClassBack, ClassColor, LeftExtraStats, RightExtraStats, PassiveImage, MainStat, MainResource, T1, T2, T3, T4):
        if ClassText.frame.contains_point(touch.location) or ClassBack.frame.contains_point(touch.location):
            self.BlackText()
            self.ClassIcons[0].texture = Texture(PassiveImage)
            self.ClassTitles[8].text = str(MainStat)
            self.ClassTitles[9].text = str(MainResource)
            globals.ClassStat = str(MainStat)
            globals.ClassResource = str(MainResource)
            self.ClassTitles[8].color = ClassColor
            self.ClassTitles[9].color = ClassColor
            globals.ClassColor = str(ClassColor)
            ClassText.color = ClassColor
            self.ClassIcons[1].color = ClassColor
            globals.Class = Class
            self.ClassTitles[11].text = str(LeftExtraStats)
            self.ClassTitles[12].text = str(RightExtraStats)
            self.ClassTitles[11].color = ClassColor
            self.ClassTitles[12].color = ClassColor
            self.ClassTitles[10].text = (str('Trait I: \n') + str(T1) + str('\n\nTrait II: \n') + str(T2) + str('\n\nTrait III: \n') + str(T3) + str('\n\nTrait IV: \n') + str(T4))
            self.ClassTitles[10].color = ClassColor
            
    def ClassIconsAttributes(self, WhichSlot, Image, Scale, Alpha):
        self.ClassIcons[WhichSlot].texture = Texture(Image)
        self.ClassIcons[WhichSlot].scale = Scale
        self.ClassIcons[WhichSlot].alpha = Alpha
