def Maximum(a):
    Max=a[0]
    for i in range(len(a)):
        if(a[i]> Max ):
            Max = a[i]

    return Max

def main():
    No=int(input("Enter a Number"))
    a = []

    for i in range(No):
        Num = int(input())
        a.append(Num)

    Ret=Maximum(a)
    
    print("Maximum Numbers is :",Ret)

if __name__=="__main__":
    main()
