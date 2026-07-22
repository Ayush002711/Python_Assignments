Divisible = lambda No : (No%5==0)

def main():
    No=int(input("Enter A Number"))
    
    if Divisible(No):
        print("True")

    else:
        print("False")

if  __name__=="__main__":
    main()