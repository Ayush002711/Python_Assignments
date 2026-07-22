from functools import reduce

def ChKEven(No):
    return No>= 70 and No <= 90

def Increase(No):
    return No + 10

def Product(x,y):
    return x * y

def main():
    A=int(input("Enter a number"))

    Data=[]

    print("Enter the Elements")

    for i in range(A):
        Value=int(input())
        Data.append(Value)

    fData = list(filter(ChKEven,Data))
    print("Filter of Numbers :",fData)

    mData=list(map(Increase,fData))
    print("Map of Numbers :",mData)

    result=reduce(Product,mData)
    print("Reduce is :",result)

if __name__=="__main__":
    main()

    


    







if __name__=="__main__":
    main()