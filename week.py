user_input = int(input("Enter your week number : "))
match user_input :
    case (1) :
        print("Monday!")
    case (2) :
        print("Tueday!")
    case (3) :
        print("Wedday!")
    case (4) :
        print("Thursay!")
    case (5) :
        print("Friday!")
    case (6) :
        print("Saturday!")
    case (7) :
        print("Sunday!")
    case _:
        print("Invalid input")

