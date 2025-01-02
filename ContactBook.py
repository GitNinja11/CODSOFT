# Contact Information: Store name, phone number, email, and address for each contact.

# Add Contact: Allow users to add new contacts with their details.

# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.

# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.

# User Interface: Design a user-friendly interface for easy interaction.

book={}

def add_Contact():                           #Function to add contact
    name=input("Enter name: ")
    phone_num=int(input("Enter phone number : "))
    email= input("Enter Email: ")
    address= input("Enter adress")
    book[name]={'PhoneNumber':phone_num , 'Email': email , 'Address':address}

def search_contact_byName(n):                #Function to search contact by name
    if n in book:
        print(f"Name: {n}")
        print(book[n])
    else:
        print("Data not found")  

def search_contact_Number(num):               #Function to  search contact by contact number
    num=str(num).strip()
    flag=False
    for name,details in book.items():
        if str(details["PhoneNumber"]).strip()==num:
            print(f"\nDetails for '{name}':")
            print(f"Phone: {details['PhoneNumber']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}\n")
            flag=True
            break
        else:
            print("Data not found")      


def View_Contact_List():                               #Funtion to view contact list
    if len(book)!=0:
        for name,details in book.items():
            print(f"name: {name}" + f"  Phone Number: {details["PhoneNumber"]}")
    else:
        print("Contact Book is Empty")


def Delete_Contact(name):                               #Function to delete contact
    if name in book:
        del book[name]
        print("Deleted Contact")
    else:
        print("Data not found")    

def Update_Contact(name):                                #Function to Update contact
    if name in book:
        print(f"Name: {name}")
        print(f"Phone Number: {book[name]['PhoneNumber']}")
        print(f"Email: {book[name]['Email']}")
        print(f"Address: {book[name]['Address']}")

        print(f"To Update Phone Number: 0 ")
        print(f"To Update Email: 1 ")
        print(f"To Update Address: 2 ")

        choice = int(input(f"What do you want to Update? "))

        if choice==0:
          try:  
            num=int(input("Enter new Phone Number: "))
            book[name]['PhoneNumber']=num
            print(f"Phone number Updated to:{num}")
          except ValueError:
            print("Invalid Input") 

        elif choice==1:
            num=(input("Enter new Email: "))
            book[name]['Email']=num
            print(f"Email Updated to:{num}")   
        
        elif choice==2:
            num=(input("Enter new Address: "))
            book[name]['Address']=num
            print(f"Address Updated to:{num}")
        
        else:
            print("Enter a valid choice")
            print(" ")
            Update_Contact(name)
    else:
        print("Data not found.")


def Contact_Book():                                      #Main Function 
  while True:
        print("Welcome to Contact Book😊")
        print("0: To Add Contact")
        print("1: To Search Contact by Name")
        print("2: To Search Contact by Phone Number")
        print("3: To View the contact List")
        print("4: To update contact")
        print("5: To delete contact")
        print("6: To Exit")
        try:
            want=int(input("Enter number corresponding to your task"))
            if want==0:
              add_Contact()
              print("The contact had been added")

            elif want==1:   
              n=input("Enter name you want to search: ")
              search_contact_byName(n)
        
            elif want==2:
              n=int(input("Enter number you want to search: "))
              search_contact_Number(n)

            elif want==3:
              print("Contact List: ")
              View_Contact_List()    

            elif want==4:
              n=input("Enter name you want to update details of : ")
              Update_Contact(n)

            elif want==5:
              n=input("Enter name you want to delete details of : ")
              Delete_Contact(n)    
        
            elif want==6:
              print("Exit")
              break
        
            else:
              print("Enter a valid choice")
              Contact_Book()
        except ValueError:
            print("Invalid input")  
            Contact_Book()    

Contact_Book()                                            #Driver code