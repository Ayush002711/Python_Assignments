def Add(a):
    Sum=0
    for i in range(len(a)):
        Sum += a[i]

    return Sum

def main():
    No=int(input("Enter a Number"))
    a = []

    for i in range(No):
        Num = int(input())
        a.append(Num)

    Ret=Add(a)
    print("Sum of All Numbers is :",Ret)

if __name__=="__main__":
    main()
