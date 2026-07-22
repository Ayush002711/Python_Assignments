Even =lambda No : No % 2 == 1
def main():
    No=int(input("Enter a Number"))

    Ret=Even(No)
    if Ret==True:
         Ret=="True"
         print("Number is odd")
    else:
        Ret=="False"
        print("Number is Even")

if __name__=="__main__":
    main()
    