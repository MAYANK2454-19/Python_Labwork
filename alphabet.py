user_input = (input("Enter your character: "))
user_input = ord(user_input.upper())
if 65 <= user_input and user_input <= 91 :
    print("Your input is an alphabet!")
else :
    print("Your input is NOT an alphabet!")