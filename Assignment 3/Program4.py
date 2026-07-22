def Reverse(No):
    Temp=0
    Digit=No
    while(No>0):
        Digit=No%10
        Temp=Temp*10+Digit
        No=No//10

    return Temp

def main():
    print("Enter a number")
    No=int(input())

    Ret=Reverse(No)

    print("Reverse number :",Ret)

if __name__=="__main__":
    main()