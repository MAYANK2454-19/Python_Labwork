s = input("Enter your string \n")
new_word = True 
text = ""
for i in s :
    
    if new_word and 'a' <= i <= 'z':
        text+=chr(ord(i)-32)
        new_word = False
    else :
        text +=i
        if i == " ":
            
            new_word=True
        else :
            new_word= False
        
print("Updated string : ",text)
