def Num(No):
    if(No>0):
        return True
    else:
        return False
    
def main():
    No=int(input("Enter a Number"))

    Ret=Num(No)
    if(Ret):
        print("Numer is positive")
    else:
        print("Number is negative")
    

if __name__=="__main__":
    main()
