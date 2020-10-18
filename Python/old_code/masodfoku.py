import math  # importing math module

a = float(input("Enter a: "))  # getting input for variable a
b = float(input("Enter b: "))  # getting input for variable b
c = float(input("Enter c: "))  # getting input for variable c
D = b ** 2 - 4 * a * c  # defining the discriminant (from now on referred to as "D")
minuszb = int(-1 * b)   # defining b times minus one

if a != 0:  # checking wether a is equal to zero

    if D > 0:  # checking wether D is greater than zero
        print("D is greater than 0 (" + str(D) + ").")  # printing that D is greater than zero and its value
        pluszSzamlalo = float(minuszb + math.sqrt(D))  # declaring the positive counter variable
        minuszSzamlalo = float(minuszb - math.sqrt(D))  # declaring the negative counter variable
        nevezo = 2 * a  # declaring the denominator variable
        x1 = pluszSzamlalo / nevezo  # calculating the value of x1
        x2 = minuszSzamlalo / nevezo  # calculating the value of x2
        print("X1 = " + str(x1) + "  (" + str(pluszSzamlalo) + "/" + str(nevezo) + ")")  # printing the value of x1
        print("X2 = " + str(x2) + "  (" + str(minuszSzamlalo) + "/" + str(nevezo) + ")")  # printing the value of x2

    elif D == 0:  # checking wether D is equal to zero
        print("D is equal to 0.")  # printing the value of D
        Szamlalo = float(minuszb + math.sqrt(D))  # declaring the counter variable
        nevezo = 2 * a  # declaring the denominator variable
        x = Szamlalo / nevezo  # calculating the value of x
        print("X = " + str(x) + "  (" + str(Szamlalo) + "/" + str(nevezo) + ")")  # printing the value of x

    elif D < 0:  # checking wether D is smaller than zero
        print("D is smaller than 0 (" + str(D) + "). No x can be defined")  # printing that D is smaller than zero and its value

else:
    print("a can not be 0.")  # printing that division by zero is not defined

