import random
import time
import numpy as np

def rollDices(sides,trail=10000):
    dice = len(sides)

    diceSides =  '/'.join(str(side) for side in sides)
    print("\n😒  Roll {} dices of {} sides for {} times\n".format(dice,diceSides,trail))

    nmax = sum(sides)
    nmin = dice
    points = np.linspace(nmin,nmax,nmax-nmin+1)
    distribution = np.zeros(nmax-nmin+1)

    for times in range(trail):
        point =sum([ random.randint(1,side) for side in sides])  
        distribution[point-nmin]+=1

    distribution = distribution/trail
    

    print('Sum: Probability')
    [print('{:^3}: {}'.format(int(points[n]),distribution[n]))  for n in range(nmax-nmin+1)]
     

  
def runThisStupidCodeAgain():
    # As you want
    rollDices([6,4])
    rollDices([6,6,6])
    # really interesting combination 
    rollDices([1])
  

runThisStupidCodeAgain()

