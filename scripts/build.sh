#!/usr/bin/env sh

ffmpeg -r 1 -i working/%05d.png \
       -vcodec libx264 -profile:v baseline \
       -pix_fmt yuv420p -movflags +faststart \
       build/poster.mp4
