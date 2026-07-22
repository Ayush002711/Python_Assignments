def  Frequency (a,Value):
    Count = 0
    for i in range(len(a)):
        if(a[i] == Value):
            Count = Count+1

    return Count

def main():
    No=int(input("Number of Elements"))
    a = []

    for i in range(No):
        Num = int(input())
        a.append(Num)

    Value=int(input("Element to Search "))

    Ret=Frequency(a,Value)
    
    print("Frequency of Numbers is :",Ret)

if __name__=="__main__":
    main()
