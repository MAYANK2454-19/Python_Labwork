print ("Enter tyhe value for a , b and c in euation , ax^2 + bx + c")
a = int(input("value of a : "))
b = int(input("value of b : "))
c = int(input("value of c : "))
root1 =  ((-b + (b**2 - 4*a*c)** (1/2))/(2*a))
root2 = (-b - (b**2 - 4*a*c)** (1/2))/(2*a)
d = (b**2 - 4*a*c)
if (d < 0) :
    print("both the roots are complex")
elif (d >= 0 and(root1==root2) ) :
    print("both roots are real and equal")
elif(root1 != root2):
    print("both roots are real and distinct")