import threading

def Small(No):
    count=0
    for A in No:
        if A.islower():
            count+=1
    
    print("Thread_Id :",threading.get_ident())
    print("Thread name:",threading.current_thread().name)
    print("Lower Letters:",count)
    print()
   

def Capital(No):
    count=0
    for A in No:
        if A.isupper():
            count+=1

    print("Thread_Id :",threading.get_ident())
    print("Thread name:",threading.current_thread().name)
    print("Capital Letters:",count)
    print()
    

def Digit(No):
    count=0
    for A in No:
        if A.isdigit():
            count+=1

    print("Thread_Id :",threading.get_ident())
    print("Thread name:",threading.current_thread().name)
    print("Digit:",count)
    print()
    
    
def main():
    No=int(input("Enter A Number"))
   
    t1=threading.Thread(target=Small,args=(No,),name="Small")
    t2=threading.Thread(target=Capital,args=(No,),name="Capital")
    t3=threading.Thread(target=Digit,args=(No,),name="Digit")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__=="__main__":
    main()