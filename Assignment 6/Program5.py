Even =lambda No : No %2 == 0
def main():
    No=int(input("Enter a Number"))

    Ret=Even(No)
    if Ret==True:
         Ret=="True"
         print("Number is Even")
    else:
        Ret=="False"
        print("Number is odd")

if __name__=="__main__":
    main()