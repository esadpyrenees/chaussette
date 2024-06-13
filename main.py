#!/usr/bin/env python3 
import time
from datetime import datetime
from chausette import emitMessage

from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2
import os
from shutil import copyfile

# setup absolute path to local dir
destdir = "/home/user/node/chaussettejs/public/videos/"

# vidéo options
options = {"CAP_PROP_FRAME_WIDTH":1280, "CAP_PROP_FRAME_HEIGHT":1024, "CAP_PROP_FPS":24}

# open any valid video stream(for e.g `myvideo.avi` file)
stream = CamGear(source=0, **options).start()

# build filenames
now = datetime.now().strftime("%m-%d--%H-%M-%S")
outputfile = f"out/{ now }.mp4"
outputwebm = f"out/{ now }.webm"

# slomo
output_params = {"-input_framerate": stream.framerate / 2}
writer = WriteGear(output=outputfile, **output_params)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}
    
    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()

# ffmpeg command as a list
ffmpeg_command = [
    "-y",
    "-i",
    outputfile,
    "-an", 
    "-c:v", "libvpx-vp9","-crf","30","-b:v","0",
    outputwebm
]  # `-y` parameter is to overwrite outputfile if exists

# "[0:v]amplify=radius=19:factor=3875.32,monochrome[out_v]",
time.sleep(1)
writer.execute_ffmpeg_cmd(ffmpeg_command)
print("video transcoded")

# copy file
destfile = os.path.join(destdir, outputwebm)

# 1) over scp ?
# os.system(f'sshpass -p "password" scp user@host:{destfile} {outputwebm}')
# 2) on same system
copyfile(outputwebm, destfile)
print("video copied")

time.sleep(1)
emitMessage("video", outputwebm)