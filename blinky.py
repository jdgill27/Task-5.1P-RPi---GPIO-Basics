import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

try:
        while 1:
                GPIO.output(18, GPIO.HIGH)
                print("light on")
                time.sleep(0.25)
                GPIO.output(18, GPIO.LOW)
                print("OFF")
                time.sleep(0.25)
except KeyboardInterrupt:
        GPIO.cleanup()
