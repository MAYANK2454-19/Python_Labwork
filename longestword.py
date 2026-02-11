s = input("Enter your string \n")
word=""
longest =""
for i in s:
    if i !=" ":
        word += i
    else :
        if(len(word) > len(longest)):
            longest = word
        word=""
if(len(word) > len(longest)):
    longest = word
print("Longest word : ",longest)
print("Length of lonest word : ",len(longest))