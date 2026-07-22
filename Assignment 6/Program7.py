Divisible= lambda No : No %5 ==0
def main():
    No=int(input("Enter a Number"))

    Ret=Divisible(No)

    print("Number is Divisible :",Ret)

if __name__=="__main__":
    main()
    