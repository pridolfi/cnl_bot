#!/usr/bin/python

import wiringpi
import time
import sdnotify
import os, sys
from evdev import InputDevice, categorize, ecodes
from select import select

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

print("programa comenzado")

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 1)
wiringpi.pinMode(20, 1)
wiringpi.pinMode(16, 1)
wiringpi.pinMode(12, 1)

while True:
    adelante()
    time.sleep(5)
    atras()
    time.sleep(5)
    izquierda()
    time.sleep(5)
    derecha()
    time.sleep(5)
    parar()
    time.sleep(5)
    n.notify("WATCHDOG=1")
