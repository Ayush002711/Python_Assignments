class Circle:
    PI=3.14
    
    def __init__(self):
        Radius=0.0
        Area=0.0
        Circumference=0.0
            
    def Accept(self):
        print("Enter the Radius")
        self.Radius=float(input())
            
    def CalculatedArea(self):
        self.Are=0.0
        self.Area=Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference= 2*Circle.PI*self.Area

    def Display(self):
        print("Radius of Circle:",self.Radius)
        print("Area of Circle:",self.Area)
        print("Circumference of Circle:",self.Circumference)

Aobj=Circle()
Aobj.Accept()
Aobj.CalculatedArea()
Aobj.CalculateCircumference()
Aobj.Display

