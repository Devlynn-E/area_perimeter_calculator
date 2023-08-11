def num_check(question):

    valid = False
    while not valid:

        error = "please input a number above zero you knob"

        try:

            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

    valid = False
    while not valid:

        error = "please input a number above zero you knob"

        try:

            length = float(input("enter the length: "))

            if length > 0:
                valid = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)


width = num_check("width: ")
height = num_check("height: ")
print()
print("width", width)
print("height:", height)
print()


perimeter = 2 * (width + height)
area = width * height

print("the perimeter is: {}".format(perimeter))
print()
print("the area is: {}".format(area))
print()
