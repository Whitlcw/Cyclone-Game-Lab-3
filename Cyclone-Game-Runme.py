#setup---------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

cyc_time = 10 #in seconds
LED_pins = [1 2 3 4 5 6 7] #reassign to match led pins
btn_pin = 10               #reassign to match btn pin
flash_time = cyc_time/7
vict_time = 3

for i in LED_pins:
  GPIO.setup(i, GPIO.OUT)

GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #sets the button pin as pulldown input. Button should send 3.3V to btn_pin
GPIO.add_event_detect(btn_pin, GPIO_RISING)

#main loop--------------------------------
while true:
  for i in LED_pins:
    GPIO.output(i, GPIO.HIGH)
    # wait for a rising edge (timeout is in milliseconds)
    channel = GPIO.wait_for_edge(btn_pin, GPIO_RISING, timeout=flash_time*1000)
    if channel is None:
      
    else:
      if i == LED_pins[3]:
        time.sleep(vict_time)
  for i in LED_pins:
    GPIO.output(i, GPIO.LOW)
    
  
