from gpiozero import * # https://gpiozero.readthedocs.io/en/stable/recipes.html
from time import * # https://docs.python.org/3/library/time.html
from numpy import * # https://numpy.org/doc/

NEGATIVE = LED(17) # Board 11
POSITIVE = LED(27) # Board 13
SLEEP_TIME = 0.016 # 10 ms
clockStart = time() # seconds since the clock started, as a float
cycleLength = 1 # Tick length in seconds

# keep this format 1/(func(seconds) - func(seconds-cycleLength)), and just change out the math function
# returns the fraction of a second each tick should last
def timeFunction():
    seconds = getSeconds()
    if seconds < 1 : # avoid feeding negative times to the math functions
        frequency = 1
    else:
        frequency = sine(seconds) - sine(seconds-1) # the tick frequency in Hz
    return 1/frequency

# this will reach our 20ms limit very quickly
def squared(seconds):
    return seconds**2

def logged(seconds):
    return log(seconds)

def factor(seconds):
    FACTOR = 1
    return FACTOR*seconds

def sine(seconds):
    return sin(seconds)

# Seconds since 00:00 on the clock as a float
def getSeconds():
    global clockStart
    if time() - clockStart > 43200 : # reset every 12 hours
        clockStart = time()
        return 0
    else:
        return time() - clockStart


### Runtime loop ###
while True:
    NEGATIVE.off()
    POSITIVE.on()
    sleep(SLEEP_TIME*3/4)
    POSITIVE.off()
    sleep(SLEEP_TIME/4)
    NEGATIVE.on()
    sleep(cycleLength - SLEEP_TIME)
    cycleLength = timeFunction()
