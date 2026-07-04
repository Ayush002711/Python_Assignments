def Divisible(No):
    if(No%3==0 and No%5==0):
        return True
    else:
        return False

def main():
    print("Enter a number")
    No=int(input())
    Ret=Divisible(No)
    print("Divisible is",Ret)

if __name__=="__main__":
    main()
    