def Cube(No):
    cube=1
    cube=No*No*No
    return cube

def main():
    print("Enter a number")
    No=int(input())
    Ret=Cube(No)
    print("Cube is ",Ret)

if __name__=="__main__":
    main()