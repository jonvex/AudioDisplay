import os
import json
import time
import subprocess
import threading

CLIENT_SLEEP_TIME = 0.5

class MiniDSP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.__data = {}
        self.__running = False
        self.__lock = threading.Lock()
        
    
        
    def run(self):
        self.__lock.acquire()
        self.__running = True
        while self.__running:
            stream = os.popen("minidsp -o json")
            mdspdata = json.loads(stream.read())
            self.__data["volume"] = mdspdata["master"]["volume"]
            self.__data["mute"] = mdspdata["master"]["mute"]
            self.__data["source"] = mdspdata["master"]["source"]
            self.__lock.release()
            time.sleep(CLIENT_SLEEP_TIME)
            self.__lock.acquire()

    def stop(self):
        with self.__lock:
            self.__running = False

    def data(self):
        return self.__data.copy()


        
