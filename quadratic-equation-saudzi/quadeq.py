# finds solutions to quadratic equations like
#   ax2 + bx + c = 0, where
#   a, b and c are real numbers and
#   a  ≠ 0

import cmath

def quadeq():

    # cycles until a valid number is given to input and then places it in a
    # fills variables a , b and c required for solving the equation
    while True:
        try:
            a = float(input("Please enter a valid value for a: "))
        except ValueError:
            print("Please enter a valid number ( integer or a double )")
            continue
        else:
            break

    while True:
        try:
            b = float(input("Please enter a valid value for b: "))
        except ValueError:
            print("Please enter a valid number ( integer or a double )")
            continue
        else:
            break

    while True:
        try:
            c = float(input("Please enter a valid value for c: "))
        except ValueError:
            print("Please enter a valid number ( integer or a double )")
            continue
        else:
            break



    # calculate and print discriminant
    d = (b**2)-(4*a*c)
    print("Discriminant is: ",d)

    # id discriminant is less than 0 then we have no solutions for the equation
    if ( d>=0 ) :
        #save solutions then print
        solution1 = ((-b-cmath.sqrt(d))/(2*a)).real
        solution2 = ((-b+cmath.sqrt(d))/(2*a)).real

        if (solution1==solution2) :
            print("your equation had only 1 solution and that being: ",solution1)
        
        else :
            print("Solutions 1 and 2 respectively are: ",solution1," & ",solution2)
        

    else :
        print("Discriminant is negative, thus we have no solutions")
