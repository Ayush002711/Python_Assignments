def main():
    file1=input("Enter the File Name")
    file2=input("Enter the  new File Name")
    
    try:
        fobj1=open(file1,"r")
        fobj2=open(file2,"w")
        
        
        for line in fobj1:
            fobj2.write(line)
            
        fobj1.close()
        fobj2.close()

        print("Content of ",file1 ,"copied into ",file2)
    
    except FileNotFoundError:
        print("File Not Found")

if __name__=="__main__":
    main()
