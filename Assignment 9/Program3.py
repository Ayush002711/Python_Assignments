def Multiplication(No):
    square=1
    square=No*No
    return square

def main():
    print("Enter a number")
    No=int(input())
    Ret= Multiplication(No)
    print("square is " , Ret)

if __name__=="__main__":
    main()
    