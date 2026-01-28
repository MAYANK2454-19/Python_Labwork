terms = int(input("Enter number of terms : "))
a = 1
b = 1

print(a,b,end=" ")
for i in range (0,terms) : 
    c = a+b   
    print(c,end=" ")
    b = a
    a = c

   

