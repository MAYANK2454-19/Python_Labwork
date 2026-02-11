s = input("Enter your string \n")
letters = 0
digits =0
for i in s :
    if 'a'<= i <= 'z' or 'A' <= i <= 'Z':
        letters +=1
    elif 0<= int(i) <= 9:
        digits += 1
print("No of digits in string : ",digits)
print("No of letters in string : ",letters)