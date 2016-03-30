import random
#def method that generates increasing large 
#arrays of neg & pos nums to send to maxSubarray

def arrayGenerator(num):
    array = []
    for n in range(num):
        array.append(random.randint(-100, 100))
    return array