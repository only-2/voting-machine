
from threading import Thread


import socket			 

s = socket.socket()		 
print ("Socket successfully created")

port = 12345				

s.bind(('127.0.0.1', port))		 
print ("socket binded to %s" %(port)) 

s.listen(5)	 
print ("socket is listening"	)		



class Vote(Thread):
    def __init__(self,add,conn,idd):
        Thread.__init__(self)
        self.idd=idd
        self.conn=conn
        self.add=add
        self.auth=False
        self.canVote=True
        self.user=''

    def credintial(self,details):
            details=str(details)[2:-1]
            f=open('database.txt','r')
            for user in f.readlines():
                dt=user.split('\n')
                namepass,voteto=dt[0].split('>')
                
                


                if(namepass==details):
                        if(voteto!='-1'):
                                print('Done')
                                self.canVote=False
                        self.user=namepass
                        return True

            f.close()

            return False

    def addVote(self,chose):
        chose=str(chose)[2:-1]
        f=open('database.txt','r')
        datainfile=''
        for user in f.readlines():
                dt=user.split('\n')
                temp=dt[0]
                namepass,voteto=dt[0].split('>')
                if(namepass==self.user):
                            newline=namepass+'>'+chose
                            datainfile+=newline
                            
                else:
                        datainfile+=temp
                datainfile+='\n'

        
        f.close()
        filewrite=open('database.txt','w')

        filewrite.write(datainfile)
        filewrite.close()
                              

            
            


    def run(self):
        self.conn.send(bytes("hello User plz enter credintial","utf-8 "))
        details=self.conn.recv(1024)
        cred=self.credintial(details)
        while(not self.auth):
                if(cred):
                        self.auth=True
                        self.conn.send(bytes("Login","utf-8 "))
                else:
                        self.auth=False
                        self.conn.send(bytes("Fail","utf-8 "))
                        details=self.conn.recv(1024)
                        cred=self.credintial(details)
        
        chose=self.conn.recv(1024)
        print(chose)
        print(self.canVote)
        if(self.canVote):
                self.addVote(chose)
                final_msg="okey your chose : "+str(chose)+"is Added"
                
                self.conn.send(bytes(final_msg,"utf-8 "))
        
        else:
                final_msg="You have already vated"
                self.conn.send(bytes(final_msg,"utf-8 "))

        
        


useraddres=[]
count=0
while True: 

        c, addr = s.accept()
        
        print(c)	
        
        useraddres.append(addr)
        useraddres[count] =Vote(addr,c,count)
        useraddres[count].start()
                
        count+=1


                

        


