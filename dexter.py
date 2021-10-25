from time import time
import socket

current_node:int=5001
s=socket.socket()
s.connect(('127.0.0.1',current_node))

available_nodes=[5001,5002,5003]

def electNewLeader(available_nodes,current_node):
    l=len(available_nodes)
    i=available_nodes.index(current_node)
    if(i==(l-1)):
        current_node=available_nodes[0]
    else:
        current_node=available_nodes[i+1]
    return current_node

tprev=time()
while True:

    tcurr=time()
    if(tcurr-tprev>20):
        flag="Mine"
        s.send(flag.encode())
        s.close()
        print("Leader Node switched")
        found=0
        while (found==0):
            current_node=electNewLeader(available_nodes,current_node)
            print(current_node)
            try:
                s=socket.socket()
                s.connect(('127.0.0.1',current_node))
                tprev=time()
                found=1
            except:
                found=0


    print("Please select an option: ")
    print("1: Add transaction\n2: View Blockchain\n3: View verified transactions\n4: Exit")
    choice=str(input("Enter code: "))
    print('\n')
    flag=""

    if(choice == '1'):
        flag="Data"
        s.send(flag.encode())
        data=input("Enter description: ")
        amount=input("Enter amount: ")
        print("\n\n")

        new_tran="{},{},{}".format(data,amount,time())
        s.send(new_tran.encode())

    elif(choice == '2'):
        flag="ShowChain"
        s.send(flag.encode())
        size=s.recv(1024).decode('UTF-8')
        s.send("Next".encode())
        size=int(size)
        while(size>0):
            print(s.recv(1024).decode())
            s.send("Next".encode())
            size-=1
        print("\n\n")

    elif(choice == '3'):
        flag="ShowTran"
        s.send(flag.encode())
        size=s.recv(1024).decode('UTF-8')
        s.send("Next".encode())
        size=int(size)
        while(size>0):
            size-=1
            if(size==0):
                break
            print(s.recv(1024).decode())
            s.send("Next".encode())
        print("\n\n")

    elif(choice == '4'):
        break

    else:
        print("Invalid Input")
        continue
        