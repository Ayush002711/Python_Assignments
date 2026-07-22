def sum(No):
    Sum =0
    for i in range(1,No+1):
        Sum = Sum + i

    return Sum

def main():

    print("Enter a number")
    No=int(input())
    Ret = sum(No)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()




    