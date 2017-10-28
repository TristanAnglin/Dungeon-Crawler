import random
import globals

class Classes():
    # ---- Ranged ---- #
    global MainStatMage
    MainStatMage = 'Intellect'
    global ResourceMage
    ResourceMage = 'Mana'
    global trait1Mage
    trait1Mage = 1
    global trait1descriptionMage
    trait1descriptionMage = '[' + str(trait1Mage) + '%] chance when you damage an enemy to gain a charge of ice. When you collect 10 charges, you will explode\nkilling all enemies in a 15ft range. Maximum of ' + str(trait1Mage*3) + '%.'
    global trait2Mage
    trait2Mage = 2.75
    global trait2descriptionMage
    trait2descriptionMage = 'Increase your versatility by an additional [' + str(trait2Mage) + '%]. Maximum of ' + str(trait2Mage*3) + '%.'
    global trait3Mage
    trait3Mage = 12
    global trait3bMage
    trait3bMage = 45
    global trait3descriptionMage
    trait3descriptionMage = str(trait3Mage) + '% chance when you deal damage to cause an additional ' + str(trait3bMage) + '% damage.'
    global trait4Mage
    trait4Mage = 40
    global trait4bMage
    trait4bMage = 5
    global trait4cMage
    trait4cMage = 1.5
    global trait4descriptionMage
    trait4descriptionMage = 'Gain an aura of frost, slowing the attack and movement speed of enemies that touch you by ' + str(trait4Mage) + '% for ' + str(trait4bMage) + ' seconds.\nWhen you slow an enemy that is not already affected by movement impairing effects, heal yourself for up to ' + str(trait4cMage) + '%\nof your maximum health.'
    
    global MainStatDruid
    MainStatDruid = 'Intellect'
    global ResourceDruid
    ResourceDruid = 'Mana'
    global trait1Druid
    trait1Druid = 6
    global trait1descriptionDruid
    trait1descriptionDruid = 'Increase your movement speed by an additional [' + str(trait1Druid) + '%]. Maximum of ' + str(trait1Druid*3) + '%.'
    global trait2Druid
    trait2Druid = 10
    global trait2descriptionDruid
    trait2descriptionDruid = 'Increase your critical strike damage by an additional [' + str(trait2Druid) + '%]. Maximum of ' + str(trait2Druid*3) + '%.'
    global trait3Druid
    trait3Druid = 33
    global trait3bDruid
    trait3bDruid = 12.5
    global trait3cDruid
    trait3cDruid = 3
    global trait3descriptionDruid
    trait3descriptionDruid = str(trait3Druid) + '% chance on hit for your enemies to bleed for an addition ' + str(trait3bDruid) + '% of the damage you dealt over ' + str(trait3cDruid) + ' seconds.'
    global trait4Druid
    trait4Druid = 2
    global trait4bDruid
    trait4bDruid = 2.5
    global trait4descriptionDruid
    trait4descriptionDruid = 'Heal yourself for ' + str(trait4Druid) + '% of your maximum health every ' + str(trait4bDruid) + ' seconds.'
    
    global MainStatShaman
    MainStatShaman = 'Intellect'
    global ResourceShaman
    ResourceShaman = 'Maelstrom'
    global trait1Shaman
    trait1Shaman = 6
    global trait1descriptionShaman
    trait1descriptionShaman = '[' + str(trait1Shaman) + '%] chance when attacked to heal yourself for 60% of the damage taken in the past 5 seconds, over 2 seconds.\nMaximum of ' + str(trait1Shaman*3) + '%.'
    global trait2Shaman
    trait2Shaman = 4
    global trait2descriptionShaman
    trait2descriptionShaman = 'Increase maximum health by [4%]. Maximum of 12%.'
    global trait3Shaman
    trait3Shaman = 7
    global trait3descriptionShaman
    trait3descriptionShaman = '7% chance when you deal damage to call on the aspect of the wolf, granting a 20% increased damage buff for 5\nseconds.'
    global trait4Shaman
    trait4Shaman = 7
    global trait4descriptionShaman
    trait4descriptionShaman = '7% chance when hit to call on the aspect of the bear, granting 50% reduced damage taken for 5 seconds.'
    
    
    
    
    global MainStatWarlock
    MainStatWarlock = 'Intellect'
    
    global ResourceWarlock
    ResourceWarlock = 'Corruption'
    
    global trait1descriptionWarlock
    trait1descriptionWarlock = str('Increase haste by [2.5%]. Maximum of 7.5%')
    global trait1Warlock
    trait1Warlock = 2.5
    
    global trait2descriptionWarlock
    trait2descriptionWarlock = str('Increase critical strike chance by [2.5%]. Maximum of 7.5%')
    global trait2Warlock
    trait2Warlock = 2.5
    
    global trait3descriptionWarlock
    trait3descriptionWarlock = str('Gain leech, healing you for 14% of the damage you deal')
    global trait3Warlock
    trait3Warlock = 4
    
    global trait4descriptionWarlock
    trait4descriptionWarlock = str('Empower yourself with darkness, giving you a 6% chance when you deal damage to weaken\nyour target for 5 seconds, increasing the damage they take by 35%')
    global trait4Warlock
    trait4Warlock = 6
    
    # ---- Melee ---- #
    global MainStatRogue
    MainStatRogue = 'Agility'
    
    global ResourceRogue
    ResourceRogue = 'Energy'
    
    global trait1descriptionRogue
    trait1descriptionRogue = str('Gain dodge, [2.5%] chance to take no damage from an enemies attack. Maximum of 7.5%')
    global trait1Rogue
    trait1Rogue = 2.5
    
    global trait2descriptionRogue
    trait2descriptionRogue = str('Increase agility by [1.25%]. Maximum of 3.75%')
    global trait2Rogue
    trait2Rogue = 1.25
    
    global trait3descriptionRogue
    trait3descriptionRogue = str('Apply a deadly poison to your weapon, dealing an addition 10% damage on your attacks over\n2 seconds')
    global trait3Rogue
    trait3Rogue = 10
    
    global trait4descriptionRogue
    trait4descriptionRogue = str('20% chance when attacked while below 60% health to drink a potion, healing you for 40% of your\nmaximum health over 6 seconds')
    global trait4Rogue
    trait4Rogue = 20
    
    
    
    global MainStatDeathKnight
    MainStatDeathKnight = 'Strength'
    
    global ResourceDeathKnight
    ResourceDeathKnight = 'Rage'
    
    global trait1descriptionDeathKnight
    trait1descriptionDeathKnight = str('[12%] Chance when you deal a critical strike to an enemy to hit the next closest enemy for the\nsame amount. Maximum of 36%')
    global trait1DeathKnight
    trait1DeathKnight = 12
    
    global trait2descriptionDeathKnight
    trait2descriptionDeathKnight = str('Gain absorption, protecting you from up to [4%] of your maximum health in additional damage.\nThis effect regenerates at a rate of 1% every 2 seconds. Maximum of 12%')
    global trait2DeathKnight
    trait2DeathKnight = 4
    
    global trait3descriptionDeathKnight
    trait3descriptionDeathKnight = str('When you die, revive yourself to 40% health. Each additional death reduces the chance to\nrevive yourself by 75% [100%, 25%, 6.25%, 1.5%]')
    global trait3DeathKnight
    trait3DeathKnight = 40
    
    global trait4descriptionDeathKnight
    trait4descriptionDeathKnight = str('10% chance when you kill an enemy for them to resurrect as a skeleton at 65% of their initial\nmaximum health and damage to fight for you for 1 minute or until they are killed again')
    global trait4DeathKnight
    trait4DeathKnight = 10
    
    
    
    global MainStatMonk
    MainStatMonk = 'Agility'
    
    global ResourceMonk
    ResourceMonk = 'Spirit'
    
    global trait1descriptionMonk
    trait1descriptionMonk = str('[8%] chance when you deal damage to an enemy to stun them, rendering them unable to move\nor attack for 6 seconds. Maximum of 24%')
    global trait1Monk
    trait1Monk = 8
    
    global trait2descriptionMonk
    trait2descriptionMonk = str('Increase maximum spirit and spirit regeneration by [5%]. Maximum of 15%')
    global trait2Monk
    trait2Monk = 5
    
    global trait3descriptionMonk
    trait3descriptionMonk = str('5% chance when hit to fade into your spirit form, taking no damage for 3 seconds')
    global trait3Monk
    trait3Monk = 5
    
    global trait4descriptionMonk
    trait4descriptionMonk = str('10% chance when hit while below 40% health to knockback all nearby enemies and heal yourself\nfor 30% health. ')
    global trait4Monk
    trait4Monk = 10
    
    
    
    global MainStatPaladin
    MainStatPaladin = 'Strength'
    
    global ResourcePaladin
    ResourcePaladin = 'Light'
    
    global trait1descriptionPaladin
    trait1descriptionPaladin = str('Damage taken reduced by [7%]. Maximum of 21%')
    global trait1Paladin
    trait1Paladin = 8
    
    global trait2descriptionPaladin
    trait2descriptionPaladin = str('Increase strength, haste and critical strike chance by [3%]. Maximum of 9%')
    global trait2Paladin
    trait2Paladin = 3
    
    global trait3descriptionPaladin
    trait3descriptionPaladin = str('When you kill an enemy, send them to hell, briefly healing you for 6% of their maximum health.')
    global trait3Paladin
    trait3Paladin = 5
    
    global trait4descriptionPaladin
    trait4descriptionPaladin = str('20% chance to cleanse yourself of all negative effects when you take damage.')
    global trait4Paladin
    trait4Paladin = 20
