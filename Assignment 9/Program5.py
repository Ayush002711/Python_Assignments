def ChKPrime(No):
    if(No<=1):
        return False
    for i in range(2,No):
        if(No%i==0):
            return False
    else:
        return True
def main():
    No=int(input("Enter a Number"))
    Ret=ChKPrime(No)
    
    if(Ret):
        print("Number is Prime")
    else:
        print("Number is Not Prime")

if __name__=="__main__":
    main()

