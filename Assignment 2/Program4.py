def Even(No):
    if (No%2==0):

        return True
    else:
        return False 
def main():
    print("Enter a number")
    No=int(input())

    Ret= Even(No)

    if(Ret):
        print("Number is Even")

    else:
        print("Number is odd")

if __name__=="__main__":
    main()
