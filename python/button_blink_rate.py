from gpiozero import Button, LED
from time import sleep

led = LED(17)
button = Button(3)

delay = 1.0

def blink_fast():
    global delay
    delay = 0.1

def blink_slow():
    global delay
    delay = 1.0
    
button.when_pressed = blink_fast
button.when_released = blink_slow

while True:
    sleep(delay)
    led.on()
    sleep(delay)
    led.off()
