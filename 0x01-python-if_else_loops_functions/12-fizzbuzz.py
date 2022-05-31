def fizzbuzz():
    """
    fizzbuzz -custom print number from 1 to 100
    """
    for i in range (1, 101):
        if i % 3 == 0:
            print("fizz", end=" ")
        elif i % 5 == 0:
            print("buzz", end=" ")
        else:
            print(i, end=" ")
