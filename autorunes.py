import pyautogui
import keyboard
import json
import time

CONFIDENCE = 0.8

def editPage():
    while keyboard.is_pressed('alt') != True:
        locale = pyautogui.locateOnScreen('./images/edit.png', confidence = CONFIDENCE)
        if locale != None:
            print(locale)
            pyautogui.click(locale)
            time.sleep(3)
            return

def savePage():
    pyautogui.click(pyautogui.locateOnScreen('./images/save.png', confidence = CONFIDENCE))


def selectRune(champion):
    f = open('{}.json'.format(champion))
    data = json.load(f)
    while keyboard.is_pressed('alt') != True:
        mainType = data['main']['type']
        mainPath = './images/{}/'.format(mainType)
        mainFirst = data['main']['first']
        mainSecond = data['main']['second']
        mainThird = data['main']['third']
        mainFourth = data['main']['fourth']
        # locale = pyautogui.locateOnScreen('./images/empty_icon.PNG', confidence = CONFIDENCE)
        print('try to click', mainPath + mainType + '_' + mainFirst + '.PNG')
        locale = pyautogui.locateOnScreen(mainPath + mainType + '_' + mainFirst + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        locale = pyautogui.locateOnScreen(mainPath + mainType + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        locale = pyautogui.locateOnScreen(mainPath + mainType + '_' + mainFirst + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        locale = pyautogui.locateOnScreen(mainPath + mainType + '_' + mainSecond + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        locale = pyautogui.locateOnScreen(mainPath + mainType + '_' + mainThird + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        locale = pyautogui.locateOnScreen(mainPath + mainType + '_' + mainFourth + '.PNG', confidence = CONFIDENCE)
        if locale != None:
            pyautogui.click(locale)
        return

def chooseChampion():
        champion = input('Choose you champion: ')
        editPage()
        selectRune(champion)

def setRune():
    print('You are in the set rune')
    runes = ['', 'domination', 'inspiration', 'precision', 'resolve', 'sorcery']
    champion = input('For which champion are setting this rune for? ')
    mainRune = int(input('Select main rune: (1)Domination ; (2)Inspiration ; (3)Precision ; (4)Resolve ; (5)Sorcery '))
    while mainRune != 1 and mainRune != 2 and mainRune != 3 and mainRune != 4 and mainRune != 5:
        mainRune = int(input('Main rune must be one of these: (1)Domination ; (2)Inspiration ; (3)Precision ; (4)Resolve ; (5)Sorcery '))
        
    if(mainRune == 1):
        selectedMainSpells = selectDomination(True)
    elif(mainRune == 2):
        selectedMainSpells = selectInspiration(True)
    elif(mainRune == 3):
        selectedMainSpells = selectPrecision(True)
    elif(mainRune == 4):
        selectedMainSpells = selectResolve(True)
    elif(mainRune == 5):
        selectedMainSpells = selectSorcery(True)
       
        
    secondaryRune = int(input('Select secondary rune: (1)Domination ; (2)Inspiration ; (3)Precision ; (4)Resolve ; (5)Sorcery'))
    while secondaryRune != 1 and secondaryRune != 2 and secondaryRune != 3 and secondaryRune != 4 and secondaryRune != 5:
        secondaryRune = int(input('Secondary rune must be one of these: (1)Domination ; (2)Inspiration ; (3)Precision ; (4)Resolve ; (5)Sorcery '))
    
    if(secondaryRune == 1):
        selectedSecondarySpells = selectDomination(False)
    elif(secondaryRune == 2):
        selectedSecondarySpells = selectInspiration(False)
    elif(secondaryRune == 3):
        selectedSecondarySpells = selectPrecision(False)
    elif(secondaryRune == 4):
        selectedSecondarySpells = selectResolve(False)
    elif(secondaryRune == 5):
        selectedSecondarySpells = selectSorcery(False)
    
    runes = {
        'main': selectedMainSpells,
        'secondary': selectedSecondarySpells
    }
    with open("{}.json".format(champion), 'w') as f:
        json.dump(runes, f)


def selectDomination(isMainRune):
    if(isMainRune):
        firstSpells = ['', 'electrocute', 'predator', 'dark_harvest', 'hail_of_blades']
        secondSpells = ['', 'cheap_shot', 'taste_of_blood', 'sudden_impact']
        thirdSpells = ['', 'zombie_ward', 'ghost_poro', 'eyeball_collection']
        fourthSpells = ['', 'ravenous_hunter', 'ingenious_hunter', 'relentless_hunter', 'ultimate_hunter']
        firstSpell = int(input('Select the first one: (1)Electrocute ; (2)Predator ; (3)Dark Harvest ; (4)Hail of Blades '))
        secondSpell = int(input('Select the second one: (1)Cheap Shot ; (2)Taste of Blood ; (3)Sudden Impact '))
        thirdSpell = int(input('Select the third one: (1)Zombie Ward ; (2)Ghost Poro ; (3)Eyeball Collection '))
        fourthSpell = int(input('Select the fourth one: (1)Ravenous Hunter ; (2)Ingenious Hunter ; (3)Relentless Hunter ; (4)Ultimate Hunter '))
        selectedMainSpells = {
            'type': 'domination',
            'first': firstSpells[firstSpell],
            'second': secondSpells[secondSpell],
            'third': thirdSpells[thirdSpell],
            'fourth': fourthSpells[fourthSpell]
        }
        return selectedMainSpells
    else:
        spells = ['', 'cheap_shot', 'taste_of_blood', 'sudden_impact', 'zombie_ward', 'ghost_poro', 'eyeball_collection', 'ravenous_hunter', 'ingenious_hunter', 'relentless_hunter', 'ultimate_hunter']
        firstSpell = int(input('Select the first one: (1)Cheap Shot ; (2)Taste of Blood ; (3)Sudden Impact ; (4)Zombie Ward ; (5)Ghost Poro ; (6)Eyeball Collection ; (7)Ravenous Hunter ; (8)Ingenious Hunter ; (9)Relentless Hunter ; (10)Ultimate Hunter '))
        secondSpell = int(input('Select the first one: (1)Cheap Shot ; (2)Taste of Blood ; (3)Sudden Impact ; (4)Zombie Ward ; (5)Ghost Poro ; (6)Eyeball Collection ; (7)Ravenous Hunter ; (8)Ingenious Hunter ; (9)Relentless Hunter ; (10)Ultimate Hunter '))
        selectedSecondarySpells = {
            'type': 'domination',
            'first': spells[firstSpell],
            'second': spells[secondSpell]
        }
        return selectedSecondarySpells

def selectInspiration():
    print('Selected 2')

def selectPrecision():
    print('Selected 3')
    
def selectResolve():
    print('Selected 4')
    
def selectSorcery(isMainRune):
    if(isMainRune):
        firstSpells = ['', 'summon_aery', 'arcane_Comet', 'phase_rush']
        secondSpells = ['', 'nullifying_orb', 'manaflow_band', 'nimbus_cloak']
        thirdSpells = ['', 'transcendence', 'celerity', 'absolute_focus']
        fourthSpells = ['', 'scorch', 'waterwalking', 'gathering_storm']
        firstSpell = int(input('Select the first one: (1)Summon Aery ; (2)Arcane Comet ; (3)Phase Rush '))
        secondSpell = int(input('Select the second one: (1)Nullifying Orb ; (2)Manaflow Band ; (3)Nimbus Cloak '))
        thirdSpell = int(input('Select the third one: (1)Transcendence ; (2)Celerity ; (3)Absolute Focus '))
        fourthSpell = int(input('Select the fourth one: (1)Scorch ; (2)Waterwalking ; (3)Gathering Storm '))
        selectedMainSpells = {
            'type': 'sorcery',
            'first': firstSpells[firstSpell],
            'second': secondSpells[secondSpell],
            'third': thirdSpells[thirdSpell],
            'fourth': fourthSpells[fourthSpell]
        }
        return selectedMainSpells
    else:
        spells = ['', 'nullifying_orb', 'manaflow_band', 'nimbus_cloak', 'transcendence', 'celerity', 'absolute_focus', 'scorch', 'waterwalking', 'gathering_storm']
        firstSpell = int(input('Select the first one: (1)Nullifying Orb ; (2)Manaflow Band ; (3)Nimbus Cloak ; (4)Transcendence ; (5)Celerity ; (6)Absolute Focus ; (7)Scorch ; (8)Waterwalking ; (9)Gathering Storm '))
        secondSpell = int(input('Select the first one: (1)Nullifying Orb ; (2)Manaflow Band ; (3)Nimbus Cloak ; (4)Transcendence ; (5)Celerity ; (6)Absolute Focus ; (7)Scorch ; (8)Waterwalking ; (9)Gathering Storm '))
        selectedSecondarySpells = {
            'type': 'sorcery',
            'first': spells[firstSpell],
            'second': spells[secondSpell]
        }
        return selectedSecondarySpells

def main():
    action = ''
    while action != '1' and action != '2':
        action = input('(1) Set Runes for Champion \n(2) Choose Champion\n')
        if action == '1':
            setRune()
        else:   
            chooseChampion()
    # selectRuna()
    
    
main()
