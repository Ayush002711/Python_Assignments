def Digit(No):
    count=0
    while(No!=0):
        Digit = No%10
        count=count+1
        No = No//10
    return count 
def main():
    print("Enter a Number")
    No=int(input())

    Ret=Digit(No)

    print("count of Digit is :",Ret)

if __name__=="__main__":
    main()