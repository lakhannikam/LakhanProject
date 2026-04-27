from machine import Pin
import time

# Motor pins
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(27, Pin.OUT)
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(12, Pin.OUT)

# Forward function
def forward():
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

# Stop function
def stop_motor():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

# Main loop
while True:
    forward()            
    time.sleep(2)        

    stop_motor()         
    time.sleep(3)        