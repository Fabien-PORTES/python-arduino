#!/usr/bin/env python
# -*- coding: latin-1 -*-
import time
import serial
serialport = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
time.sleep(2)
while 1:
	response = serialport.readline()
	
	print response