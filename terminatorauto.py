import terminatorlib as tlib
from gpiozero import PWMOutputDevice, DistanceSensor
from time import sleep

while True:
    tlib.forward_mid()
    tlib.distance_front()
    if tlib.distance_front() < 0.3:
        print("ATTENTION! Obstacle detected!")
        tlib.stop()
        sleep(0.5)
        tlib.backward_slow()
        sleep(3)
        tlib.turn_right()
        sleep(3)
        tlib.forward_mid()
