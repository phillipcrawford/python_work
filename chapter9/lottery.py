from random import randint

def play_lottery():

    pool = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
    winners = []
    count = 0
    
    while count < 4:
        current = pool.pop(randint(0,(14-count)))
        winners.append(current)
        count += 1
    return winners