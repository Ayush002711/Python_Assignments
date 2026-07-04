def Factor(No):
    Num=1
    for i in range(1,No+1):
        if(No%i==0):
            print(i)

def main():
    print("Enter a number")
    No=int(input())
    Ret =Factor(No)

if __name__=="__main__":
    main()

    