Square = lambda No : No * No

def main():
    print("Enter a Number")
    No=int(input())
    A=[]
    for i in range(No):
        Num = int(input())
        A.append(Num)

    Ret=list(map(Square,A))
    print("Square is :",Ret)

if __name__=="__main__":
    main()
