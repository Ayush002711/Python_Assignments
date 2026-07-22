def Prime(No):
    if(No%2==0):
        return True
    else:
        return False

def main():
    print("Enter a Number")
    No=int(input())

    Ret=Prime(No)

    print("Number is Prime")

if __name__=="__main__":
    main()