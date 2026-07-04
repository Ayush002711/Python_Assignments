def Vowels(Character):
    if(Character == "A" or Character == "a" or
       Character == "E" or Character == "e" or 
       Character == "I" or Character == "i" or
       Character == "O" or Character == "o" or
       Character == "U" or Character == "u"):
  
        return True
    else:
        return False
def main():
    print("Enter a Character")
    Character=input()
    Ret = Vowels(Character)
    if(Ret==True):
        print("The number is Vowel")

    else:
        print("The number is not a Vowel")
if __name__=="__main__":
    main()
