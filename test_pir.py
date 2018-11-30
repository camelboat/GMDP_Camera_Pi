from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep
# GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.IN)
#GPIO.setup(21, GPIO.OUT)

led21 = LED(21)
pir = MotionSensor(7)

while True:
    print("motion=", pir.motion_detected)
    sleep(0.1)
#    i = GPIO.input(7)
#    if i == 0:
#        print("No intruders", i)
#        GPIO.output(21, 0)
#        time.sleep(0.1)
#    elif i == 1:
#        print("Intruder detected", i)
#        GPIO.output(21, 1)
#        time.sleep(0.1)
