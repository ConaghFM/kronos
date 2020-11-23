from gpiozero import *
from time import *
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
    return squared()

# squared returns the fraction of a second the tick (cycleLength) should take
# this will reach our 20ms limit after about 50 seconds
def squared():
    seconds = getSeconds()
    return seconds/(seconds**2)

# Seconds since 00:00 on the clock
def getSeconds():
    t = time.localtime
    if(t.tm_hours > 11)
        hours = t.tm_hour - 12
    else
        hours = t.tm_hour
    t0 = time.struct_time(t.tm_year, t.tm_mon, t.tm_day, hours, 0, 0, tm_wday=4, tm_yday=60, tm_isdst=0)
    seconds = time.mktime(t-t0)
    return seconds
