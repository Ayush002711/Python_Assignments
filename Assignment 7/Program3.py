CheckOdd = lambda No : No%2==1

def main():
    No=int(input("Enter a Number"))
    A=[]
    for i in range(No):
        Num=int(input())
        A.append(Num)

        Ret=list(filter(CheckOdd,A))
        print("Odd Numbers are :",Ret)

if __name__=="__main__":
    main()
    