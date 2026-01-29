from gpiozero import DistanceSensor, PWMLED
from time import sleep
led = PWMLED(12)
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=1)
while True:
    print(ultrasonic.distance)
    sleep(0.2)
    led.value=ultrasonic.distance