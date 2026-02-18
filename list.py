#1
list = ["10","20","30","50","100","90","80"]
#a
count = 0
for i in list :
    count += 1
print("The length of the list is :",count)
#b
print("The element at index zero is :",list[0])
#c
print("Enter the element you want add :")
new= [input()]
list = list + new
print(list)
#d
print("printing last elemnt of the list  using negative indexing :",list[-1])
#e
list_new=[]
object = input("enter element you want to remove :")
list.remove(object)
print(list)
#f
sorted_list=[]
for i in range (0,len(list)) :
    sorted_list.append(int(list[i]))
print(sorted_list)
for j in range (len(sorted_list)):
    for i in range (len(sorted_list)-1) :
        if sorted_list[i] > sorted_list[i+1] :
            temp = sorted_list[i]  
            sorted_list[i]= sorted_list[i+1]
            sorted_list[i+1] = temp
print("The sorted list is : ",sorted_list)
#2
#a
sum = 0
for i in sorted_list :
    sum +=i
mean = sum / len(sorted_list)
print("Mean : ",round (mean,2))
#b
count_new=0
for i in sorted_list :
    count_new += 1
print("The length of the list is :",count_new)
print(sorted_list)
if count % 2 == 0 :
    mid1 = sorted_list[count_new//2 - 1]
    mid2 = sorted_list[count_new//2]
    median = (mid1 + mid2)/2
else :
    median = sorted_list[count_new//2]
print("Median :",round(median,2))
    
#3
max_count=0
for i in list:
    count_mode = 0 
    for j in list :
        if i == j :
            count_mode += 1
        if count_mode > max_count :
            max_count= count_mode
val = 0
mode_list = []
for i in list:
    count_mode = 0 
    for j in list :
        if i == j :
            count_mode += 1
        if count_mode == max_count :
            if i not in mode_list:
                mode_list.append(i)
            
for e in mode_list:
    print(e,"is a mode ")
