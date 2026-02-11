s = input("Enter your string \n")
vowels=0
consonants=0
spaces=0
for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch == " ":
        spaces += 1
    else :
        consonants +=1 
print("No of vowels : ",vowels)
print("No of consonants : ",consonants)
print("No of spaces : ",spaces)