def main():
    filename=input("Enter The File Name")
    fobj=open(filename,"r")
    
    for line in fobj:
       print(line)
       
       
    fobj.close()

        
if __name__=="__main__":
    main()
