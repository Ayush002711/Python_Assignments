def Length(No):
    Num=0
    Count=No
    while(No!=0):
        Count=No%10
        Num=Num+Count
        No=No//10
    return Num
    
def main():
    No=int(input("Enter a Number"))
    Ret=Length(No)

    print("Count is :",Ret)

if __name__=="__main__":
    main()