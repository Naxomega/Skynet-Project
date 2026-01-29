from gpiozero import DistanceSensor, LED # Setting up gpiozero
from time import sleep
led1 = LED(14) # }
led2 = LED(15) # } Setting up LEDs pins
led3 = LED(18) # }
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=1) # Setting up the Ultrasonic Sensor Pin
while True:
    if ultrasonic.distance <= 0.3: # Powering on and off LEDs if an object if far/close from the sensor
        led3.on()                  # The expected physical setup is by using a green, an orange/yellow and a red LED 
    if ultrasonic.distance <= 0.2:
        led2.on()
    if ultrasonic.distance <= 0.1:
        led1.on()
    else:
        led1.off()
        led2.off()
        led3.off()



    
