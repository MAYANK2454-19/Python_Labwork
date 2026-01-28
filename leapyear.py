user_input = int(input("Enter your year : "))
if (user_input % 4 == 0) and (user_input % 100 != 0 or user_input % 400 == 0) :
    print(f"{user_input} is a leap year!")
else :
    print(f"{user_input} is NOT a leap year!")