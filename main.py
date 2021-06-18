import os
import json
stream = os.popen("minidsp -o json")
#stream.write("minidsp -o json")
mdspdata = json.loads(stream.read())
for key in mdspdata:
    print("*******************")
    print(key)
    print(mdspdata[key])
