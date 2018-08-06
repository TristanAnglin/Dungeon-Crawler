from scene import *
import time
import random
import ui

class Dungeons(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.dungeon1setup = 0
        self.dungeon2setup = 0
        self.Tiles = []
        self.MovePad = []
        self.Squares = []
        self.MovePoints = []
        self.background = SpriteNode('Dungeon Crawler/assets/MainMenu/gradient.JPG',
            	                        position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
                                      
        for movepad in range(5):
            self.MovePad.append(SpriteNode('Dungeon Crawler/assets/GameScene/IMG_1176.PNG',
            	                        position = (self.size_of_screen_x/1.01 - self.size_of_screen_x, self.size_of_screen_y/1.05 - self.size_of_screen_y),
                                      scale = 0.2,
                                      anchor_point = (0,0),
                                      alpha = 0,
                                      color = '#000000',
                                      parent = self))
        self.MovePad[0].texture = Texture('Dungeon Crawler/assets/GameScene/IMG_1175.PNG')
        self.MovePad[1].texture = Texture('Dungeon Crawler/assets/GameScene/IMG_1179.PNG')
        self.MovePad[2].texture = Texture('Dungeon Crawler/assets/GameScene/IMG_1177.PNG')
        self.MovePad[3].texture = Texture('Dungeon Crawler/assets/GameScene/IMG_1176.PNG')
        self.MovePad[4].texture = Texture('Dungeon Crawler/assets/GameScene/IMG_1190.PNG')
        self.MovePad[4].alpha = 0.5
        
                                      
        for Points in range(4):
            self.MovePoints.append(SpriteNode(position = (0,0),
                                      scale = 0.05,
                                      anchor_point = (0.5,0.5),
                                      alpha = 0,
                                      color = '#ffffff',
                                      parent = self))
                                      
        self.MovePoints[0].position = (self.size_of_screen_x/19, self.size_of_screen_y/5.75)
        self.MovePoints[1].position = (self.size_of_screen_x/19, self.size_of_screen_y/15)
        self.MovePoints[2].position = (self.size_of_screen_x/7.75, self.size_of_screen_y/15)
        self.MovePoints[3].position = (self.size_of_screen_x/7.75, self.size_of_screen_y/5.75)
        
        self.AttackPad = SpriteNode('Dungeon Crawler/assets/Icons/upg_sword.png',
            	                        position = (self.size_of_screen_x/1.05, 0),
                                      scale = 0.375,
                                      anchor_point = (1,0),
                                      alpha = 0.5,
                                      color = '#000000',
                                      parent = self)
        
        self.TilingSetUp()
        self.BarSetups()
    def update(self):
        #this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.MovePad[4].frame.contains_point(touch.location):
            self.CheckDirec(touch)
        if self.AttackPad.frame.contains_point(touch.location):
            self.AttackPad.alpha = 1
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if self.MovePad[4].frame.contains_point(touch.location):
            self.CheckDirec(touch)
        else:
            self.MovePad[0].alpha = 0
            self.MovePad[1].alpha = 0
            self.MovePad[2].alpha = 0
            self.MovePad[3].alpha = 0
        
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        self.MovePad[0].alpha = 0
        self.MovePad[1].alpha = 0
        self.MovePad[2].alpha = 0
        self.MovePad[3].alpha = 0
        self.AttackPad.alpha = 0.5
        
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
    
    def TilingSetUp(self):
        for tiling in range(100):
            self.randomint = random.randint(1,3)
            if self.randomint == 1:
                self.randomimg = 'Dungeon Crawler/assets/GameScene/stone_E.png'
            elif self.randomint == 2:
                self.randomimg = 'Dungeon Crawler/assets/GameScene/stone_E.png'
            elif self.randomint == 3:
                self.randomimg = 'Dungeon Crawler/assets/GameScene/stone_E.png'
            self.Tiles.append(SpriteNode(str(self.randomimg),
                                      scale = 0.4,
                                      anchor_point = (0.5,0.5),
                                      parent = self))
        
        self.Tiles[0].position = (self.size_of_screen_x,self.size_of_screen_y+self.size_of_screen_y/11.75)
        for Row1 in range(11):
            self.Tiles[Row1].position = ((self.Tiles[0].position.x - (self.Tiles[0].size.x/2.5)*Row1), self.Tiles[0].position.y)
        self.Tiles[11].position = (self.Tiles[0].position.x - self.Tiles[0].size.x/5, self.Tiles[0].position.y - self.Tiles[0].size.x/8.75)
        for Row2 in range(10):
            self.Tiles[11+Row2].position = ((self.Tiles[11].position.x - (self.Tiles[11].size.x/2.5)*Row2), self.Tiles[11].position.y)
        self.Tiles[21].position = (self.Tiles[0].position.x, self.Tiles[0].position.y - self.Tiles[0].size.x/4.365)
        for Row3 in range(11):
            self.Tiles[21+Row3].position = ((self.Tiles[21].position.x - (self.Tiles[11].size.x/2.5)*Row3), self.Tiles[21].position.y)
        
        for NumOfsquares in range(len(self.Tiles)):
            for squares in range(16):
                self.Squares.append(SpriteNode(scale = 0.075,
                                               alpha = 0,
                                               position = (self.Tiles[NumOfsquares].position.x, self.Tiles[NumOfsquares].position.y),
                                               anchor_point = (0.5,0.5),
                                               parent = self))
                
            self.PositioningMovePoints(NumOfsquares,1,'',0,12)
            
            self.PositioningMovePoints(NumOfsquares,2,'-',21,10.25)
            self.PositioningMovePoints(NumOfsquares,3,'+',21,10.25)
            
            self.PositioningMovePoints(NumOfsquares,4,'-',10,9)
            self.PositioningMovePoints(NumOfsquares,5,'',0,9)
            self.PositioningMovePoints(NumOfsquares,6,'+',10,9)
            
            self.PositioningMovePoints(NumOfsquares,7,'-',6.5,8)
            self.PositioningMovePoints(NumOfsquares,8,'-',19,8)
            self.PositioningMovePoints(NumOfsquares,9,'+',6.5,8)
            self.PositioningMovePoints(NumOfsquares,10,'+',19,8)
            
            self.PositioningMovePoints(NumOfsquares,11,'-',10,7.1)
            self.PositioningMovePoints(NumOfsquares,12,'',0,7.1)
            self.PositioningMovePoints(NumOfsquares,13,'+',10,7.1)
            
            self.PositioningMovePoints(NumOfsquares,14,'-',21,6.45)
            self.PositioningMovePoints(NumOfsquares,15,'+',21,6.45)
            
            self.PositioningMovePoints(NumOfsquares,16,'',0,5.95)
            
            
            
            
        # (0.5,0.5) anchor is W/S-facing object top left, (0.125,0.61) anchor is W/S-facing object bottom right
        # (0.5,0.5) anchor is E/N-facing object top right, (0.8775,0.615) anchor is E/N-facing object bottom right
        
        #self.T1 = SpriteNode('Dungeon Crawler/assets/GameScene/stoneWallHole_N.png',
                             # parent = self,
                      #        scale = 0.4,
                          #    anchor_point = (0.8775,0.615),
                          #    position = (self.screen_center_x, self.screen_center_y))
        
    def CheckDirec(self, touch):
        self.TouchedHere = touch.location
        self.One = abs(self.MovePoints[0].position - touch.location)
        self.Two = abs(self.MovePoints[1].position - touch.location)
        self.Three = abs(self.MovePoints[2].position - touch.location)
        self.Four = abs(self.MovePoints[3].position - touch.location)
        
        self.MovePad[0].alpha = 0
        self.MovePad[1].alpha = 0
        self.MovePad[2].alpha = 0
        self.MovePad[3].alpha = 0
        
        if self.One < self.Two and self.One < self.Three and self.One < self.Four:
            self.MovePad[0].alpha = 1
        if self.Two < self.One and self.Two < self.Three and self.Two < self.Four:
            self.MovePad[1].alpha = 1
        if self.Three < self.One and self.Three < self.Two and self.Three < self.Four:
            self.MovePad[2].alpha = 1
        if self.Four < self.One and self.Four < self.Two and self.Four < self.Three:
            self.MovePad[3].alpha = 1
            
    
    def PositioningMovePoints(self,NumOfsquares,Num,Dire,X,Y):
        if Dire == '+':
            self.Squares[len(self.Squares)-Num].position = (self.Tiles[NumOfsquares].position.x + (self.Tiles[0].size.x/X), self.Tiles[NumOfsquares].position.y - (self.Tiles[0].size.y/Y))
        elif Dire == '-':
            self.Squares[len(self.Squares)-Num].position = (self.Tiles[NumOfsquares].position.x - (self.Tiles[0].size.x/X), self.Tiles[NumOfsquares].position.y - (self.Tiles[0].size.y/Y))
        elif Dire == '':
            self.Squares[len(self.Squares)-Num].position = (self.Tiles[NumOfsquares].position.x, self.Tiles[NumOfsquares].position.y - (self.Tiles[0].size.y/Y))
            
            
    def BarSetups(self):
                                      
        
        self.HealthBack = SpriteNode('Dungeon Crawler/assets/MainMenu/gradient.JPG',
                                      scale = 1,
                                      color = '#ffffff',
                                      alpha = 1,
                                      size = (self.size_of_screen_x/3.225, self.size_of_screen_y/15),
                                      position = (self.screen_center_x/1.45, self.size_of_screen_y*1.0815 - self.size_of_screen_y),
                                      anchor_point = (0,0.5),
                                      parent = self)
                                      
        self.Health = SpriteNode('Dungeon Crawler/assets/MainMenu/gradient.JPG',
                                      scale = 1,
                                      color = '#ff2b2b',
                                      alpha = 1,
                                      size = (self.HealthBack.size.x/2, self.HealthBack.size.y),
                                      position = (self.HealthBack.position.x, self.HealthBack.position.y),
                                      anchor_point = (0,0.5),
                                      parent = self)
        
        self.ResourceBack = SpriteNode('Dungeon Crawler/assets/MainMenu/gradient.JPG',
                                      scale = 1,
                                      color = '#ffffff',
                                      alpha = 1,
                                      size = (self.size_of_screen_x/3.225, self.size_of_screen_y/26),
                                      position = (self.screen_center_x/1.45, self.size_of_screen_y*1.0275 - self.size_of_screen_y),
                                      anchor_point = (0,0.5),
                                      parent = self)
                                      
        self.Resource = SpriteNode('Dungeon Crawler/assets/MainMenu/gradient.JPG',
                                      scale = 1,
                                      color = '#2be3ff',
                                      alpha = 1,
                                      size = (self.ResourceBack.size.x/1.5, self.ResourceBack.size.y),
                                      position = (self.ResourceBack.position.x, self.ResourceBack.position.y),
                                      anchor_point = (0,0.5),
                                      parent = self)
        
        self.FrameResourceHp = SpriteNode('Dungeon Crawler/assets/GameScene/BaseHpHolder.PNG',
                                      scale = 0.15,
                                      color = '#c0c0c0',
                                      alpha = 1,
                                      position = (self.screen_center_x, 0),
                                      anchor_point = (0.5,0),
                                      parent = self)
                                      
        self.HealthLabel = LabelNode(text = '[ 50 | 100 ] 50%',
                                     parent = self,
                                     scale = 1,
                                     position = (self.screen_center_x, self.HealthBack.position.y),
                                     font = ('CopperPlate', 15),
                                     color = '#000000',
                                     anchor_point = (0.5, 0.5))
                                     
        self.ResourceLabel = LabelNode(text = '[ 75 | 100 ] 75%',
                                     parent = self,
                                     scale = 1,
                                     position = (self.screen_center_x, self.ResourceBack.position.y),
                                     font = ('CopperPlate', 15),
                                     color = '#000000',
                                     anchor_point = (0.5, 0.5))
                                     
        self.HealthImg = SpriteNode('Dungeon Crawler/assets/Icons/heart.png',
                                      scale = 0.15,
                                      color = '#c0c0c0',
                                      alpha = 1,
                                      position = (self.Health.position.x, self.Health.position.y),
                                      anchor_point = (0.5,0.5),
                                      parent = self)
                                      
        self.ResourceImg = SpriteNode('ICS3U/Final/Hit and Run/assets/sprites/exporb.PNG',
                                      scale = 0.2,
                                      color = '#c0c0c0',
                                      alpha = 1,
                                      position = (self.Resource.position.x, self.Resource.position.y),
                                      anchor_point = (0.5,0.5),
                                      parent = self)
        
main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = Dungeons()
main_view.present(hide_title_bar = True, animated = False)