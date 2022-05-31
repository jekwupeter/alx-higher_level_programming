def uppercase(str):
    """
    uppercase - prints a string in uppercase
    @str - input string
    """
    for i in str:
        if ord(i) in range(97, 123):
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()
