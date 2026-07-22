from functools import reduce

def ChKEven(No):
    return No % 2==0

def Calculate(No):
    return No * No

def Addition (x,y):
    return x + y

def main():
    A=int(input("Enter a number"))

    Data=[]

    print("Enter the Elements")

    for i in range(A):
        Value=int(input())
        Data.append(Value)

    fData = list(filter(ChKEven,Data))
    print("Filter of Numbers :",fData)

    mData=list(map(Calculate,fData))
    print("Map of Numbers :",mData)

    result=reduce(Addition,mData)
    print("Reduce is :",result)

if __name__=="__main__":
    main()

    


    







if __name__=="__main__":
    main()