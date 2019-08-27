#Program to enable NIC
# T. Lockman
#June 2018


import os


Pass = raw_input("What is the password? ")


if Pass in ['Turtles']:

    os.system('netsh interface set interface "Ethernet" admin=enable')
    os.system('ipconfig /flushdns')

else:
    print "Sorry Charlie...."



