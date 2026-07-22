ChKEven=lambda No : No%2==0

def main():
    No=int(input("Enter A Number"))

    if ChKEven(No):
        print("Number is Even")

    else:
        print("Number is Odd")

if __name__=="__main__":
    main()

