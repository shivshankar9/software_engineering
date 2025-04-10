count=0
for i in range(3):
    
    password=input("enter pass: ")
    if(password=="1234"):
        print("success")
    else:
        count+=1
        if(count==3):
            print("reached maximum attempt ")
        
        

    