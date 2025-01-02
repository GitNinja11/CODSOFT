import random                          #Importing libraries
import string

def generate_password(l):              #Function to generate password

    Uppercase = string.ascii_uppercase
    Lowercase = string.ascii_lowercase
    Digits = string.digits
    SpecialChars = string.punctuation
     
    password=[]

    All_characters = Uppercase + Lowercase + Digits + SpecialChars
    password += random.choices(All_characters, k=l)

    random.shuffle(password)

    # Convert the list to a string
    a=''.join(password)
    print(a)

def pass_gen():                                    #Main function 
    print("Welcome to Password Generator!")
    try:
        n=int(input("Enter length of your password : "))         #taking the required password length
        if n>=3:
           generate_password(n)
        else:
           print("minimum length of password must be three")
           pass_gen()
    except ValueError:
        print("Invalid input")            

pass_gen()           