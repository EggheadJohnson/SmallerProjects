# Axis and Allies: World War I is a boardgame where players are one of seven different World War I
# powers.  Two important aspects of this game are battles and purchasing units.  This program
# simulates the battles with a Monte Carlo simulation and calculates all the possible purchasing
# options based on how much the player is able to spend.
# Paul Johnson
# Spring 2014

from random import randint
import os

# This recursively builds the players options.

def howMany(IPCs):
    if IPCs < 3: return IPCs
    options = { 'Battleship':12, 'Cruiser':9, 'Sub':6, 'Artillery':4, 'Infantry':3}
    thisRun = []
    for piece in options.keys():
        if options[piece] <= IPCs:
            thisRun.append( [piece] )
    for piece in thisRun:
        piece.append(howMany(IPCs-options[piece[0]]))
    return thisRun



# This recursively prints the players options.

def printOptions(options, root='', lists = []):
    
    for x in options:

        if isinstance(x[1],list):
            printOptions(x[1],root+x[0]+' ', lists)
        elif isinstance(x[1],int):
            lists.append( root+x[0]+' ')
    return lists

# This is the last step of organization before printing.

def organizeOptions(listOfOptions):
    result = []
    for set in listOfOptions:
        tempResult = []
        set = set.split()
        set.sort()
        added = 0
        
        for x in result:
            if set > x or added:
                tempResult.append(x)
            if set == x and not added:
                added = 1
                tempResult.append(x)
            if set < x and not added:
                added = 1
                tempResult.append(set)
                tempResult.append(x)
        if not added: tempResult.append(set)
        
        result = tempResult
    temp = []
    for r in result:
        temp.append(condense(r))
    result = temp
    return result

# The function howMany makes a list of options that will repeat the same unit multiple times
# The function condense just counts up how many instances of each unit are in the list and iterates a counter.

def condense(shortList):
    counter = {}
    for unit in shortList:
        if unit in counter.keys():
            counter[unit]+=1
        else:
            counter[unit] = 1
    return counter

# This prints the options.

def actuallyPrint(printDict):
    costs = { 'Battleship':12, 'Cruiser':9, 'Sub':6, 'Artillery':4, 'Infantry':3}

    for option in printDict:
        line = '   '
        cost = 0
        for unit in option.keys():
            cost += option[unit]*costs[unit]
            line += str(option[unit]) + ' ' + unit + ' '
        line += 'for ' + str(cost)
        print line

# This eliminates duplicate options.

def orderAndEliminate(l):
    result = []

    for item in l:
        temp = []
        added = 0
        for resultItem in result:
            if item > resultItem or added:
                temp.append(resultItem)
            if item == resultItem and not added:
                added = 1
                temp.append(resultItem)
            if item < resultItem and not added:
                added = 1
                temp.append(item)
                temp.append(resultItem)

        if not added: temp.append(item)
        result = temp
        
        
    return result



# Here is the Monte Carlo simulation for a battle.  There are a lot of pieces that can be involved
# and that has a huge impact on the battle.  This also makes it slow to enter the information.
# As such, you can put a list of how many units in as a parameter.  The order should be the same
# as they would be entered.  Each unit has a different effect on the battle and the other units.
# Each unit has a different hit die to represent the chances of a successful attack.  This
# code just sets that all up and runs the Monte Carlo.

def whatAreMyChances(runs=10000, l = []):
    if not l:
        attacking_planes = input("How many planes are attacking? ")
        attacking_infantry = input("How many infantry are attacking? ")
        attacking_artillery = input("How many artillery are attacking? ")
        attacking_tanks = input("How many tanks are attacking? ")
        attacking_boats = input("How many boats are attacking? ")
        defending_planes = input("How many planes are defending? ")
        defending_infantry = input("How many infantry are defending? ")
        defending_artillery = input("How many artillery are defending? ")
        defending_tanks = input("How many tanks are defending? ")
    else:
        attacking_planes = l[0]
        attacking_infantry = l[1]
        attacking_artillery = l[2]
        attacking_tanks = l[3]
        attacking_boats = l[4]
        defending_planes = l[5]
        defending_infantry = l[6]
        defending_artillery = l[7]
        defending_tanks = l[8]
    attacker_planes_destroyed = 0
    attacking_infantry_plus = 0
    attacking_artillery_plus = 0
    attacking_tanks_plus = 0
    defender_planes_destroyed = 0
    defending_artillery_plus = 0



    attackResults = [0]
    defenseResults = [0]
    total_attackers = attacking_infantry+attacking_artillery+attacking_tanks+attacking_boats
    total_defenders = defending_infantry+defending_artillery+defending_tanks
    for x in range(total_attackers):
        defenseResults.append(0)
    for x in range(total_defenders):
        attackResults.append(0)
    for x in range(runs):
        attacker_air_supremacy = defender_air_supremacy = 0
        attackers_destroyed = defenders_destroyed = 0
        while attacking_planes and defending_planes:
            attRes = []
            defRes = []
            attacker_planes_destroyed = defender_planes_destroyed = 0
            for y in range(attacking_planes):
                attRes.append(randint(1,6))
            for y in range(defending_planes):
                defRes.append(randint(1,6))
            for y in attRes:
                if y <= 2: attacking_planes -= 1
            for y in defRes:
                if y <= 2: defending_planes -= 1
            attacking_planes = floorOfZero(attacking_planes)
            defending_planes = floorOfZero(defending_planes)
        attacker_air_supremacy = attacking_planes
        defender_air_supremacy = defending_planes
        attacking_planes = l[0]
        defending_planes = l[5]
        if attacking_artillery and attacking_infantry:
            diff = floorOfZero(attacking_infantry - attacking_artillery)
            if diff:
                attacking_infantry_plus = attacking_artillery
                attacking_infantry -= attacking_artillery
            else:
                attacking_infantry_plus = attacking_infantry
                attacking_infantry = 0
        if attacking_tanks and attacking_artillery:
            diff = floorOfZero(attacking_infantry - attacking_artillery)
            if diff:
                attacking_tanks_plus = attacking_artillery
                attacking_tanks -= attacking_artillery
            else:
                attacking_tanks_plus = attacking_infantry
                attacking_tanks = 0
        if attacking_artillery and attacker_air_supremacy:
            attacking_artillery_plus = attacking_artillery
            attacking_artillery = 0


        for y in range(attacker_air_supremacy):
            if randint(1,6) <= 2: defenders_destroyed += 1
        for y in range(attacking_infantry):
            if randint(1,6) <= 2: defenders_destroyed+=1
        for y in range(attacking_infantry_plus):
            if randint(1,6) <= 3: defenders_destroyed+=1
        for y in range(attacking_artillery):
            if randint(1,6) <= 3: defenders_destroyed+=1
        for y in range(attacking_artillery_plus):
            if randint(1,6) <= 4: defenders_destroyed+=1
        for y in range(attacking_tanks):
            attackers_destroyed -= 1
            if randint(1,6) <=2: defenders_destroyed += 1
        for y in range(attacking_tanks_plus):
            attackers_destroyed -= 1
            if randint(1,6) <=2: defenders_destroyed += 1
        for y in range(attacking_boats):
            if randint(1,6) <= 4: defenders_destroyed += 1
        if defender_air_supremacy:
            defending_artillery_plus = defending_artillery
            defending_artillery = 0

        for y in range(defender_air_supremacy):
            if randint(1,6) <= 2: attackers_destroyed += 1
        for y in range(defending_infantry):
            if randint(1,6) <= 3: attackers_destroyed+=1
        for y in range(defending_artillery):
            if randint(1,6) <= 3: attackers_destroyed+=1
        for y in range(defending_artillery_plus):
            if randint(1,6) <= 4: attackers_destroyed+=1
        for y in range(defending_tanks):
            if randint(1,6) <=1: attackers_destroyed += 1
        attackers_destroyed = floorOfZero(attackers_destroyed)
        if attackers_destroyed > total_attackers: attackers_destroyed = total_attackers
        if defenders_destroyed > total_defenders: defenders_destroyed = total_defenders

        attackResults[defenders_destroyed]+=1
        defenseResults[attackers_destroyed]+=1
    return attackResults, defenseResults


# floorOfZero is here because you don't want to end up with negative units after a battle.

def floorOfZero(n):
    if n >= 0: return n
    else: return 0

# This prints the results of the battle.  It displays them as a series of probabilities for how
# many units each side may lose.

def printResults(results):
    attackers = results[0]
    defenders = results[1]
    print ''
    for att in range(len(attackers)):
        line = 'The defenders lose: ' + str(att) + ' with ' + str(attackers[att]/100.) + '% probability'
        print line
    print ''
    for defe in range(len(defenders)):
        line = 'The attackers lose: ' + str(defe) + ' with ' + str(defenders[defe]/100.) + '% probability'
        print line
    print ''

# Used to check if the player entered a number that can be an integer.

def canBeInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# Runs the whole thing.

def run():
    print "Welcome to my Axis and Allies WWI Edition Computer!"
    print "What would you like to do?"
    print "   1 - Determine your odds in a given attack"
    print "   2 - Determine your choices in purchasing given your resources"
    selection = raw_input(" Your choice: ")
    while not canBeInt(selection):
        print "You must select either 1 or 2"
        print "   1 - Determine your odds in a given attack"
        print "   2 - Determine your choices in purchasing given your resources"
        selection = raw_input(" Your choice: ")
    if selection == '1':
        run = whatAreMyChances()
        printResults(run)
    elif selection == '2':
        IPCs = raw_input("How many IPCs do you have to spend? ")
        while not canBeInt(IPCs):
            print "IPCs must be an integer"
            IPCs = raw_input("How many IPCs do you have to spend? ")
        IPCs = int(IPCs)
        if IPCs < 3: print "You cannot purchase anything this round"
        elif IPCs >= 3:
            l = howMany(IPCs)
            l = printOptions(l)
            l = orderAndEliminate(l)
            d = organizeOptions(l)
            actuallyPrint(d)
            
run()
