s = input("Enter your string \n")
lower_string=""
upper_string=""
for i in s:
    if 'a'<= i <='z' :
        upper_string += chr(ord(i)-32)
    else :
        upper_string += i
    if'A'<= i <='Z' :
        lower_string += chr(ord(i)+32)
    else :
         lower_string += i
print("lower case string : ", lower_string)
print("upper case string : ", upper_string)