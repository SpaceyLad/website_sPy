#!/usr/bin/env python3

# Written and developed by Stian Kvålshagen.
# Reminder: Do not use this against websites without permission.

import urllib.request
import argparse 

# Import data needed
parser = argparse.ArgumentParser()
parser.add_argument("-a","--all",help="List everything!",required=False,action=argparse.BooleanOptionalAction)
parser.add_argument("-u","--url",help="The url you wish to scan.",required=True,type=str)
parser.add_argument("-s","--script",help="List all scripts",action=argparse.BooleanOptionalAction)
parser.add_argument("-sO","--sources",help="List all sources",action=argparse.BooleanOptionalAction)
parser.add_argument("-l","--links",help="List all links",required=False,action=argparse.BooleanOptionalAction)
parser.add_argument("-p","--png",help="List all pngs",required=False,action=argparse.BooleanOptionalAction)
parser.add_argument("-j","--jpg",help="List all jpeg and jpgs",required=False,action=argparse.BooleanOptionalAction)
args = parser.parse_args()

url = args.url

# Open and read the URL.
fp = urllib.request.urlopen(url)
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()

# Here we split content into an list. The split parameter is "<".
lines =  mystr.split("<")
# fl = fixed lines
fl = []
for x in lines:
 fl.append("<" + x)

# Display Error message telling user to add argument
if args.all is not True and args.links is not True and args.sources is not True and args.png is not True and args.jpg is not True:
 print("Make sure to have an argument! Try -a for all")

# Check if all
all = False
if args.all:
 all = True

# Find all scripts
if args.script or all:
 found = False
 print("All scripts:")
 for x in fl:
  if "<script" in x:
   print(x)
   found = True
 if not found:
  print("Nothing found..")
 print(" ")

# Find all links
if args.links or all:
 print("All links")
 found = False
 for x in fl:
  if "<link" in x:
   print(x)
   found = True
 if not found:
  print("Nothing found..")
 print(" ")

# Find all sources
if args.sources or all:
 src = []
 found = False
 for x in fl:
  src.append(x.find("src"))
 print("All sources:")
 i = 0
 for x in fl:
  if src[i] > 0:
   print(x)
   i = i + 1
   found = True
  else:
   i = i + 1
 print(" ")
 if not found:
  print("Nothing found..")

# Look for png
if args.png or all:
 print("All png:")
 png = []
 for x in fl:
  png.append(x.find(".png"))
 i = 0
 for x in fl:
  if png[i] > 0:
   print(x)
   i = i + 1
  else:
   i = i + 1
 print(" ")
 pngsum = len(png)
 for x in png:
  pngsum = pngsum + int(x)
 if pngsum == 0:
  print("Nothing found..")

# Look for jpg or jpeg
if args.jpg or all:
 print("All jpeg & jpg:")
 jpg = []
 jpeg = []
 for x in fl:
  jpg.append(x.find(".jpg"))
  jpeg.append(x.find(".jpeg"))
 i = 0
 for x in fl:
  if jpg[i] > 0 or jpeg[i] > 0:
   print(x)
   i = i + 1
  else:
   i = i + 1
 jpgsum = len(jpeg) + len(jpg)
 for x in jpg:
  jpgsum = jpgsum + int(x)
 for x in jpeg:
  jpgsum = jpgsum + int(x)
 if jpgsum == 0:
  print("Nothing found..")
