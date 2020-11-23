from gpiozero import * # https://gpiozero.readthedocs.io/en/stable/recipes.html
from time import * # https://docs.python.org/3/library/time.html
from numpy import * # https://numpy.org/doc/

POSITIVE = LED(17) # Board 11
NEGATIVE = LED(27) # Board 13
SLEEP_TIME = 0.01 # 10 ms
clockStart = time.time() # seconds since the clock started, as a float
cycleLength = 1 # Tick length in seconds

while(true)
    POSITIVE.on()
    sleep(SLEEP_TIME)
    POSITIVE.off()
    NEGATIVE.on()
    sleep(SLEEP_TIME)
    NEGATIVE.off()
    if(cycleLength-(2*SLEEP_TIME) > 0): # check this time is not NEGATIVE
        sleep(cycleLength-(2*SLEEP_TIME))
    cycleLength = timeFunction()

# keep this format 1/(func(seconds) - func(seconds-cycleLength)), and just change out the math function
# returns the fraction of a second each tick should last
def timeFunction():
    seconds = getSeconds()
    if (seconds < 1): # avoid feeding negative times to the math functions
        frequency = 1
    else:
        frequency = squared(seconds) - squared(seconds-1) # the tick frequency in Hz
    return 1/frequency

# this will reach our 20ms limit very quickly
def squared(seconds):
    return seconds**2

def logged(seconds):
    return numpy.log(seconds)

# Seconds since 00:00 on the clock as a float
def getSeconds():
    if ((time.time() - clockStart) > 43200): # reset every 12 hours
        clockStart = time.time()
        return 0
    else:
        return time.time() - clockStart
