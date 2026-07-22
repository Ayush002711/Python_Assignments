def ChKNum(No):
    if(No%2==0):
        return True
    else:
        return False
def main():
    No=int(input("Enter a number"))
    
    Ret=ChKNum(No)

    if(Ret):
        print("Even Number")
    else:
        print("Odd Number")

if __name__=="__main__":
    main()