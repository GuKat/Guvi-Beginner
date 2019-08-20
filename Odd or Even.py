a1 = input("Enter the input:")
if(a1.isdigit()):
    a=int(a1)
    if(a%2==0):
        print("Number is Even")  
    else:  
        print("Number is Odd") 
else:
    print("Ivalid Character")
