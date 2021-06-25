import minidsp 

m = minidsp.Minidsp()
volume = m.volume()
oldvolume = volume
mute = m.mute()
oldmute = mute
source = m.source()
oldsource = source
while (True):
    oldvolume = volume
    oldmute = mute
    oldsource = source

    volume = m.volume()
    mute = m.mute()
    source = m.source()
    
    if source != oldsource:
        print("*****Source: " + source + "*****")
    if mute != oldmute:
        if mute:
            print("*****System Mute On*****")
        else:
            print("*****System Mute Off*****")
    if oldvolume != volume:
        print(volume)