Maxm = lambda No1,No2 : No1>No2

def main():
    No1=int(input("Enter First number"))
    No2=int(input("Enter Second number"))

    Ret=Maxm(No1,No2)
    if(Ret==True):
        Ret=No1
    else:
        Ret=No2

    print("Maximum Number is :",Ret)

if __name__=="__main__":
    main()
