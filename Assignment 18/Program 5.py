def main():
    try:
        filename=input("Enter The File Name")
        fobj=open(filename,"r")

        count=0

        for line in fobj:
            words=line.split()
            count=count+len(words)  

        print("Total number of words are:",count)      

        fobj.close()
        
    except FileNotFoundError as fobj:  
        print("File not found")      

if __name__=="__main__":
    main()
