from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    No1=int(input("Enter a Number"))
    No2=int(input("Enter a Number"))
    A=[]
    for i in range(No1,No2):
        Num= int(input())
        A.append(Num)

        Ret=list(reduce(Addition,A))
        print("Addition of  Numbers are : ",Ret)

if __name__=="__main__":
    main()
    