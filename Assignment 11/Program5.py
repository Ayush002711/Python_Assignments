from functools import reduce

def ChKPrime(No):
    Sum=0
    if(No<=1):
        return False
    for i in range(2,No):
        if No%2==0:
            return False
    return True
def Mult(No):
    return No * 2

def Maximum(x,y):
    if(x>y):
        return True
    else:
        return False 

def main():
    No=int(input("Enter a Number"))
    Data=[]
    print("Enter the Elements")

    for i in range(No):
        Value=int(input())
        Data.append(No)

    fData=list(filter(ChKPrime,Data))
    print("Filter of Number is :",fData)

    mData=list(filter(Mult,fData))
    print("Map of Number is :",mData)

    result=reduce(Maximum,mData)
    print("Reduce is :",result)

if __name__=="__main__":
    main()












if __name__=="__main__":
    main()