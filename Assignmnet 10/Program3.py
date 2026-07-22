def Minimum(a):
    Min=a[0]
    for i in range(len(a)):
        if(a[i]< Min ):
            Mix = a[i]

    return Mix

def main():
    No=int(input("Enter a Number"))
    a = []

    for i in range(No):
        Num = int(input())
        a.append(Num)

    Ret=Minimum(a)
    
    print("Minimum Numbers is :",Ret)

if __name__=="__main__":
    main()
