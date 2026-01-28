user_input = int(input("Enter your number : "))
if (user_input % 6 == 0):
    print("Number is divisible by both 2 and 3")
elif (user_input % 2 == 0):
    print("Number is divisible by 2 ")
elif (user_input % 3 == 0):
    print("Number is divisible 3")
else :
    print("Number is NOT divisible by either 2 or 3")