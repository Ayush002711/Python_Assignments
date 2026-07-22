ChKOdd = lambda No : No%2!=0

def main():
    No=int(input("Enter A Number"))

    if ChKOdd(No):
        print("Number is Odd")

    else:
        print("Number is Even")

if __name__=="__main__":
    main()

