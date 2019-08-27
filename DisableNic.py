#Program to enable NIC
# T. Lockman
#June 2018


import os


os.system('netsh interface set interface "Ethernet" admin=disable')
os.system('ipconfig /flushdns')




