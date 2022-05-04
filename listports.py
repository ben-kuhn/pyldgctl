#!/usr/bin/env python3
import serial
import serial.tools.list_ports
for n, (portname, desc, hwid) in enumerate(sorted(serial.tools.list_ports.comports())):
	print(portname + ": " + desc)
