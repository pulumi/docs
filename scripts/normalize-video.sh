#!/bin/bash

# This script takes an input video path (relative is fine) and converts it to H.264 MP4 format with AAC audio,
# downscaling to 1200-pixel max-width where necessary. Converted files are written to ${filename}-${video_codec}.${extension}.
# Originals are left not modified.
#
# Requires ffmpeg: https://ffmpeg.org/download.html

filename=$(basename $1)
path=$(dirname $1)
video_codec="h264"
audio_codec="aac"
max_width="1200"
extension="mp4"

ffmpeg -i "${1}" -vcodec "$video_codec" -acodec "$audio_codec" -crf 18 -vf "scale=${max_width}:-1" "${path}/$(echo ${filename%.*})-${video_codec}.${extension}"
