CheckEven = lambda No : No%2==0

def main():
    No=int(input("Enter a Number"))
    A=[]
    for i in range(No):
        Num=int(input())
        A.append(Num)

        Ret=list(filter(CheckEven,A))
        print("Even Numbers are :",Ret)

if __name__=="__main__":
    main()
    