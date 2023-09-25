import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# define pin numbers
btn_pin = 
led_pins = [1 2 3 4 5 6 7]

# define times
t_tot = 10 # in seconds
led_time = t_tot/7
vic_time = 3 # in seconds

# setup pins as inputs and outputs
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for led_p in led_pins:
  GPIO.setup(led_p, GPIO.OUT)

def test_for_win(channel):
  # code that triggers when button is pressed goes here
  if led_p == led_pins[3]: #I'm concerned that because we aren't passing led_p to the fxn, it won't get the right value
    time.sleep(led_time)
  else:
    pass

# add event detection (bouncetime is in ms)
GPIO.add_event_detect(btn_pin, GPIO.RISING, callback=test_for_win, bouncetime=200)

# main loop code
try:
  while True:
    # reset key vars and pin states
    #i = 0
    for led_p in led_pins:
      GPIO.output(led_p, GPIO.LOW)

    # increment LEDs and key vars
    for led_p in led_pins:
      GPIO.output(led_p, GPIO.HIGH)
      time.sleep(led_time)
      #i = i + 1
except KeyboardInterrupt:
  GPIO.cleanup()  # Clean up GPIO on CTRL+C exit

GPIO.cleanup()
