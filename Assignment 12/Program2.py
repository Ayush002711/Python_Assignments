import threading

def EvenFactor(No):
    sum=0
    print("Even Factors are")
    for i in range(1,No+ 1):
        if No % i == 0 and i % 2 == 0:
            print(i,end=" ")
            sum += i
            print("Sum of Even Factors:",sum)

def OddFactor(No):  
    sum=0
    print("Odd Factors are") 
    for i in range(1,No+1):
        if No% i ==0 and i % 2!=0:
            print(i,end="")
            sum += i
            print("Sum of Odd Factors:",sum)

def main():
    No=int(input("Enter a Number"))
    
    t1=threading.Thread(target=EvenFactor,args=(No,))
    t2=threading.Thread(target=OddFactor,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit From Main")


if __name__=="__main__":
    main()