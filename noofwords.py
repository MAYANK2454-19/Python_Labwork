s = input("Enter your string \n")
words = 0
in_word = False
for i in s :
    if i != " " and not in_word :
        words +=1
        in_word=True
    elif i == " ":
        in_word=False
print("No of words : ",words)