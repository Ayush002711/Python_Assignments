def Palon(No):
    count=0
    while(No!=0):
        Palon = No%10
        count=count*10+Palon
        No=No//10
    if No == count:
        return True
    else:
        return False

def main():
    No=int(input("Enter a number"))

    Ret=Palon(No)

    if Ret == True:
        print("Number is Palindrome")

    else:
        print("Number is not Palindrome")

if __name__=="__main__":
    main()