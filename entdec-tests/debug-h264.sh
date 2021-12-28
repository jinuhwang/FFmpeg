#!/bin/bash

LOCATION=/ssd1/archie/day1.mp4

gdb --args \
gst-launch-1.0 \
    filesrc location=$LOCATION ! qtdemux ! h264parse \
    ! avdec_h264 max-threads=1 \
    ! fakesink
