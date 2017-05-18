
import time             # library for intoducing deleay between led on and off
import RPi.GPIO as GPIO #for contolling voltage output to pins

def blink():
    GPIO.setmode(GPIO.BOARD)  ## Use board pin numbering
    GPIO.setup(5, GPIO.OUT)  ## Setup GPIO Pin 5 to OUT (chossen at random )
    count=0
    while count!=05:
        GPIO.output(5,True)  ## Turn on Led
        time.sleep(0.1)     ## Wait for one millisecond
        GPIO.output(5,False) ## Turn off Led
        time.sleep(0.1)    ## Wait for one millisecond
        count=count+1