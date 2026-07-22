def Divi(No):
    if(No%5==0):
        return True
    else:
        return False
    
def main():
    No=int(input("Enter a Number"))

    Ret=Divi(No)
    print("Is is Divisible",Ret )

if __name__=="__main__":
    main()