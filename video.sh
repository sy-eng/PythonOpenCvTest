#!/bin/bash

file=/dev/video0
modprobe v4l2loopback max_buffers=8 video_nr=7 exclusive_caps=1 card_label=mysink
sleep 10

#chmod 666 /dev/video*
#chmod 666 /dev/media*

# /dev/video7, a v4l2loopback virtual device, is made by this shell script file
