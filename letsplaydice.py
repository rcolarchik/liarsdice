from random import *
from time import sleep
from pprint import pprint as pp
from datetime import datetime


## Constants
NOOFDICE = 5
dicelayout = 'row' #row or column
nonewline = 50


removedielist = ['Lost a Die', 'Remove a Dice', 'Lost a Dice', 'Remove a Die', 'Lost']
validinputn = ['End Game', 'Roll'] + removedielist
validinput =[]

for i in validinputn:
    x = i.upper()
    validinput.append(x)

def getinput(inputdescriptor):
    x = input(inputdescriptor)
    validinputsset = set(validinput)
    if x.upper() in validinputsset:
        return x.lower()
    else:
        y =inputdescriptor
        print('Not a valid input. Try:\n')
        for i in validinput:
            print(i)
        print('\n')
        getinput(y)
    

def makedice(row1, row2, row3):
    top =' ------- \n'
    bottom = ' ------- '
    x = top + row1 + row2 + row3 + bottom
    return x

def mkdicedict():
    diceemptyrow = '|       |\n'
    dice1dotleft = '| *     |\n'
    dice1dotright = '|     * |\n'
    dice2dot = "| *   * |\n"
    dice1dotcenterrow = '|   *   |\n'

    dice1 = makedice(diceemptyrow, dice1dotcenterrow, diceemptyrow) 
    dice2 = makedice(dice1dotleft, diceemptyrow, dice1dotright) 
    dice3 = makedice(dice1dotleft, dice1dotcenterrow, dice1dotright) 
    dice4 =  makedice(dice2dot,diceemptyrow,dice2dot)
    dice5 = makedice(dice2dot, dice1dotcenterrow, dice2dot) 
    dice6 = makedice(dice2dot, dice2dot, dice2dot)

    dicedict = {'1': dice1,'2':dice2,'3':dice3,'4':dice4,'5':dice5,'6':dice6} 
    return dicedict
def dice2dict(dice,values,nodice):
    dicedict = {}
    for i in range(nodice):
        dicedictkey = str(dice[i]) 
        dicedictval = values[dicedictkey]
        dicedict[i] = dicedictval
    return dicedict
def roworcolumn(orientation,dictionary, nodice):
    if orientation == 'row':
        templist = []
        listofstrings = ['','','','','']

        for i in range(nodice):
            dice = dictionary[i]
            templist = dice.split('\n')
            #print(templist)
            for i in range(len(templist)):
                x = listofstrings[i] 
                y = x + templist[i] + '  '
                listofstrings[i] = y
        final = '\n'.join(listofstrings)
        for i in range(nonewline):
            print('\n')
        print(str(datetime.now(tz=None)))
        print(final)
    elif orientation == 'column':
        print(str(datetime.now(tz=None)))
        for i in range(nonewline):
            print('\n')
        for i in range(nodice):
            dice = dictionary[i]
            print(dice)
        
        
            


def main():
    dicedict = mkdicedict()
    numberofdice = NOOFDICE
    endgame = ''
    removedi = ''
    orientation = dicelayout
    while endgame.lower() != 'end game':
        if removedi.lower() in set([x.lower() for x in removedielist]):
            numberofdice = numberofdice-1
        else:
            pass
        tempdict = {}
        for i in range(numberofdice):
            tempdict[i] = randint(1,6)
            currentdict = tempdict
        ran2dice = dice2dict(currentdict,dicedict,numberofdice)
        roworcolumn(orientation,ran2dice,numberofdice)
        temp = getinput("What's next? ")
        endgame = temp
        removedi = temp
        
        

main()