print("\n**** welcome to the area / perimeter calculator ****")


def num_check(question):

    valid = False
    while not valid:

        error = "please input a number above zero"

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

        error = "please input a number above zero"

        try:

            length = float(input("enter the length: "))

            if length > 0:
                valid = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":

    width = num_check("width: ")
    height = num_check("height: ")
    print("\nwidth", width)
    print("height:", height)

    perimeter = 2 * (width + height)
    area = width * height

    print("\nthe perimeter is: {} units".format(perimeter))
    print("\nthe area is: {} square units".format(area))

    keep_going = input("\npress <enter> to enter more or anything else to leave")

print("\n** thanks for using my area / perimeter calculator **")
