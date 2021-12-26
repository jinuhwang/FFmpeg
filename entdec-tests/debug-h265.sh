#!/bin/bash

LOCATION=/ssd3/h265/archie/day1-1m-crf-26-slow.mp4

gdb --args \
gst-launch-1.0 \
    filesrc location=$LOCATION ! qtdemux ! h265parse \
    ! avdec_h265 max-threads=1 \
    ! fakesink
