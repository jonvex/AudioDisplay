import os
import time
import json

UPDATE_RATE = 0.25

class Minidsp:

    def __init__(self):
        self.time = 0
        self.mute = ""
        self.volume = ""
        self.source = source
        self.__update()

    def __update(self):
        newtime = time.time_ns()
        if (newtime - self.time) > (1e9 * UPDATE_RATE):
            print("acutally updated")
            stream = os.popen("minidsp -o json")
            mdspdata = json.loads(stream.read())
            self.volume = mdspdata["master"]["volume"]
            self.mute = mdspdata["master"]["mute"]
            self.source = mdspdata["master"]["source"]
            self.time = newtime

    def volume(self):
        self.__update()
        return self.volume

    def mute(self):
        self.__update()
        return self.mute

    def source(self):
        self.__update()
        return self.source
    
    


