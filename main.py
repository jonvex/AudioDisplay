import os
import json
import time
stream = os.popen("minidsp -o json")
volume = ""
oldvolume=""
mute=False
oldmute=False
source=""
oldsource=""
while (True):
    oldvolume = volume
    oldmute = mute
    oldsource = source

    mdspdata = json.loads(stream.read())
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
        print(volume)
    stream = os.popen("minidsp -o json")
    time.sleep(0.25)
    

#stream.write("minidsp -o json")

# for key in mdspdata:
#     print("*******************")
#     print(key)
#     print(mdspdata[key])
