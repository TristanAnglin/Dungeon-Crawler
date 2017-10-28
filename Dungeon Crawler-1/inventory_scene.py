import console
from random import *
from classes import *
from globals import *
from gemuse_scene import *
from scene import *
import time

class Item(object):
    pass

class InventoryScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.ItemDescription = ''
        self.ItemBackground = []
        self.ItemFrame = []
        self.ItemObject = []
        self.ItemText = []
        self.EquippedFrames = []
        self.EquippedText = []
        self.background = SpriteNode('assets/Icons/woodback.PNG',
                                      position = self.size / 2,
                                      scale = 1,
                                      parent = self,
                                      size = (self.size_of_screen_x, self.size_of_screen_y))
                                      
        self.SetupEquippedFrames('assets/Icons/helmet.png', (self.screen_center_x * 1.4, self.screen_center_y * 1.625))
        self.SetupEquippedFrames('assets/Icons/armor.png', (self.screen_center_x * 1.4, self.screen_center_y * 1.3))
        self.SetupEquippedFrames('assets/Icons/upg_sword.png', (self.screen_center_x * 1.15, self.screen_center_y * 1.3))
        self.SetupEquippedFrames('assets/Icons/shieldSmall.png', (self.screen_center_x * 1.65, self.screen_center_y * 1.3))
        self.SetupInventoryFraming(self.ItemBackground, 'assets/MainMenu/gradient.JPG', 0.3815)
        self.SetupInventoryFraming(self.ItemFrame, 'assets/Classes/frame-8-grey.png', 0.3815)
        self.SetupInventoryFraming(self.ItemObject, 'assets/Icons/shop.PNG', 0.186)
        self.SetupInventoryText(self.ItemText, '')
        self.SetupInventoryPositions(self.ItemBackground)
        self.SetupInventoryPositions(self.ItemText)
        self.SetupInventoryPositions(self.ItemObject)
        self.SetupInventoryPositions(self.ItemFrame)
        self.startup()
        self.showEquipped()
        self.itemsininventory()
    def update(self):
        #this method is called, hopefully, 60 times a second
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        self.TapInventory(touch)
        if self.EquippedFrames[0].frame.contains_point(touch.location) and len(EquippedSlot1) > 0 or self.EquippedFrames[2].frame.contains_point(touch.location) and len(EquippedSlot1) > 0:
            self.checkEquippedHelm(touch)
        if self.EquippedFrames[3].frame.contains_point(touch.location) and len(EquippedSlot2) > 0 or self.EquippedFrames[5].frame.contains_point(touch.location) and len(EquippedSlot2) > 0:
            self.checkEquippedChest(touch)
        if self.EquippedFrames[6].frame.contains_point(touch.location) and len(EquippedSlot3) > 0 or self.EquippedFrames[8].frame.contains_point(touch.location) and len(EquippedSlot3) > 0:
            self.checkEquippedWeapon(touch)
        if self.EquippedFrames[9].frame.contains_point(touch.location) and len(EquippedSlot4) > 0 or self.EquippedFrames[11].frame.contains_point(touch.location) and len(EquippedSlot4) > 0:
            self.checkEquippedOffhand(touch)
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
    
    def CreateGem(self, WhichType, GemRarity):
        Loot = Item()
        Loot.GemValues = [1, 1.5, 2, 2.5, 5, 7.5, 10, 12.5, 15, 20, 25]
        Loot.ItemRarity = GemRarity
        if Loot.ItemRarity <= 30:
            Loot.ItemColor = .61, .61, .61
            Loot.ItemTitle = 'Common'
            Loot.GemValue = Loot.GemValues[random.randint(0,2)]
            
        elif Loot.ItemRarity <= 55 and Loot.ItemRarity > 30:
            Loot.ItemColor = .14, .81, .0
            Loot.ItemTitle = 'Uncommon'
            Loot.GemValue = Loot.GemValues[random.randint(2,4)]
            
        elif Loot.ItemRarity <= 75 and Loot.ItemRarity > 55:
            Loot.ItemColor = .0, .71, .81
            Loot.ItemTitle = 'Rare'
            Loot.GemValue = Loot.GemValues[random.randint(4,6)]
            
        elif Loot.ItemRarity <= 90 and Loot.ItemRarity > 75:
            Loot.ItemColor = .56, .03, .81
            Loot.ItemTitle = 'Epic'
            Loot.GemValue = Loot.GemValues[random.randint(6,8)]
            
        elif Loot.ItemRarity <= 100 and Loot.ItemRarity > 90:
            Loot.ItemColor = 1.0, .52, .0
            Loot.ItemTitle = 'Exotic'
            Loot.GemValue = Loot.GemValues[random.randint(8,10)]
        
        Loot.Gem = 'assets/Icons/blankgem.PNG'
        Loot.Color1 = float(random.randint(1,85)/100.00)
        Loot.Color2 = float(random.randint(1,85)/100.00)
        Loot.Color3 = float(random.randint(1,85)/100.00)
        Loot.GemColor = (Loot.Color1, Loot.Color2, Loot.Color3)
            
        Loot.GemDifferentTypes = ['+' + str(Loot.GemValue) + '% Bleed', '+' + str(Loot.GemValue) + '% Reflect', '+' + str(Loot.GemValue) + '% Explosive', '+' + str(Loot.GemValue) + '% Crit', '+' + str(Loot.GemValue) + '% Stamina', '+' + str(Loot.GemValue) + '% Range']
        Loot.Type = Loot.GemDifferentTypes[WhichType]
        Loot.SellPrice = int((((Loot.ItemRarity * 2.45) * 0.197) + Loot.GemValue * 1.5) * 0.31)
        Inventory.append(Loot)
    def CreateItem(self, ItemRarity, WhereTo, WhichType):
        Loot = Item()
        
        Loot.ItemRarity = ItemRarity
        Loot.ItemLevel = globals.Level
        Loot.ItemMultipliers = [0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20]
        Loot.MultiRange = int(len(Loot.ItemMultipliers)-1)
        
        Loot.Value1 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 297.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value2 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 197.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value3 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 237.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value4 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 237.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value5 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 114.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value6 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 159.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value7 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 56.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value8 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 32.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value9 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 32.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value10 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 32.50) * globals.Level) * 100.00) / 100.00)
        Loot.Value11 = float(round(((Loot.ItemMultipliers[random.randint(0, Loot.MultiRange)] * Loot.ItemRarity / 497.50) * globals.Level) * 100.00) / 100.00)
        
        
        Loot.TotalEnchants = ['+' + str(Loot.Value1) + '% Leech', '+' + str(Loot.Value2) + '% Gold', '+' + str(Loot.Value3) + '% Crit', '+' + str(Loot.Value4) + '% Dodge', '+' + str(Loot.Value5) + '% Speed', '+' + str(Loot.Value6) + '% Haste', '+' + str(Loot.Value7) + '% Stamina', '+' + str(Loot.Value8) + '% Agility',  '+' + str(Loot.Value9) + '% Strength',  '+' + str(Loot.Value10) + '% Intellect', '+' + str(Loot.Value11) + '% Versatility']
    
        Loot.CopyTotalEnchants = Loot.TotalEnchants
        Loot.ItemEnchants = []
        Loot.GemsSocketed = []
    
        if Loot.ItemRarity <= 30:
            Loot.ItemMaxDurability = random.randint(50,175)
            Loot.ItemDurability = Loot.ItemMaxDurability
            Loot.ItemColor = .61, .61, .61
            Loot.ItemTitle = 'Common'
            Loot.NumOfEnchantments = 0
            Loot.NumOfSockets = 0
        
        elif Loot.ItemRarity <= 55 and Loot.ItemRarity > 30:
            Loot.ItemMaxDurability = random.randint(175,235)
            Loot.ItemDurability = Loot.ItemMaxDurability
            Loot.ItemColor = .14, .81, .0
            Loot.ItemTitle = 'Uncommon'
            Loot.NumOfEnchantments = random.randint(1,2)
            Loot.NumOfSockets = 0
            for WhichEnchants in range(Loot.NumOfEnchantments):
                Loot.ItemEnchants.append(Loot.CopyTotalEnchants[random.randint(0,len(Loot.CopyTotalEnchants)-1)])
                Loot.CopyTotalEnchants.remove(Loot.ItemEnchants[len(Loot.ItemEnchants)-1])
        
        elif Loot.ItemRarity <= 75 and Loot.ItemRarity > 55:
            Loot.ItemMaxDurability = random.randint(235,290)
            Loot.ItemDurability = Loot.ItemMaxDurability
            Loot.ItemColor = .0, .71, .81
            Loot.ItemTitle = 'Rare'
            Loot.NumOfEnchantments = random.randint(2,4)
            Loot.NumOfSockets = random.randint(0,1)
            for WhichEnchants in range(Loot.NumOfEnchantments):
                Loot.ItemEnchants.append(Loot.CopyTotalEnchants[random.randint(0,len(Loot.CopyTotalEnchants)-1)])
                Loot.CopyTotalEnchants.remove(Loot.ItemEnchants[len(Loot.ItemEnchants)-1])
            
        elif Loot.ItemRarity <= 90 and Loot.ItemRarity > 75:
            Loot.ItemMaxDurability = random.randint(290,375)
            Loot.ItemDurability = Loot.ItemMaxDurability
            Loot.ItemColor = .56, .03, .81
            Loot.ItemTitle = 'Epic'
            Loot.NumOfEnchantments = random.randint(3,6)
            Loot.NumOfSockets = random.randint(0,1)
            for WhichEnchants in range(Loot.NumOfEnchantments):
                Loot.ItemEnchants.append(Loot.CopyTotalEnchants[random.randint(0,len(Loot.CopyTotalEnchants)-1)])
                Loot.CopyTotalEnchants.remove(Loot.ItemEnchants[len(Loot.ItemEnchants)-1])
                
        
        elif Loot.ItemRarity <= 100 and Loot.ItemRarity > 90:
            Loot.ItemMaxDurability = random.randint(375,455)
            Loot.ItemDurability = Loot.ItemMaxDurability
            Loot.ItemColor = 1.0, .52, .0
            Loot.ItemTitle = 'Exotic'
            Loot.NumOfEnchantments = random.randint(5,8)
            Loot.NumOfSockets = random.randint(1,2)
            for WhichEnchants in range(Loot.NumOfEnchantments):
                Loot.ItemEnchants.append(Loot.CopyTotalEnchants[random.randint(0,len(Loot.CopyTotalEnchants)-1)])
                Loot.CopyTotalEnchants.remove(Loot.ItemEnchants[len(Loot.ItemEnchants)-1])
            
        Loot.SellPrice = int((((Loot.ItemRarity * 6.89) + Loot.ItemLevel * 38.62) + Loot.NumOfEnchantments * 196.43) + Loot.NumOfSockets * 198.28)
        
        if WhichType == int(1):
            Loot.Type = 'Helmet'
        elif WhichType == int(2):
            Loot.Type = 'Chestplate'
        elif WhichType == int(3):
            Loot.Type = 'Weapon'
        elif WhichType == int(4):
            Loot.Type = 'Offhand'
        WhereTo.append(Loot)
    def checkEquippedHelm(self, touch):
            self.ItemDescription = ''
            for numberofsockets in range(EquippedSlot1[0].NumOfSockets):
                self.ItemDescription = self.ItemDescription + '[+] Gem Socket\n'
            for numberofenchants in range(EquippedSlot1[0].NumOfEnchantments):
                self.ItemDescription = self.ItemDescription + str(EquippedSlot1[0].ItemEnchants[numberofenchants]) + '\n'
            self.ItemPopUp = console.alert(str(EquippedSlot1[0].ItemTitle) + ' ' + str(EquippedSlot1[0].Type) + '\nDurability: ' + str(EquippedSlot1[0].ItemDurability) + ' / ' + str(EquippedSlot1[0].ItemMaxDurability) + '\nRarity: ' + str(EquippedSlot1[0].ItemRarity) + '\nLevel: ' + str(EquippedSlot1[0].ItemLevel), str(self.ItemDescription), 'Unequip', 'Sell [$' + str(EquippedSlot1[0].SellPrice) + ']')
                
            if self.ItemPopUp == 1:
                Inventory.append(EquippedSlot1[0])
                self.remove_from_parent()
                EquippedSlot1.remove(EquippedSlot1[0])
                self.EquippedFrames[0].color = '#ffffff'	
                self.EquippedFrames[1].alpha = 0.5
                self.itemslotcounter = 0
                self.EquippedText[0].text = '  '
                self.EquippedFrames[2].texture = Texture('assets/Classes/frame-8-grey.png')
                self.itemsininventory()
            elif self.ItemPopUp == 2:
                globals.Coins = globals.Coins + EquippedSlot1[0].SellPrice
                self.remove_from_parent()
                EquippedSlot1.remove(EquippedSlot1[0])
                self.EquippedFrames[0].color = '#ffffff'	
                self.EquippedFrames[1].alpha = 0.5
                self.EquippedText[0].text = '  '
                self.EquippedFrames[2].texture = Texture('assets/Classes/frame-8-grey.png')
    def checkEquippedChest(self, touch):
            self.ItemDescription = ''
            for numberofsockets in range(EquippedSlot2[0].NumOfSockets):
                self.ItemDescription = self.ItemDescription + '[+] Gem Socket\n'
            for numberofenchants in range(EquippedSlot2[0].NumOfEnchantments):
                self.ItemDescription = self.ItemDescription + str(EquippedSlot2[0].ItemEnchants[numberofenchants]) + '\n'
            self.ItemPopUp = console.alert(str(EquippedSlot2[0].ItemTitle) + ' ' + str(EquippedSlot2[0].Type) + '\nDurability: ' + str(EquippedSlot2[0].ItemDurability) + ' / ' + str(EquippedSlot2[0].ItemMaxDurability) + '\nRarity: ' + str(EquippedSlot2[0].ItemRarity) + '\nLevel: ' + str(EquippedSlot2[0].ItemLevel), str(self.ItemDescription), 'Unequip', 'Sell [$' + str(EquippedSlot2[0].SellPrice) + ']')
                
            if self.ItemPopUp == 1:
                Inventory.append(EquippedSlot2[0])
                self.remove_from_parent()
                EquippedSlot2.remove(EquippedSlot2[0])
                self.EquippedFrames[3].color = '#ffffff'
                self.EquippedFrames[4].alpha = 0.5
                self.itemsininventory()
                self.EquippedText[1].text = '  '
                self.EquippedFrames[5].texture = Texture('assets/Classes/frame-8-grey.png')
            elif self.ItemPopUp == 2:
                globals.Coins = globals.Coins + EquippedSlot2[0].SellPrice
                self.remove_from_parent()
                EquippedSlot2.remove(EquippedSlot2[0])
                self.EquippedFrames[3].color = '#ffffff'
                self.EquippedFrames[4].alpha = 0.5
                self.EquippedText[1].text = '  '
                self.EquippedFrames[5].texture = Texture('assets/Classes/frame-8-grey.png')
    def checkEquippedWeapon(self, touch):
            self.ItemDescription = ''
            for numberofsockets in range(EquippedSlot3[0].NumOfSockets):
                self.ItemDescription = self.ItemDescription + '[+] Gem Socket\n'
            for numberofenchants in range(EquippedSlot3[0].NumOfEnchantments):
                self.ItemDescription = self.ItemDescription + str(EquippedSlot3[0].ItemEnchants[numberofenchants]) + '\n'
            self.ItemPopUp = console.alert(str(EquippedSlot3[0].ItemTitle) + ' ' + str(EquippedSlot3[0].Type) + '\nDurability: ' + str(EquippedSlot3[0].ItemDurability) + ' / ' + str(EquippedSlot3[0].ItemMaxDurability) + '\nRarity: ' + str(EquippedSlot3[0].ItemRarity) + '\nLevel: ' + str(EquippedSlot3[0].ItemLevel), str(self.ItemDescription), 'Unequip', 'Sell [$' + str(EquippedSlot3[0].SellPrice) + ']')
                
            if self.ItemPopUp == 1:
                Inventory.append(EquippedSlot3[0])
                self.remove_from_parent()
                EquippedSlot3.remove(EquippedSlot3[0])
                self.EquippedFrames[6].color = '#ffffff'
                self.EquippedFrames[7].alpha = 0.5
                self.EquippedText[2].text = '  '
                self.EquippedFrames[8].texture = Texture('assets/Classes/frame-8-grey.png')
                self.itemsininventory()
            elif self.ItemPopUp == 2:
                globals.Coins = globals.Coins + EquippedSlot3[0].SellPrice
                self.remove_from_parent()
                EquippedSlot3.remove(EquippedSlot3[0])
                self.EquippedFrames[6].color = '#ffffff'
                self.EquippedFrames[7].alpha = 0.5
                self.EquippedText[2].text = '  '
                self.EquippedFrames[8].texture = Texture('assets/Classes/frame-8-grey.png')
    def checkEquippedOffhand(self, touch):
            self.ItemDescription = ''
            for numberofsockets in range(EquippedSlot4[0].NumOfSockets):
                self.ItemDescription = self.ItemDescription + '[+] Gem Socket\n'
            for numberofenchants in range(EquippedSlot4[0].NumOfEnchantments):
                self.ItemDescription = self.ItemDescription + str(EquippedSlot4[0].ItemEnchants[numberofenchants]) + '\n'
            self.ItemPopUp = console.alert(str(EquippedSlot4[0].ItemTitle) + ' ' + str(EquippedSlot4[0].Type) + '\nDurability: ' + str(EquippedSlot4[0].ItemDurability) + ' / ' + str(EquippedSlot4[0].ItemMaxDurability) + '\nRarity: ' + str(EquippedSlot4[0].ItemRarity) + '\nLevel: ' + str(EquippedSlot4[0].ItemLevel), str(self.ItemDescription), 'Unequip', 'Sell [$' + str(EquippedSlot4[0].SellPrice) + ']')
                
            if self.ItemPopUp == 1:
                Inventory.append(EquippedSlot4[0])
                self.remove_from_parent()
                EquippedSlot4.remove(EquippedSlot4[0])
                self.EquippedFrames[9].color = '#ffffff'
                self.EquippedFrames[10].alpha = 0.5
                self.itemsininventory()
                self.EquippedText[3].text = '  '
                self.EquippedFrames[11].texture = Texture('assets/Classes/frame-8-grey.png')
            elif self.ItemPopUp == 2:
                globals.Coins = globals.Coins + EquippedSlot4[0].SellPrice
                self.remove_from_parent()
                EquippedSlot4.remove(EquippedSlot4[0])
                self.EquippedFrames[9].color = '#ffffff'
                self.EquippedFrames[10].alpha = 0.5
                self.EquippedText[3].text = '  '
                self.EquippedFrames[11].texture = Texture('assets/Classes/frame-8-grey.png')
    def itemsininventory(self):
        self.itemslotcounter = 0
        for items in Inventory:
            self.ItemFrame[int(self.itemslotcounter)].texture = Texture('assets/Classes/frame-8-grey.png')
            self.ItemBackground[int(self.itemslotcounter)].color = items.ItemColor
            self.ItemText[int(self.itemslotcounter)].color = items.ItemColor
            if items.ItemTitle == 'Exotic':
                self.ItemFrame[int(self.itemslotcounter)].texture = Texture('assets/Classes/frame-5-orange.png')
            if items.Type == 'Helmet':
                self.ItemText[int(self.itemslotcounter)].text = '  ' + items.ItemTitle[0] + '\n  Lv' + str(items.ItemLevel) + '\n  ' + str(items.ItemDurability) + ' / ' + str(items.ItemMaxDurability) + '\n'
                self.ItemObject[int(self.itemslotcounter)].color = '#ffffff'
                self.ItemObject[int(self.itemslotcounter)].texture = Texture('assets/Icons/helmet.png')
                self.ItemObject[int(self.itemslotcounter)].alpha = 1
            elif items.Type == 'Chestplate':
                self.ItemText[int(self.itemslotcounter)].text = '  ' + items.ItemTitle[0] + '\n  Lv' + str(items.ItemLevel) + '\n  ' + str(items.ItemDurability) + ' / ' + str(items.ItemMaxDurability) + '\n'
                self.ItemObject[int(self.itemslotcounter)].color = '#ffffff'
                self.ItemObject[int(self.itemslotcounter)].texture = Texture('assets/Icons/armor.png')
                self.ItemObject[int(self.itemslotcounter)].alpha = 1
            elif items.Type == 'Weapon':
                self.ItemText[int(self.itemslotcounter)].text = '  ' + items.ItemTitle[0] + '\n  Lv' + str(items.ItemLevel) + '\n  ' + str(items.ItemDurability) + ' / ' + str(items.ItemMaxDurability) + '\n'
                self.ItemObject[int(self.itemslotcounter)].color = '#ffffff'
                self.ItemObject[int(self.itemslotcounter)].texture = Texture('assets/Icons/upg_sword.png')
                self.ItemObject[int(self.itemslotcounter)].alpha = 1
            elif items.Type == 'Offhand':
                self.ItemText[int(self.itemslotcounter)].text = '  ' + items.ItemTitle[0] + '\n  Lv' + str(items.ItemLevel) + '\n  ' + str(items.ItemDurability) + ' / ' + str(items.ItemMaxDurability) + '\n'
                self.ItemObject[int(self.itemslotcounter)].color = '#ffffff'
                self.ItemObject[int(self.itemslotcounter)].texture = Texture('assets/Icons/shieldSmall.png')
                self.ItemObject[int(self.itemslotcounter)].alpha = 1
            else:
                self.ItemText[int(self.itemslotcounter)].text = '  ' + items.ItemTitle[0] + '\n  ' + (items.Type) + '\n'
                self.ItemObject[int(self.itemslotcounter)].texture = Texture(str(items.Gem))
                self.ItemObject[int(self.itemslotcounter)].alpha = 1
                self.ItemObject[int(self.itemslotcounter)].color = items.GemColor
            self.itemslotcounter = self.itemslotcounter + 1
        for clearEmptySlots in range(0,len(self.ItemFrame)):
            if len(Inventory)-1 >= clearEmptySlots:
                pass
            else:
                self.ItemBackground[clearEmptySlots].color = '#ffffff'
                self.ItemObject[clearEmptySlots].alpha = 0
                self.ItemObject[clearEmptySlots].color = '#ffffff'
                self.ItemText[clearEmptySlots].color = '#ffffff'
                self.ItemText[clearEmptySlots].text = ''
                self.ItemFrame[clearEmptySlots].texture = Texture('assets/Classes/frame-8-grey.png')
        
        
    def showEquipped(self):
        if len(EquippedSlot1) > 0:
            self.EquippedFrames[0].color = EquippedSlot1[0].ItemColor
            self.EquippedFrames[1].alpha = 1
            if EquippedSlot1[0].ItemTitle == 'Exotic':
                self.EquippedFrames[2].texture = Texture('assets/Classes/frame-5-orange.png')
            self.EquippedText[0].text = '  ' + str(EquippedSlot1[0].ItemTitle[0]) + '\n  Lv' + str(EquippedSlot1[0].ItemLevel) + '\n  ' + str(EquippedSlot1[0].ItemDurability) + ' / ' + str(EquippedSlot1[0].ItemMaxDurability) + '\n'
            self.EquippedText[0].color = EquippedSlot1[0].ItemColor
        if len(EquippedSlot2) > 0:
            self.EquippedFrames[3].color = EquippedSlot2[0].ItemColor
            self.EquippedFrames[4].alpha = 1
            if EquippedSlot2[0].ItemTitle == 'Exotic':
                self.EquippedFrames[5].texture = Texture('assets/Classes/frame-5-orange.png')
            self.EquippedText[1].text = '  ' + str(EquippedSlot2[0].ItemTitle[0]) + '\n  Lv' + str(EquippedSlot2[0].ItemLevel) + '\n  ' + str(EquippedSlot2[0].ItemDurability) + ' / ' + str(EquippedSlot2[0].ItemMaxDurability) + '\n'
            self.EquippedText[1].color = EquippedSlot2[0].ItemColor
        if len(EquippedSlot3) > 0:
            self.EquippedFrames[6].color = EquippedSlot3[0].ItemColor
            self.EquippedFrames[7].alpha = 1
            if EquippedSlot3[0].ItemTitle == 'Exotic':
                self.EquippedFrames[8].texture = Texture('assets/Classes/frame-5-orange.png')
            self.EquippedText[2].text = '  ' + str(EquippedSlot3[0].ItemTitle[0]) + '\n  Lv' + str(EquippedSlot3[0].ItemLevel) + '\n  ' + str(EquippedSlot3[0].ItemDurability) + ' / ' + str(EquippedSlot3[0].ItemMaxDurability) + '\n'
            self.EquippedText[2].color = EquippedSlot3[0].ItemColor
        if len(EquippedSlot4) > 0:
            self.EquippedFrames[9].color = EquippedSlot4[0].ItemColor
            self.EquippedFrames[10].alpha = 1
            if EquippedSlot4[0].ItemTitle == 'Exotic':
                self.EquippedFrames[11].texture = Texture('assets/Classes/frame-5-orange.png')
            self.EquippedText[3].text = '  ' + str(EquippedSlot4[0].ItemTitle[0]) + '\n  Lv' + str(EquippedSlot4[0].ItemLevel) + '\n  ' + str(EquippedSlot4[0].ItemDurability) + ' / ' + str(EquippedSlot4[0].ItemMaxDurability) + '\n'
            self.EquippedText[3].color = EquippedSlot4[0].ItemColor
            
    def TapInventory(self, touch):
        self.inventorycounter = 0
        for checkStuffInventory in Inventory:
            if self.ItemObject[int(self.inventorycounter)].frame.contains_point(touch.location):
                self.ItemDescription = ''
                if checkStuffInventory.Type != 'Helmet' and checkStuffInventory.Type != 'Chestplate' and checkStuffInventory.Type != 'Weapon' and checkStuffInventory.Type != 'Offhand':
                    self.ItemDescription = str(checkStuffInventory.Type)
                    self.ItemPopUp = console.alert(str(Inventory[int(self.inventorycounter)].ItemTitle) + ' Gem' + '\nRarity: ' + str(Inventory[int(self.inventorycounter)].ItemRarity), str(self.ItemDescription), 'Use', 'Sell [' + str(checkStuffInventory.SellPrice) + '*]')
                    
                    if self.ItemPopUp == 1:
                        run(GemUse())
                    if self.ItemPopUp == 2:
                        globals.GemShards = globals.GemShards + Inventory[int(self.inventorycounter)].SellPrice
                        self.remove_from_parent()
                        Inventory.remove(Inventory[int(self.inventorycounter)])
                        self.ItemObject[int(self.inventorycounter)].color = '#ffffff'
                        self.ItemObject[int(self.inventorycounter)].alpha = 0
                        self.ItemFrame[int(self.inventorycounter)].color = '#ffffff'
                        self.itemsininventory()
                else:
                    for numberofsockets in range(Inventory[int(self.inventorycounter)].NumOfSockets):
                        self.ItemDescription = self.ItemDescription + '[+] Gem Socket\n'
                    for numberofenchants in range(Inventory[int(self.inventorycounter)].NumOfEnchantments):
                        self.ItemDescription = self.ItemDescription + str(Inventory[int(self.inventorycounter)].ItemEnchants[numberofenchants]) + '\n'
                    if Inventory[int(self.inventorycounter)].Type == 'Helmet' and len(EquippedSlot1) > 0 or Inventory[int(self.inventorycounter)].Type == 'Chestplate' and len(EquippedSlot2) > 0 or Inventory[int(self.inventorycounter)].Type == 'Weapon' and len(EquippedSlot3) > 0 or Inventory[int(self.inventorycounter)].Type == 'Offhand' and len(EquippedSlot4) > 0:
                        self.ItemPopUp = console.alert(str(Inventory[int(self.inventorycounter)].ItemTitle) + ' ' + str(Inventory[int(self.inventorycounter)].Type) + '\nDurability: ' + str(Inventory[int(self.inventorycounter)].ItemDurability) + ' / ' + str(Inventory[int(self.inventorycounter)].ItemMaxDurability) + '\nRarity: ' + str(Inventory[int(self.inventorycounter)].ItemRarity) + '\nLevel: ' + str(Inventory[int(self.inventorycounter)].ItemLevel), str(self.ItemDescription), 'Swap', 'Sell [$' + str(Inventory[int(self.inventorycounter)].SellPrice) + ']')
                        if self.ItemPopUp == 1:
                            if Inventory[int(self.inventorycounter)].Type == 'Helmet':
                                Inventory.append(EquippedSlot1[0])
                                self.remove_from_parent()
                                EquippedSlot1.remove(EquippedSlot1[0])
                                EquippedSlot1.append(Inventory[int(self.inventorycounter)])
                                self.EquippedFrames[2].texture = Texture('assets/Classes/frame-8-grey.png')
                            elif Inventory[int(self.inventorycounter)].Type == 'Chestplate':
                                Inventory.append(EquippedSlot2[0])
                                self.remove_from_parent()
                                EquippedSlot2.remove(EquippedSlot2[0])
                                EquippedSlot2.append(Inventory[int(self.inventorycounter)])
                                self.EquippedFrames[5].texture = Texture('assets/Classes/frame-8-grey.png')
                            elif Inventory[int(self.inventorycounter)].Type == 'Weapon':
                                Inventory.append(EquippedSlot3[0])
                                self.remove_from_parent()
                                EquippedSlot3.remove(EquippedSlot3[0])
                                EquippedSlot3.append(Inventory[int(self.inventorycounter)])
                                self.EquippedFrames[8].texture = Texture('assets/Classes/frame-8-grey.png')
                            elif Inventory[int(self.inventorycounter)].Type == 'Offhand':
                                Inventory.append(EquippedSlot4[0])
                                self.remove_from_parent()
                                EquippedSlot4.remove(EquippedSlot4[0])
                                EquippedSlot4.append(Inventory[int(self.inventorycounter)])
                                self.EquippedFrames[11].texture = Texture('assets/Classes/frame-8-grey.png')
                            self.remove_from_parent()
                            Inventory.remove(Inventory[int(self.inventorycounter)])
                            self.ItemObject[int(self.inventorycounter)].color = '#ffffff'
                            self.ItemObject[int(self.inventorycounter)].alpha = 0
                            self.ItemFrame[int(self.inventorycounter)].color = '#ffffff'
                            self.showEquipped()
                            self.itemsininventory()
                        elif self.ItemPopUp == 2:
                            globals.Coins = globals.Coins + Inventory[int(self.inventorycounter)].SellPrice
                            self.remove_from_parent()
                            Inventory.remove(Inventory[int(self.inventorycounter)])
                            self.ItemObject[int(self.inventorycounter)].color = '#ffffff'
                            self.ItemObject[int(self.inventorycounter)].alpha = 0
                            self.ItemFrame[int(self.inventorycounter)].color = '#ffffff'
                            self.itemsininventory()
                    else:
                        self.ItemPopUp = console.alert(str(Inventory[int(self.inventorycounter)].ItemTitle) + ' ' + str(Inventory[int(self.inventorycounter)].Type) + '\nRarity: ' + str(Inventory[int(self.inventorycounter)].ItemRarity) + '\nLevel: ' + str(Inventory[int(self.inventorycounter)].ItemLevel), str(self.ItemDescription), 'Equip', 'Sell [$' + str(Inventory[int(self.inventorycounter)].SellPrice) + ']')
                
                        if self.ItemPopUp == 1:
                            if Inventory[int(self.inventorycounter)].Type == 'Helmet':
                                EquippedSlot1.append(Inventory[int(self.inventorycounter)])
                            if Inventory[int(self.inventorycounter)].Type == 'Chestplate':
                                EquippedSlot2.append(Inventory[int(self.inventorycounter)])
                            if Inventory[int(self.inventorycounter)].Type == 'Weapon':
                                EquippedSlot3.append(Inventory[int(self.inventorycounter)])
                            if Inventory[int(self.inventorycounter)].Type == 'Offhand':
                                EquippedSlot4.append(Inventory[int(self.inventorycounter)])
                            self.remove_from_parent()
                            Inventory.remove(Inventory[int(self.inventorycounter)])
                            self.ItemObject[int(self.inventorycounter)].color = '#ffffff'
                            self.ItemObject[int(self.inventorycounter)].alpha = 0
                            self.ItemFrame[int(self.inventorycounter)].color = '#ffffff'
                            self.itemsininventory()
                            self.showEquipped()
                        elif self.ItemPopUp == 2:
                            globals.Coins = globals.Coins + Inventory[int(self.inventorycounter)].SellPrice
                            self.remove_from_parent()
                            Inventory.remove(Inventory[int(self.inventorycounter)])
                            self.ItemObject[int(self.inventorycounter)].color = '#ffffff'
                            self.ItemObject[int(self.inventorycounter)].alpha = 0
                            self.ItemFrame[int(self.inventorycounter)].color = '#ffffff'
                            self.itemsininventory()
                        else:	
                            pass
            self.inventorycounter = self.inventorycounter + 1
    
    def SetupInventoryText(self, WhichArray, WhichText):
        for InventoryStuff in range(40):
            WhichArray.append(LabelNode(text = WhichText,
                                         parent = self,
                                         font = ('CopperPlate', 10),
                                         anchor_point = (0, 0),
                                         scale = 1))
            
    def SetupInventoryFraming(self, WhichArray, WhichImage, WhichScale):
        for InventoryStuff in range(40):
            WhichArray.append(SpriteNode(WhichImage,
                                         parent = self,
                                         anchor_point = (0, 0),
                                         scale = 0))
            WhichArray[InventoryStuff].size = (self.screen_center_x / 2, self.screen_center_y / 1.52)
            WhichArray[InventoryStuff].scale = WhichScale
    
    def SetupInventoryPositions(self, WhichArray):
        self.xvalue1 = 1.095
        self.xvalue2 = 1.19
        self.xvalue3 = 1.285
        self.xvalue4 = 1.38
        
        self.yvalue1 = 1.125
        self.yvalue2 = 1.25
        self.yvalue3 = 1.375
        self.yvalue4 = 1.5
        self.yvalue5 = 1.625
        self.yvalue6 = 1.75
        self.yvalue7 = 1.875
        
        WhichArray[0].position = (0, 0)
        WhichArray[1].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, 0)
        WhichArray[2].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, 0)
        WhichArray[3].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, 0)
        WhichArray[4].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, 0)
        WhichArray[5].position = (0, self.size_of_screen_y * self.yvalue1 - self.size_of_screen_y)
        WhichArray[6].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue1 - self.size_of_screen_y)
        WhichArray[7].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue1 - self.size_of_screen_y)
        WhichArray[8].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue1 - self.size_of_screen_y)
        WhichArray[9].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue1 - self.size_of_screen_y)
        WhichArray[10].position = (0, self.size_of_screen_y * self.yvalue2 - self.size_of_screen_y)
        WhichArray[11].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue2 - self.size_of_screen_y)
        WhichArray[12].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue2 - self.size_of_screen_y)
        WhichArray[13].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue2 - self.size_of_screen_y)
        WhichArray[14].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue2 - self.size_of_screen_y)
        WhichArray[15].position = (0, self.size_of_screen_y * self.yvalue3 - self.size_of_screen_y)
        WhichArray[16].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue3 - self.size_of_screen_y)         
        WhichArray[17].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue3 - self.size_of_screen_y) 
        WhichArray[18].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue3 - self.size_of_screen_y)
        WhichArray[19].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue3 - self.size_of_screen_y)
        WhichArray[20].position = (0, self.size_of_screen_y * self.yvalue4 - self.size_of_screen_y)
        WhichArray[21].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue4 - self.size_of_screen_y)
        WhichArray[22].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue4 - self.size_of_screen_y)
        WhichArray[23].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue4 - self.size_of_screen_y)
        WhichArray[24].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue4 - self.size_of_screen_y)
        WhichArray[25].position = (0, self.size_of_screen_y * self.yvalue5 - self.size_of_screen_y)
        WhichArray[26].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue5 - self.size_of_screen_y)
        WhichArray[27].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue5 - self.size_of_screen_y)
        WhichArray[28].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue5 - self.size_of_screen_y)
        WhichArray[29].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue5 - self.size_of_screen_y)
        WhichArray[30].position = (0, self.size_of_screen_y * self.yvalue6 - self.size_of_screen_y)
        WhichArray[31].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue6 - self.size_of_screen_y)
        WhichArray[32].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue6 - self.size_of_screen_y)
        WhichArray[33].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue6 - self.size_of_screen_y)
        WhichArray[34].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue6 - self.size_of_screen_y)
        WhichArray[35].position = (0, self.size_of_screen_y * self.yvalue7 - self.size_of_screen_y)
        WhichArray[36].position = (self.size_of_screen_x * self.xvalue1 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue7 - self.size_of_screen_y)
        WhichArray[37].position = (self.size_of_screen_x * self.xvalue2 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue7 - self.size_of_screen_y)
        WhichArray[38].position = (self.size_of_screen_x * self.xvalue3 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue7 - self.size_of_screen_y)
        WhichArray[39].position = (self.size_of_screen_x * self.xvalue4 - self.size_of_screen_x, self.size_of_screen_y * self.yvalue7 - self.size_of_screen_y)
    
    def startup(self):
        if globals.GenStartingItems == 0:
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            for Gems in range(random.randint(0,1)):
                self.CreateGem(random.randint(0,5), random.randint(1,100))
            for Items in range(random.randint(0,1)):
                self.CreateItem(random.randint(90,100), Inventory, random.randint(1,4))
            self.CreateItem(random.randint(1,100), EquippedSlot1, int(1))
            self.CreateItem(random.randint(1,100), EquippedSlot2, int(2))
            self.CreateItem(random.randint(1,100), EquippedSlot3, int(3))
            self.CreateItem(random.randint(1,100), EquippedSlot4, int(4))
            globals.GenStartingItems = 1
    
    def SetupEquippedFrames(self, WhichImage, WhichPosition):
        self.EquippedFrames.append(SpriteNode('assets/MainMenu/gradient.JPG',
                                          parent = self,
                                          scale = 0.4,
                                          color = '#ffffff',
                                          anchor_point = (0, 0),
                                          size = (self.screen_center_x / 2, self.screen_center_y / 1.52)))
        self.EquippedFrames.append(SpriteNode(WhichImage,
                                          parent = self,
                                          scale = 0.2,
                                          alpha = 0.5,
                                          anchor_point = (0, 0)))
        self.EquippedFrames.append(SpriteNode('assets/Classes/frame-8-grey.png',
                                          parent = self,
                                          scale = 0.4,
                                          anchor_point = (0, 0)))
        self.EquippedText.append(LabelNode(text = '',
                                          parent = self,
                                          scale = 1,
                                          font = ('CopperPlate', 10),
                                          color = '#ffffff',
                                          anchor_point = (0, 0)))
        self.EquippedFrames[len(self.EquippedFrames)-1].position = WhichPosition
        self.EquippedFrames[len(self.EquippedFrames)-2].position = WhichPosition
        self.EquippedFrames[len(self.EquippedFrames)-3].position = WhichPosition
        self.EquippedText[len(self.EquippedText)-1].position = WhichPosition
