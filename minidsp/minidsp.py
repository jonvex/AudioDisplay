import os
import time
import json

UPDATE_RATE = 0.25

class Minidsp:

    def __init__(self):
        self.__time = 0
        self.__mute = ""
        self.__volume = ""
        self.__source = ""
        self.__update()

    def __update(self):
        newtime = time.time_ns()
        if (newtime - self.__time) > (1e9 * UPDATE_RATE):
            print("acutally updated")
            stream = os.popen("minidsp -o json")
            mdspdata = json.loads(stream.read())
            self.__volume = mdspdata["master"]["volume"]
            self.__mute = mdspdata["master"]["mute"]
            self.__source = mdspdata["master"]["source"]
            self.__time = newtime

    def volume(self):
        self.__update()
        return self.__volume

    def mute(self):
        self.__update()
        return self.__mute

    def source(self):
        self.__update()
        return self.__source
    
    


