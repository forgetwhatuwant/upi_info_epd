import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback(channel):
    print("Button was pushed!")

try:
    GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback, bouncetime=200)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped by User")
finally:
    GPIO.cleanup()
