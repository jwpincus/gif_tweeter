import picamera
import time
import datetime
from subprocess import call


class TakeGif(object):
    
    def shoot(self):
        with picamera.PiCamera() as camera:
            now = datetime.datetime.now().strftime("%H%M%S")
            camera.resolution = (320, 240)
            camera.start_preview()
            time.sleep(.25)
            camera.start_recording(("%(now)s.h264" % locals()))
            camera.wait_recording(3)
            camera.stop_recording()
            camera.stop_preview()
            camera.close()
            cmd = ("MP4Box -add %(now)s.h264 %(now)s.mp4" % locals())
            call([cmd], shell=True)
            cmd2 = ("avconv -i %(now)s.mp4 -s qvga -vf format=rgb8,format=rgb24 -pix_fmt rgb24 -r 10 twitter_staging/final.gif" % locals())
            call([cmd2], shell=True)
            cmd3 = "rm *.h264 && rm *.mp4"
            call([cmd3], shell=True)


