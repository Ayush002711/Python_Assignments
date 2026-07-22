def main():
    try:
        filename=input("Enter The File Name")
        fobj=open(filename,"r")

        count=0
        for line in fobj:
            count=count+1

        print("Total number of lines are:",count)      

        fobj.close()
        
    except FileNotFoundError as fobj:  
        print("File not found")      

if __name__=="__main__":
    main()
