import RPi.GPIO as GPIO
import time
 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        
    else:
        
 
try:
    GPIO.setmode(GPIO.BCM)
    led_pins = [1 2 3 4 5 6 7]
    btn_pin = 8
    for i in led_pins:
        
    GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_pin, GPIO.RISING, callback=my_callback)
 
    message = raw_input('\nPress any key to exit.\n')

finally:
    GPIO.cleanup()
