#!/usr/bin/env python

import signal
import board
import adafruit_dotstar
import socket
import time
import os
from subprocess import call
import  Adafruit_SSD1306
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
disp=Adafruit_SSD1306.SSD1306_128_64(rst=0)
disp.begin()
disp.clear()
disp.display()
width=disp.width
height=disp.height
font=ImageFont.load_default()
dots=adafruit_dotstar.DotStar(
        board.D6,
        board.D5,
        3,
        auto_write=True,
        brightness=0.2,
        pixel_order=adafruit_dotstar.RGB,
)
dots.fill((0,0,0))
UPTIME_PATH="/home/pi/uptime.txt"
UPTIME_MOTORS_PATH="/home/pi/uptime_motors.txt"

def display_text(text,line,image):
    draw=ImageDraw.Draw(image)
    draw.text((0,line*12),str(text),font=font,fill=255)
    disp.image(image)
    disp.display()



count_global=0
last_pressed=0

def is_connected():
    try:
        s=socket.create_connection(("1.1.1.1",53))
        return True
    except Exception:
        pass
    return False


def get_ip():
    if is_connected():
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        return str(s.getsockname()[0])
    else:
        return "No connectivity."

def long_pressed():
    print("Double pressed.")
    shutdown_pressed()

def shutdown_pressed():
    print("Shutting down...")
    image=Image.new('1',(width,height))
    display_text("Shutting down...",0,image)
    ut=get_uptime()
    fwrite=open(UPTIME_PATH,'w')
    print("writing",ut)
    fwrite.write(str(ut))
    fwrite.close()
    GPIO.cleanup()
    call("sudo nohup shutdown -h now",shell=True)

def get_uptime():
    fread=open(UPTIME_PATH,'r')
    ut_pre=fread.readline()
    fread.close()
    with open('/proc/uptime','r') as f:
        ut_mins=float(f.readline().split()[0])/60
    ut_new=int(ut_mins)+int(ut_pre)
    return ut_new

def get_uptime_motors():
    fread=open(UPTIME_MOTORS_PATH,'r')
    ut=fread.readline()
    fread.close()
    return ut

def button2_pressed():
    print("button 2 pressed!")

def button_pressed(channel):
    print("button pressed")
    image=Image.new('1',(width,height))
    global count_global
    if count_global==0:
        display_text("Welcome to Zumo Robot!",0,image)
    elif count_global==1:
        ip=get_ip()
        ut=get_uptime()
        utm=get_uptime_motors()
        display_text("IP: "+str(ip),0,image)
        display_text("Uptime",1,image)
        display_text("System: "+str(ut)+"min.",2,image)
        display_text("Motors: "+str(utm)+"sec.",3,image)
    if count_global>1:
        count_global=0
    else:
        count_global+=1
    duration_count=0
    for i in range(0,5):
        time.sleep(0.5)
        if not GPIO.input(BUTTON_GPIO):
            duration_count+=1
    if duration_count==5:
        long_pressed()

BUTTON_GPIO=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_GPIO,GPIO.FALLING,callback=button_pressed,bouncetime=100)

BUTTON2_GPIO=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON2_GPIO,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON2_GPIO,GPIO.FALLING,callback=button2_pressed,bouncetime=100)

image=Image.new('1',(width,height))
display_text("Welcome to Zumo Robot!",0,image)
signal.pause()
