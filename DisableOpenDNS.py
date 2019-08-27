#Program to point to Comcast DNS and get around OpenDNS
# T. Lockman
#December 2017


import os
import time
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
count = int(0)


Pass = raw_input("What is the password? ")


if Pass in ['Turtles']:

    os.system('netsh interface ipv4 set dnsservers "Ethernet" static 75.75.75.75')
    os.system('ipconfig /flushdns')

    for voice in voices:
        if count == 0:
         engine.setProperty('voice', voice.id)
         engine.say("I HAVE CARRIED OUT YOUR ORDERS MY MASTER...")
         engine.runAndWait()
         count += 1

    print "OpenDNS DISABLED!!! CACHE FLUSHED!"
    time.sleep(3)

else:

    for voice in voices:
        if count == 0:
         engine.setProperty('voice', voice.id)
         engine.say("YOU ARE INCORRECT AND MUST DIE MOTHERFUCKER.")
         engine.runAndWait()
         count += 1

    print "INCORRECT PASSWORD BITCH."
    time.sleep(3)


