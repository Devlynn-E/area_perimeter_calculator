valid = False
while not valid:

    error = "please input a number above zero you knob"

    try:

        response = float(input("enter a number: "))

        if response > 0:
            valid = True

        else:
            print(error)
            print()

    except ValueError:
        print(error)
