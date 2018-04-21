import random
import time
import numpy as np


def rollDices(dice,side,trail=10000):
    print("❤ Roll {} dices of {} sides for {} times\n".format(dice,side,trail))
    global DB
    global SIDE

    SIDE = side
    DB =np.zeros([dice+1,dice*side+1])
    
    result = [ sum([random.randint(1,side) for throw in range(dice)]) for times in range(trail) ]
    mean = sum(result)/trail
    var = sum(pow(np.array(result)-mean,2))/trail
    stdev = pow(var,0.5)


    sumArray = np.linspace(dice,side*dice,side*dice-dice+1)
    distribution = np.array([ pointProbability(dice,int(p)) for p in sumArray])

    theory_mean = sum(sumArray*distribution)
    theory_var = sum(pow(sumArray-theory_mean,2)*distribution)
    theory_std = pow(theory_var,0.5)

    print('Mean>\n theory: {theory:.4f}\n experiment: {exp:.4f}\n error ratio: {ratio:.6f}\n'
        .format(theory=theory_mean,exp=mean,ratio=abs(mean-theory_mean)/theory_mean))

    print('Variance>\n theory: {theory:.4f}\n experiment: {exp:.4f}\n error ratio: {ratio:.6f}\n'
        .format(theory=theory_var,exp=var,ratio=abs(var-theory_var)/theory_var))

    print('Standard deviation>\n theory: {theory:.4f}\n experiment: {exp:.4f}\n error ratio: {ratio:.6f}\n'
        .format(theory=theory_std,exp=stdev,ratio=abs(stdev-theory_std)/theory_std))


# There is a better way to caculate mean value
# using the fact that each dice are indepandent...
# rather than caculate its probability distribution
# credit to ChengHsinHan 👍 (https://github.com/NTHU-Phys-Qubit/SM-2-ChengHsinHan/blob/master/NDice_np.py) 

# but I still keep the recursive method.
# Ref to : https://digitalscholarship.unlv.edu/cgi/viewcontent.cgi?article=1025&context=grrj

def pointProbability(dice,point):
    pointArray = np.linspace(1,SIDE,SIDE)  
    summation = 0

    if dice>1 :
        for now in pointArray:
            now = int(now)
            last = point-now  
            lastdice = dice-1       

            if lastdice*SIDE>=last>=lastdice:
                if DB[lastdice][last]==0:
                    summation += pointProbability(lastdice,last)*1/SIDE
                else:
                    summation += DB[lastdice][last]*1/SIDE

        DB[dice][point]=summation
        return summation
    else: 
        return 1/SIDE

  
def runThisStupidCode():
    rollDices(2,10)
    rollDices(10,20)
    

runThisStupidCode()

