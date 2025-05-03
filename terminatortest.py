import terminatorlib as tlib
from gpiozero import PWMOutputDevice, DistanceSensor
from time import sleep

while True:
    # Testing the robot's movement functions
    tlib.forward_slow()
    print("Moving forward slowly")
    sleep(2)
    tlib.forward_mid()
    print("Moving forward at medium speed")
    sleep(2)
    tlib.forward_fast()
    print("Moving forward fast")
    sleep(2)
    tlib.backward_slow()
    print("Moving backward slowly")
    sleep(2)
    tlib.backward_fast()
    print("Moving backward fast")
    sleep(2)
    tlib.stop()
    print("Stopping")
    sleep(2)
    tlib.direct_left()
    print("Turning left")
    sleep(2)
    tlib.direct_right()
    print("Turning right")
    sleep(2)