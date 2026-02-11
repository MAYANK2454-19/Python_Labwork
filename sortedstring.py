s = input("Enter your string \n")
s_list = list(s)
for i in range(len(s_list)):
    for j in range (i+1,len(s_list)):
        if s_list[i]> s_list[j]:
            s_list[i],s_list[j]=s_list[j],s_list[i]
sorted = ""
for t in s_list :
    sorted += t
print("sorted string : ", sorted)