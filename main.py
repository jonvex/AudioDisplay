import os
import json
import time
stream = os.popen("minidsp -o json")
volume = ""
oldvolume=""
while (True):
    mdspdata = json.loads(stream.read())
    oldvolume = volume
    volume = mdspdata["master"]["volume"]
    if oldvolume != volume:
        print(volume)
    stream.write("minidsp -o json")
    time.sleep(0.25)
    

#stream.write("minidsp -o json")

# for key in mdspdata:
#     print("*******************")
#     print(key)
#     print(mdspdata[key])
