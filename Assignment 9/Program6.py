def Matrix(No):
    for i in range(No,0-1):
        for j in range(i):
            print("*",end="")
    print()


def main():
    No=int(input("Enter a Number"))
    Matrix(No)

if __name__=="__main__":
    main()

    