class BookStore():
    NoOfBooks=0
    
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBooks +=1

    def Display(self):
        print(self.Name, "by",self.Author,"No of Books",BookStore.NoOfBooks)

print("Enter a Bookname")
Name=input()

print("Enter Author name")
Author=input()

Aobj=BookStore(Name,Author)
Aobj.Display()



    