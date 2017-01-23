# 2048 is a very popular game.  Countless variations have been created around it.  Many students
# lost class time to trying to achieve a highscore.  I was curious as to whether it would be
# possible to get to 2048 randomly.  It's not.  This program is designed to run a Monte Carlo
# simulation of the game as many times as you want.  The most I ran was 2 million.  The highest
# score achieved was never more than 512.
# Paul Johnson
# Spring 2014

from random import randint, choice

def makeNewBoard():
    b = []
    for x in range(4): b.append([0,0,0,0])
    added = 0
    while added<2:
        x = randint(0,3)
        y = randint(0,3)
        if not b[x][y]:
            b[x][y] = 2
            added+=1
    return b

def addNew(b):
    options = []
    for x in range(4):
        for y in range(4):
            if not b[x][y]: options.append((x,y))
    addHere = choice(options)
    b[addHere[0]][addHere[1]] = choice([2,2,2,2,2,2,2,4])


def printBoard(b):
    for line in b:
        outPut = ''
        for item in line:
            outPut += str(item)
            outPut += ' '
        print outPut
    print '\n'

def makeAMove(b, move):
    tempB = []
    moveOccurred = False
    for x in range(4):
        tempB.append([[],[],[],[]])
        for y in range(4):
            tempB[x][y] = [b[x][y],0]
    if move == 'down':
        for y in range(4):
            for x in range(3):
                c = 2-x
                for z in range(c+1, 4):
                    if tempB[z][y] == [0,0] and z == 3 and tempB[c][y][0]:
                        tempB[z][y] = tempB[c][y]
                        tempB[c][y] = [0,0]
                        moveOccurred = True
                    elif ((tempB[z][y][0] != tempB[c][y][0] and tempB[z][y][0] != 0) or tempB[z][y][1]) == 1 and tempB[c][y][0]:
                        tempB[z-1][y] = tempB[c][y]
                        if z>c+1:
                            tempB[c][y] = [0,0]
                            moveOccurred = True
                        break
                    elif tempB[z][y][0] == tempB[c][y][0] and tempB[z][y][1] == 0 and tempB[z][y][0] and tempB[c][y][0]:
                        tempB[z][y][1] = 1
                        tempB[c][y] = [0,0]

                        moveOccurred = True
                        break
    if move == 'right':
        for x in range(4):
            for y in range(3):
                c = 2-y
                for z in range(c+1, 4):
                    if tempB[x][z] == [0,0] and z == 3 and tempB[x][c][0]:
                        tempB[x][z] = tempB[x][c]
                        tempB[x][c] = [0,0]
                        moveOccurred = True
                    elif ((tempB[x][z][0] != tempB[x][c][0] and tempB[x][z][0] != 0) or tempB[x][z][1]) == 1 and tempB[x][c][0]:
                        tempB[x][z-1] = tempB[x][c]
                        if z>c+1:
                            tempB[x][c] = [0,0]
                            moveOccurred = True
                        break
                    elif tempB[x][z][0] == tempB[x][c][0] and tempB[x][z][1] == 0 and tempB[x][z][0] and tempB[x][c][0]:
                        tempB[x][z][1] = 1
                        tempB[x][c] = [0,0]

                        moveOccurred = True
                        break
    if move == 'up':
        for y in range(4):
            for c in range(1,4):
                for z in range(1,c+1):
                    if tempB[c-z][y] == [0,0] and c-z == 0 and tempB[c][y][0]:
                        tempB[c-z][y] = tempB[c][y]
                        tempB[c][y] = [0,0]
                        moveOccurred = True
                    elif ((tempB[c-z][y][0] != tempB[c][y][0] and tempB[c-z][y][0] != 0) or tempB[c-z][y][1]) == 1 and tempB[c][y][0]:
                        myTemp = tempB[c][y]
                        tempB[c][y] = [0,0]
                        tempB[c-z+1][y] = myTemp
                        break
                    elif tempB[c-z][y][0] == tempB[c][y][0] and tempB[c-z][y][1] == 0 and tempB[c-z][y][0] and tempB[c][y][0]:
                        tempB[c-z][y][1] = 1
                        tempB[c][y] = [0,0]

                        moveOccurred = True
                        break
    if move == 'left':
        for x in range(4):
            for c in range(1,4):
                for z in range(1,c+1):
                    if tempB[x][c-z] == [0,0] and c-z == 0 and tempB[x][c][0]:
                        tempB[x][c-z] = tempB[x][c]
                        tempB[x][c] = [0,0]
                        moveOccurred = True
                    elif ((tempB[x][c-z][0] != tempB[x][c][0] and tempB[x][c-z][0] != 0) or tempB[x][c-z][1]== 1)  and tempB[x][c][0]:
                        myTemp = tempB[x][c]
                        tempB[x][c] = [0,0]

                        tempB[x][c-z+1] = myTemp
                        break
                    elif tempB[x][c-z][0] == tempB[x][c][0] and tempB[x][c-z][1] == 0 and tempB[x][c-z][0] and tempB[x][c][0]:
                        tempB[x][c-z][1] = 1
                        tempB[x][c] = [0,0]

                        moveOccurred = True
                        break
    for x in range(4):
        for y in range(4):
            if tempB[x][y][1] == 1: b[x][y] = 2*tempB[x][y][0]
            else: b[x][y] = tempB[x][y][0]
    if moveOccurred: addNew(b)


def keepGoing(b,maxout=False):
    
    for x in range(3):
        for y in range(3):
            if b[x][y] >= 2048 and maxout: return False
            if b[x][y] == 0: return True
            if b[x+1][y] == 0 or b[x+1][y] == b[x][y]: return True
            if b[x][y+1] == 0 or b[x][y+1] == b[x][y]: return True
    for x in range(1,4):
        for y in range(1,4):
            if b[x][y] == 0: return True
            if b[x-1][y] == 0 or b[x-1][y] == b[x][y]: return True
            if b[x][y-1] == 0 or b[x][y-1] == b[x][y]: return True
    return False

def runGame(printMe=False, maxout=False):
    b = makeNewBoard()
    while keepGoing(b, maxout=maxout):
        makeAMove(b, choice(['up','down','right','left']))
        if printMe: printBoard(b)
    max = 0
    if printMe:
        printBoard(b)
    for x in b:
        for y in x:
            if y > max: max = y
    return max

def playMany(runs=5, printMe=False, maxout=False):
    res = {}
    tenper = runs/10
    if not tenper: tenper = 1
    for x in range(runs):
        m = runGame(printMe=printMe, maxout=maxout)
        if m in res.keys(): res[m]+=1
        else: res[m] = 1
        
        if not (x+1)%tenper:
            print x+1, "runs completed"
            printRes(res)

    return res

def printRes(r):
    a = r.keys()
    a.sort()
    tot = 0
    for x in a:
        tot += r[x]
    line = '   '
    for x in a:
        line = '   '
        line += str(x)
        line += ' :: '
        line += str(100.*r[x]/tot)
        line += '%'
        print line
r = playMany(5000, printMe=False, maxout=True)
print "results:"
printRes(r)

