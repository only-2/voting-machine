
import socket			 

s = socket.socket()		 

port = 12345				

s.connect(('127.0.0.1', port)) 


print (s.recv(1024)[2:-1] )


name=input("name :  ")
password=input("password  :  ")
e=name+"#"+password

s.send(bytes(e,"utf-8 "))

AmIAuth=s.recv(1024)
AmIAuth=str(AmIAuth)[2:-1]


while(AmIAuth!="Login"):
    print("Try again")
        
    name=input("name  :  ")
    password=input("password  :  ")
    e=name+"#"+password

    s.send(bytes(e,"utf-8 "))

    AmIAuth=s.recv(1024)
    AmIAuth=str(AmIAuth)[2:-1]

print("Login")
print('''
chose \n
1.Biden
2.Trump 
''')
chose=input()

s.send(bytes(chose,"utf-8 "))

print(s.recv(1024)[2:-1])




