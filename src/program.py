#!/usr/bin/python

import wiringpi
import time
import sdnotify
import os, sys
from evdev import InputDevice, categorize, ecodes
from select import select

RUTA='/dev/input/event0'

def adelante():
    wiringpi.digitalWrite(21, 1)
    wiringpi.digitalWrite(20, 0)
    wiringpi.digitalWrite(16, 1)
    wiringpi.digitalWrite(12, 0)

def atras():
    wiringpi.digitalWrite(21, 0)
    wiringpi.digitalWrite(20, 1)
    wiringpi.digitalWrite(16, 0)
    wiringpi.digitalWrite(12, 1)

def parar():
    wiringpi.digitalWrite(21, 0)
    wiringpi.digitalWrite(20, 0)
    wiringpi.digitalWrite(16, 0)
    wiringpi.digitalWrite(12, 0)

def izquierda():
    wiringpi.digitalWrite(21, 0)
    wiringpi.digitalWrite(20, 1)
    wiringpi.digitalWrite(16, 1)
    wiringpi.digitalWrite(12, 0)

def derecha():
    wiringpi.digitalWrite(21, 1)
    wiringpi.digitalWrite(20, 0)
    wiringpi.digitalWrite(16, 0)
    wiringpi.digitalWrite(12, 1)

ok= False
while ok == False:
    ok= os.access(RUTA, os.F_OK)
    time.sleep(1)

dev = InputDevice(RUTA)

print(dev)
print("programa comenzado")

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 1)
wiringpi.pinMode(20, 1)
wiringpi.pinMode(16, 1)
wiringpi.pinMode(12, 1)

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
        if event.type == ecodes.EV_REL:
            print("rel: " + str(event.value))
            if event.code == ecodes.REL_Y:
                if event.value <= -2:
                    adelante()
                elif event.value >= 2:
                    atras()
                else:
                    parar()
            if event.code == ecodes.REL_X:
                if event.value <= -2:
                    izquierda()
                elif event.value >= 2:
                    derecha()
                else:
                    parar()

    n.notify("WATCHDOG=1")
