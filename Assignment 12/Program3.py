from Calculation import *

def main():
    No1=int(input("Enter First Number"))
    No2=int(input("Enter Second Number"))
    
    Ret=Addition(No1,No2)
    print("Addition is:",Ret)

    Ret=Substraction(No1,No2)
    print("Substraction is :",Ret)

    Ret=Multiplication(No1,No2)
    print("Multiplicaton is :",Ret)

    Ret=Division(No1,No2)
    print("Division is :",Ret)


if __name__=="__main__":
    main()