def Start(No):
    while No >0: 
        print(No)
        No = No-1

def main():
    print("Enter a Number")
    No=int(input())

    Ret=Start(No)

if __name__=="__main__":
    main()