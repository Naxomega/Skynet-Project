from gpiozero import DistanceSensor, LED
from time import sleep
led1 = LED(14)
led2 = LED(15)
led3 = LED(18)
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=1)
while True:
    if ultrasonic.distance <= 0.3:
        led3.on()
    if ultrasonic.distance <= 0.2:
        led2.on()
    if ultrasonic.distance <= 0.1:
        led1.on()
    else:
        led1.off()
        led2.off()
        led3.off()



    
