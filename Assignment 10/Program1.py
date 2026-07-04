def Table(No):
    
    for i in range(1,10+1):
            print(No*i)

def main():
    print("Enter a number")
    No=int(input())
    Table(No)

if __name__=="__main__":
    main()