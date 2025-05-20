while True:
    try:
        a = int(input("Enter number One: "))
        b = int(input("Enter number Two: "))

        print(f"The sum is {a + b}")

    except Exception as e:
        print("Some error occurred! ", e)
