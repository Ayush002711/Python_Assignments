import threading

def Even(A):
    for i in range(len(A)):
        if(A[i]%2==0):
            print("Even Thread")
        print(i)
def Odd(A):
    for i in range(len(A)):
        if(A[i]%2 !=0):
            print("Odd Thread")
        print(i)

def main():
    No=int(input("Enter a Number"))

    A=[]

    print("Enter the Elements")
    for i in range(No):
        Num=int(input())
        A.append(Num)


    t1=threading.Thread(target =Even,args=(A,))
    t2=threading.Thread(target =Odd,args=(A,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both Threads are Executed")

if __name__=="__main__":
        main()
