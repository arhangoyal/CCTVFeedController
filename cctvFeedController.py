# importing the modules
import math
from PIL import Image, ImageChops
import time
import datetime
import os
import picamera
import csv


# image capture initialisation
# create object for PiCamera class
camera = picamera.PiCamera()
# set resolution
camera.resolution = (1024, 768)
# camera.brightness = 60
camera.start_preview()
camera.annotate_text = 'CCTV Feed Controller'

img_counter = 0
vid_counter = 0
start = False  #video recording started/stopped

# initialise csv file
csv_file = open('info.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['S.No.', 'File Name', 'Start Time', 'Date'])


try:
    while True:
        # to show the frame while the recording is going on
        for beep in range(2):
            img_name = "image{}.png".format(img_counter)
            camera.capture(img_name)
            img_counter += 1
            print("{} written!".format(img_name))
            time.sleep(2)

        # creating objects for the two images
        im1 = Image.open(r"/home/pi/Desktop/Camera/image0.png")
        im2 = Image.open(r"/home/pi/Desktop/Camera/image1.png")
        # Calculate the root-mean-square difference between two images
        diff = ImageChops.difference(im1, im2)
        h = diff.histogram()
        sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
        print(rms)
        # to delete the used images
        os.remove(r"/home/pi/Desktop/Camera/image0.png")
        os.remove(r"/home/pi/Desktop/Camera/image1.png")
        img_counter = 0


        if rms > 50 and start == False:
            vid_name = "video{}.h264".format(vid_counter)
            camera.start_recording(vid_name)
            print("video recording started")
            start = True

            file_name = "video" + str(vid_counter)
            file_time = datetime.datetime.today().replace(microsecond=0).time()
            file_date = datetime.datetime.now().date()
            csv_writer.writerow([vid_counter + 1, file_name, file_time, file_date])

            vid_counter += 1

        elif rms < 50 and start == True:
            camera.stop_recording()
            print("video recording stopped")
            start = False

except KeyboardInterrupt:  #to exit the program using the keyboard
    if start == True:  #stop recording before exiting (to prevent errors)
        camera.stop_recording()  #to end the recording
        print("video recording stopped")


csv_file.close()


# display contents of csv file
with open('info.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)


camera.stop_preview()
