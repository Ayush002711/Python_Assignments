import threading

def EvenList(A):
    for i in range(A):
        if (i %2==0):
            print("Even List")


def OddList(A):
    for i in range(A):
        if(i % 2 !=0):
            print("Odd List")

def main():
    No=int(input("Enter A Number"))

    A=[]

    print("List")
    for i in range(No):
        Num=int(input())
        A.append(Num)

    t1=threading.Thread(target=EvenList,args=(A,))
    t2=threading.Thread(target=OddList,args=(A,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()