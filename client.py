import http.client
import json
import time
import subprocess
from matrixdisplay.main import Render

from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions

connection = http.client.HTTPConnection("moode.local", 5004, timeout=10)
connection.request("GET","/")

volume = ""
oldvolume=""
mute=False
oldmute=False
source=""
oldsource=""
r = Render()


while (True):
    oldvolume = volume
    oldmute = mute
    oldsource = source

    mdspdata = json.loads(connection.getresponse().read().decode())
    volume = mdspdata["master"]["volume"]
    mute = mdspdata["master"]["mute"]
    source = mdspdata["master"]["source"]
    if source != oldsource:
        print("*****Source: " + source + "*****")
    if mute != oldmute:
        if mute:
            print("*****System Mute On*****")
        else:
            print("*****System Mute Off*****")
    if oldvolume != volume:
        r.setVolume(volume)
        print(volume)
    connection.request("GET","/")



