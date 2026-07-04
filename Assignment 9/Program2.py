def chkGreater(No1,No2):
    if(No1>No2):
        return True
    else:
        return False
    
def main():
    print("Enter first number ")
    No1=int(input())
    print("Enter second number")
    No2=int(input())

    Ret=chkGreater(No1,No2)
    if(Ret==True):
        print("No1 is grater")
    else:
        print("No2 is greater")


if __name__=="__main__":
    main()

