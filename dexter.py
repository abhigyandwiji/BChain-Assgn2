from time import time
import socket

current_node=5002
s=socket.socket()
s.connect(('127.0.0.1',current_node))

while True:
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
        flag="Mine"
        s.send(flag.encode())

    else:
        print("Invalid Input")
        continue
        