import os
import json
import time
stream = os.popen("minidsp -o json")
volume = ""
oldvolume=""
mute=False
oldmute=False
while (True):
    oldvolume = volume
    oldmute = mute

    mdspdata = json.loads(stream.read())
    volume = mdspdata["master"]["volume"]
    mute = mdspdata["master"]["mute"]
    if mute != oldmute:
        if mute:
            print("*****System Mute On*****")
        else:
            print("*****System Mute Off*****")
    if oldvolume != volume:
        if mute:
            print("m " + str(volume))
        else:
            print(volume)
    stream = os.popen("minidsp -o json")
    time.sleep(0.25)
    

#stream.write("minidsp -o json")

# for key in mdspdata:
#     print("*******************")
#     print(key)
#     print(mdspdata[key])
