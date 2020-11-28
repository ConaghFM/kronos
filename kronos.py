from gpiozero import * # https://gpiozero.readthedocs.io/en/stable/recipes.html
from time import * # https://docs.python.org/3/library/time.html
from numpy import * # https://numpy.org/doc/

NEGATIVE = LED(17) # Board 11
POSITIVE = LED(27) # Board 13
SLEEP_TIME = 0.017 # 10 ms
clockStart = time() # seconds since the clock started, as a float
cycleLength = 1 # Tick length in seconds
SOFT_START = false

# keep this format 1/(func(hours) - func(hours-cycleLength)), and just change out the math function
# returns the fraction of a second each tick should last
def timeFunction():
    hours = getHours()
    if hours < 0 : # avoid feeding negative times to the math functions
        return 1
    else:
        frequency = logged(hours) - logged(hours-(1/3600)) # the tick frequency in Hz
    return 1/frequency

# this will reach our 20ms limit very quickly
def squared(hours):
    if SOFT_START and hours < 1: # normal time for the first hour
        return 1
    else:
        return (hours)**2

def logged(hours):
    if SOFT_START and hours < 1: # normal time for the first hour
        return 1
    else:
        return log(hours)

def factor(hours):
    FACTOR = 1
    return FACTOR*hours

def sine(hours):
    return hours*(1 + sin(hours))

# Seconds since 00:00 on the clock as a float
def getHours():
    global clockStart
    if time() - clockStart > 43200 : # reset every 12 hours
        clockStart = time()
        return 0
    else:
        return (time() - clockStart)/3600


### Runtime loop ###
while True:
    NEGATIVE.off()
    POSITIVE.on()
    sleep(SLEEP_TIME*3/4)
    POSITIVE.off()
    sleep(SLEEP_TIME/4)
    NEGATIVE.on()
    if (cycleLength - SLEEP_TIME) < 0 :
        sleep(SLEEP_TIME)
    else:
        sleep(cycleLength - SLEEP_TIME)
    cycleLength = timeFunction()
