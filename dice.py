import random
import time

#Initializes variables
def init (): 
    startTime = time.time() #Starts the timing
    maxStat = 0
    maxMaxStat = 0
    count = 0
    count17 = 0
    nearMiss = 0
    critFail = 0
    missStat = 0
    minStat = 0
    stat = 0
    return startTime, maxStat, maxMaxStat, count, count17, nearMiss, critFail, missStat, minStat, stat

#Roll 4d6 drop lowest
def rollCall (): 
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    
    roll = [die1, die2, die3, die4]
    roll.remove(min(roll))
    stat = sum(roll)
    
    return stat

#Checks if the desired stats are rolled
def check (maxStat, minStat, missStat, stat): 
    if stat == 18: #Checks if it is max roll
        maxStat += 1
        
    elif stat == 3: #Checks if it is min roll
        minStat += 1
        
    elif stat == 17: #checks if it is near miss
        missStat += 1
        
    return maxStat, minStat, missStat, stat

#Checks for program updates
def update (maxStat, missStat, minStat, maxMaxStat, count, startTime, nearMiss, critFail): 
    if maxStat == 5 and missStat == 1: #Checks for a near miss
        nearMiss += 1
        print("Near miss #"+str(nearMiss))
        
    elif minStat == 6: #Checks for a critical fail
        critFail +=1
        print("Crit fail #"+str(critFail))
        
    if maxStat > maxMaxStat: #Updates number of consecutive 18s
        maxMaxStat = maxStat
        print("New record of consecutive 18s is,",maxMaxStat)
        
    if count % 10000000 == 0: #Updates when 10 million characters are rolled
        print("Update,",count,"rolled characters,",round((time.time()-startTime),2),"seconds elapsed.")
        
    return nearMiss, critFail, maxMaxStat

#End notification
def done (nearMiss, critFail, startTime): 
    print("Perfect character rolled.\n# of near misses is",nearMiss,"\n# of crit fails is",critFail,"\nTotal time elapsed",(time.time()-startTime),"seconds")
    input()

#Rolls a character
def character (maxStat, minStat, missStat, count, count17, stat): 
    maxStat = 0
    minStat = 0
    missStat = 0
    count += 1
    for i in range(0,6): #Rolls all six stats
        stat = rollCall()
        maxStat, minStat, missStat, stat = check(maxStat, minStat, missStat, stat) #Checks if the desired stats are rolled
        if stat == 17:
            count17 += 1
        if stat != 18 and stat != 3 and stat != 17 and count17 > 1: #Breaks if not all max, all min, or near miss
            break
    return maxStat, minStat, missStat, count, count17, stat

#Main program, stops when all 18s are rolled
print("Running program")
startTime, maxStat, maxMaxStat, count, count17, nearMiss, critFail, missStat, minStat, stat = init()

while maxStat < 6:
    
    nearMiss, critFail, maxMaxStat = update(maxStat, missStat, minStat, maxMaxStat, count, startTime, nearMiss, critFail)
    maxStat, minStat, missStat, count, count17, stat = character(maxStat, minStat, missStat, count, count17, stat)
       
done(nearMiss, critFail, startTime)
