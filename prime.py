user_input = int(input("Enter your number : "))
count = 0
if (user_input <= 1):
    print("Not Prime!")
else :
    for i in range (1,user_input+1) :
        if(user_input%i==0):
            count += 1
    if(count > 2) :
        print("Not prime!")
    else :
        print("Prime!")        