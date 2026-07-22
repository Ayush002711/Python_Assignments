def main():
    file=input("Enter the File Name")
    word =input("Enter a word to search ")

    try:
        fobj=open(file,"r")
        Data=fobj.read()

        if word in Data:
            print("Word is present in Data")
        else:
            print("Word is not present in Data")  
    
    except FileNotFoundError:
        print("File Not Found")

if __name__=="__main__":
    main()
