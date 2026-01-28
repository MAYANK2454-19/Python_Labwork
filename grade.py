marks = int(input("Enter your marks : "))
if (marks < 0 or marks > 100):
    print("Invalid input")
elif marks < 50 :
    print("Grade is F ")
elif marks >= 50 and marks < 60 :
    print("Grade is D ")
elif marks >= 60 and marks < 70:
    print("Grade is C ")
elif marks >= 70 and marks < 80 :
    print("Grade is B ")
elif marks >= 80 and marks < 90 :
    print("Grade is A ")
elif marks >= 90 :
    print("Grade is A+ ")