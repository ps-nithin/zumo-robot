import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(5,gpio.OUT)
gpio.setup(6,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(27,gpio.OUT)
l1=gpio.PWM(5,1000)
l2=gpio.PWM(6,1000)
r1=gpio.PWM(22,1000)
r2=gpio.PWM(27,1000)
l1.start(0)
l2.start(0)
r1.start(0)
r2.start(0)
speed=100
l1_speed=speed
l2_speed=speed
r1_speed=speed
r2_speed=speed

def accelerate():
    global speed
    global l1_speed
    global l2_speed
    global r1_speed
    global r2_speed
    if speed<100:
        speed=speed+10
    if l1_speed>0 and l1_speed<100:
        l1.ChangeDutyCycle(speed)
        l1_speed=speed
    if l2_speed>0 and l2_speed<100:
        l2.ChangeDutyCycle(speed)
        l2_speed=speed
    if r1_speed>0 and r1_speed<100:
        r1.ChangeDutyCycle(speed)
        r1_speed=speed
    if r2_speed>0 and r2_speed<100:
        r2.ChangeDutyCycle(speed)
        r2_speed=speed



def decelerate():
    global speed
    global l1_speed
    global l2_speed
    global r1_speed
    global r2_speed
    if speed>30:
        speed=speed-10
    if l1_speed>0:
        l1.ChangeDutyCycle(speed)
        l1_speed=speed
    if l2_speed>0:
        l2.ChangeDutyCycle(speed)
        l2_speed=speed
    if r1_speed>0:
        r1.ChangeDutyCycle(speed)
        r1_speed=speed
    if r2_speed>0:
        r2.ChangeDutyCycle(speed)
        r2_speed=speed

def forward():
    stop()
    l1.ChangeDutyCycle(speed)
    r1.ChangeDutyCycle(speed)
    global l1_speed
    global r1_speed
    l1_speed=speed
    r1_speed=speed

def backward():
    stop()
    l2.ChangeDutyCycle(speed)
    r2.ChangeDutyCycle(speed)
    global l2_speed
    global r2_speed
    l2_speed=speed
    r2_speed=speed

def spin_cw():
    stop()
    l1.ChangeDutyCycle(speed)
    r2.ChangeDutyCycle(speed)
    global l1_speed
    global r2_speed
    l1_speed=speed
    r2_speed=speed

def stop():
    l1.ChangeDutyCycle(0)
    l2.ChangeDutyCycle(0)
    r1.ChangeDutyCycle(0)
    r2.ChangeDutyCycle(0)
    global l1_speed
    global l2_speed
    global r1_speed
    global r2_speed
    l1_speed=0
    l2_speed=0
    r1_speed=0
    r2_speed=0
def spin_acw():
    stop()
    l2.ChangeDutyCycle(speed)
    r1.ChangeDutyCycle(speed)
    global l2_speed
    global r1_speed
    l2_speed=speed
    r1_speed=speed
