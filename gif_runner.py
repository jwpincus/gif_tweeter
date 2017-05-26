import RPi.GPIO as GPIO
import os
from subprocess import call
from gif_maker import TakeGif
from tweeter import TweetGif

buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
    camera = TakeGif()
    twitter = TweetGif()
    if (GPIO.input(buttonPin)):
        call(['rm twitter_staging/final.gif'], shell=True)
        camera.shoot()
        twitter.tweet()
        
        
