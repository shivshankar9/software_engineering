#login first
#condition and control statements

username = input("enter user name: ")

if(username== "shiv"):
    password=input("enter your password: ")
    if(password=="1234"):
        print("login sucessfull!")
        print("Welcome to Age based suggestions:")
        age=int(input("Enter Your Age: "))
        name=input("Enter your name: ")
        if(age<13):
            print("Hi! "+name+" You're a child, enjoy cartoons!")
        elif(age<20):
            print("Hi! "+name+" You're a teenager, stay curious!")
        elif(age<60):
                print("Hi! "+name+" You're an adult, chase your dreams!")
        else:
             print("Hi! "+name+" You're a senior, enjoy your wisdom!")


            
    else:
        print("Enter valid password!!")
else:
    print("Invalid username please enter correctly.")


