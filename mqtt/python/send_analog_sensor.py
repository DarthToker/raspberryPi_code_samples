#!/usr/bin/env python
"""

DeviceHUB.net sample code for sending an analog sensor.

In this example the sensor is simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 26 May 2015
by Alexandru Gheorghe

"""


from devicehub import Sensor, Device, Project
from time import sleep
from random import randint

PROJECT_ID      = '4586'
DEVICE_UUID     = '0960c350-dee7-4c25-87a2-fa32164d5c16'
API_KEY         = '6ccd115d-5131-407f-b76f-5158fa4889bb'
AN_SENSOR_NAME  = 'CONS_PH1'


def analog_input(dev, sensor):
    value = randint(0, 1023)
    sensor.addValue(value)
    dev.send()
    print value
    return

project = Project(PROJECT_ID, ssl_verify=False)
device = Device(project, DEVICE_UUID, API_KEY)

AN1 = Sensor(Sensor.ANALOG, AN_SENSOR_NAME)

device.addSensor(AN1)

while True:
    analog_input(device, AN1)
    sleep(5.0)
