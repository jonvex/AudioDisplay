import http.client
import json
import time
import subprocess
import threading

CLIENT_SLEEP_TIME = 0.5

class changeitem:
    def __init__(self, first):
        self.__old = first
        self.__new = first
    
    def changed(self):
        return self.__old == self.__new
    
    def put(self, value):
        self.__new = value

    def get(self):
        self.__old = self.__new
        return self.__new

class minidspdata:
    def __init__(self):
        self.__volume = changeitem("")
        self.__mute = changeitem(False)
        self.__source = changeitem("")
        self.__lock = threading.Lock()
    
    def changed(self):
        self.__lock.acquire()
        if self.__volume.changed():
            return True
        if self.__mute.changed():
            return True
        if self.__source.changed():
            return True
        self.__lock.release()
        return False

    def put(self, volume, mute, source):
        with self.__lock:
            self.__volume.put(volume)
            self.__mute.put(mute)
            self.__source.put(source)

    def get(self):
        ret = {}
        if self.__volume.changed():
            ret["volume"] = self.__volume.get()
        if self.__mute.changed():
            ret["mute"] = self.__mute.get()
        if self.__source.changed():
            ret["source"] = self.__source.get()
        self.__lock.release()
        return ret
    
        
    


class minidspclient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.__data = minidspdata()
        self.__running = False
        self.__lock = threading.Lock()
        
    
        
    def run(self):
        connection = http.client.HTTPConnection("moode.local", 5004, timeout=10)
        self.__lock.acquire()
        self.__running = True
        while self.__running:
            connection.request("GET","/")
            mdspdata = json.loads(connection.getresponse().read().decode())
            self.__data.put(mdspdata["master"]["volume"], mdspdata["master"]["mute"], mdspdata["master"]["source"])
            self.__lock.release()
            time.sleep(0.5)
            self.__lock.acquire()

    def stop(self):
        with self.__lock:
            self.__running = False

    
    def updated(self):
        return self.__data.changed()

    def data(self):
        return self.__data.get()


        
