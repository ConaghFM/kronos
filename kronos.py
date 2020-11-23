from gpiozero import *
from time import sleep
positive = LED(17) # Board 11
negative = LED(27) # Board 13
cycleLength = 1

while(true)
    positive.on()
    sleep(0.01) # 10 ms
    positive.off()
    negative.on()
    sleep(0.01)
    negative.off()
    if(cycleLength-0.02 > 0) # check this time is not negative
        sleep(cycleLength-0.02)
    cycleLength = timeFunction(cycleLength)

def timeFunction(cycleLength):
    return cycleLength*1
