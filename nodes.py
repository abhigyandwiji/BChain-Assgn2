from block import Block
from blockchain import Blockchain
from time import time
from transaction import Transaction
import sys
import socket

t=Transaction(0,0,0)
verified=[t]
bcn=Blockchain()

host='127.0.0.1'
port=0
node_id=''

companion_nodes=[5001,5002,5003]

n=len(sys.argv)
if(n!=3):
    print("Please specify Node ID and port number as arguments")
    sys.exit(2)
else:
    node_id=sys.argv[1]
    port=int(sys.argv[2])

s=socket.socket()
print("Socket {} created at port {}".format(node_id,port))
s.bind(('',port))
s.listen(5)

while(1):
    c,addr=s.accept()
    print("Client connection accepted")
    count=0
    while(1):
        flag=c.recv(1024).decode('UTF-8')
        if(flag=="Data"):
            datarcv=c.recv(1024).decode('UTF-8')
            datarcvpm=datarcv.split(',')
            new_tran=Transaction(datarcvpm[0],datarcvpm[1],datarcvpm[2])
            wrong=0
            try:
                amt=int(datarcvpm[1])
                last_time=bcn.get_last_timestamp()
                if(float(datarcvpm[2])<last_time):
                    wrong=1
            except:
                wrong=1
            if(wrong==0):
                verified.append(new_tran)
        elif(flag=="ShowChain"):
            size=str(len(bcn.blocks))
            print(size)
            c.send(size.encode())
            c.recv(1024)
            i=0
            for bcks in bcn.blocks:
                if(i==size):
                    break
                c.send(bcks.to_string().encode())
                c.recv(1024)
                i+=1
        elif(flag=="ShowTran"):
            size=str(len(verified))
            print(size)
            c.send(size.encode())
            c.recv(1024)
            i=0
            for tran in verified:
                if(i==0):
                    i+=1
                    continue
                i+=1
                if(i==size):
                    break
                c.send(tran.to_string().encode())
                c.recv(1024)
        elif(flag=="Mine"):
            combined_data=''
            i=0
            for tran in verified:
                if(i==0):
                    i+=1
                    continue
                combined_data+=tran.to_string()
                combined_data+='\n'
            bcn.add_new_block(combined_data,time())
            c.send("Done".encode())

            for node in companion_nodes:
                print(node)
                if(node==port):
                    continue
                s2=socket.socket()
                s2.connect(('127.0.0.1',node))
                print("Connected to peer")
                s2.send("Verify".encode())
                s2.close()

            verified.clear()
            break
        elif(flag=="Verify"):
            print("Hello ji")
        else:
            count+=1
            if(count>100):
                break
            continue
    c.close()