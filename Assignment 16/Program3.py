class Arithmetic:
    def __init__(self,A,B):
        self.value1=A
        self.value2=B
    
    def Addition(self):
        Ans=self.value1+self.value2
        return Ans
    
    def Substraction(self):
        Ans=self.value1+self.value2
        return Ans
    
    def Multiplication(self):
        Ans=self.value1 * self.value2
        return Ans

    def Division(self):
        Ans=self.value1 % self.value2
        return Ans
    
No1=int(input("Enter first Number"))
No2=int(input("Enter second Number"))
    
    
Aobj = Arithmetic(No1,No2)

Ret=Aobj.Addition
print("Addition is :",Ret)

Ret=Aobj.Substraction
print("Substraction is :",Ret)

Ret=Aobj.Multiplication
print("Mult is :",Ret)

Ret=Aobj.Division
print("Division is :",Ret)
