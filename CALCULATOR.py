#CALCULATOR
def simple_calculator():
   try: 
    a=float(input("Enter first number"))               #User input first number
    b=float(input("Enter second number"))              #User input second number
    c=int(input("Enter required operation: (1: + / 2: - /3. * / 4. /): "))          #User input operation
   except ValueError:
      print(f"Invalid input")
      simple_calculator()

   if c==1:                             #Using if else checking the operation and printing the desired result
       print(f"result: {a+b}")
   elif c==2:
       print(f"result: {a-b}")
   elif c==3:
       print(f"result: {a*b}")
   elif c==4:
       if b!=0:
          print(f"result: {a/b}")
       else:
          print("divison by zero  not allowed")  
   else:
       print("invalid")                  

simple_calculator()