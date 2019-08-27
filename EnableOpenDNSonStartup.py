#Program to point DNS back to DHCP settings
# T. Lockman
#December 2017


import os
import time
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 100)
voices = engine.getProperty('voices')
count = int(0)


os.system('netsh interface ipv4 set dnsservers name="Ethernet" source=dhcp')
os.system('ipconfig /flushdns')

for voice in voices:
    if count == 0:
        engine.setProperty('voice', voice.id)
        engine.say("WELCOME, TRAVIS. WHAT IS THY BIDDING MY MASTER???")
        engine.runAndWait()
        count += 1

print "OpenDNS ENABLED!!! CACHE FLUSHED!"
time.sleep(1)

