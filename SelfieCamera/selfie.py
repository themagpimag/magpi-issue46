from gpiozero import Button
from datetime import datetime
import picamera
import time

btn = Button(14)
pc = picamera.PiCamera()

def picture():
    timestamp = datetime.now()
    pc.capture('pic'+str(timestamp)+'.jpg')
    time.sleep(1)

while True:
    btn.wait_for_press
    picture()
