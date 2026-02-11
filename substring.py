main_string = input("Enter your string \n")
sub_string= input("Enter substring \n")
count = 0
i = 0
while i<= len(main_string)-len(sub_string):
    if main_string[i:i+len(sub_string)] == sub_string :
    
        count +=1
    i+=1
print("NO of occurence of substring : ",count)