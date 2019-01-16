#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pytube import YouTube
import sys
import io

SOUND_NO = 140
DOWNLOAD_PATH = r"C:\Users\masaoza\Desktop"
ul =  r"https://www.youtube.com/watch?v=xAeiQnJl1-s"
print("OK!")
ul = input('>>  ')
print(ul)

yt = YouTube(ul)
for lis in yt.streams.all():
    print(lis)

#yt.streams.get_by_itag(SOUND_NO).download(DOWNLOAD_PATH)
print("Download successfully.")
