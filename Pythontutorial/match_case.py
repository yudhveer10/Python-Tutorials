a = int(input("Enter a number between 1 to 10:" ))

match a :
    case 1:
        print("You won a charger")
    case 3:
        print("You won a trip to hometown")
    case 6:
        print("You won a flight ticket")  
    case _:
        print("Better luck next time")

#Similar to switch cases in other programming language
