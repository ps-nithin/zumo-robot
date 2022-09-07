import pigpio 
import time
pi=pigpio.pi()
pi.hardware_PWM(12,100,0)
pi.hardware_PWM(13,100,0)
pi.hardware_PWM(18,100,0)
pi.hardware_PWM(19,100,0)


def forward(speed):
    stop()
    pi.set_PWM_dutycycle(12,speed)
    pi.set_PWM_dutycycle(13,speed)

def backward(speed):
    stop()
    pi.set_PWM_dutycycle(18,speed)
    pi.set_PWM_dutycycle(19,speed)

def spin_cw(speed):
    stop()
    pi.set_PWM_dutycycle(12,speed)
    pi.set_PWM_dutycycle(19,speed)

def stop():
    pi.set_PWM_dutycycle(12,0)
    pi.set_PWM_dutycycle(13,0)
    pi.set_PWM_dutycycle(18,0)
    pi.set_PWM_dutycycle(19,0)

def spin_acw(speed):
    stop()
    pi.set_PWM_dutycycle(18,speed)
    pi.set_PWM_dutycycle(13,speed)
