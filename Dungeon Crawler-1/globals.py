import random

class Globals():
    
    global ClassSelected
    ClassSelected = 0
    
    global Name
    Name = ''
    
    global Class
    Class = ''
    
    global Level
    Level = 1
    
    global Coins
    Coins = 0
    
    global GemShards
    GemShards = 0
    
    # Stats --------------
    
    global TotalStamina
    TotalStamina = 0
    
    global TotalIntellect
    TotalIntellect = 0
    
    global TotalStrength
    TotalStrength = 0
    
    global TotalAgility
    TotalAgility = 0
    
    global TotalGoldPERC
    TotalGoldPERC = 0
    
    global TotalVersatilityPERC
    TotalVersatilityPERC = 0
    
    global TotalSpeedPERC
    TotalSpeedPERC = 0
    
    global TotalLeechPERC
    TotalLeechPERC = 0
    
    global TotalHastePERC
    TotalHastePERC = 0
    
    global TotalCritPERC
    TotalCritPERC = 0
    
    # -------------------
    
    global Inventory 
    Inventory = []
    
    global GenStartingItems
    GenStartingItems = 0
    
    global EquippedSlot1
    EquippedSlot1 = []
    
    global EquippedSlot2
    EquippedSlot2 = []
    
    global EquippedSlot3
    EquippedSlot3 = []
    
    global EquippedSlot4
    EquippedSlot4 = []
    
    global Dungeon1
    Dungeon1 = 0
    
    global Dungeon2
    Dungeon2 = 0
    
    global Trait1Curr
    Trait1Curr = 0
    
    global T1A
    T1A = 0
    
    global Trait2Curr
    Trait2Curr = 0
    
    global T2A
    T2A = 0
    
    global Trait3Curr
    Trait3Curr = 0
    
    global T3A
    T3A = 0
    
    global Trait4Curr
    Trait4Curr = 0
    
    global T4A
    T4A = 0
    
    global UpgradeTraitCost
    UpgradeTraitCost = (125 * Level) + (250 * Trait1Curr) + (250 * Trait2Curr) + (375 * Trait3Curr) + (500 * Trait4Curr)

