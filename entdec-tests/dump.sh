#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 SRC DST"
    exit 1
fi

gst-launch-1.0 \
    filesrc location=$1 ! qtdemux ! h265parse \
    ! avdec_h265 max-threads=1 \
    ! filesink location=$2
