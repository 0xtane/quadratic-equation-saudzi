# finds solutions to quadratic equations like
#   ax2 + bx + c = 0, where
#   a, b and c are real numbers and
#   a  ≠ 0

import cmath
import tkinter as tk

def quadeqinput():

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



def quadeq(a,b,c):

    # sees if numbers given to function are able to be parsed to float
    # if not returns 0

    try:
        test = float(a) + float (b) + float (c)
    except ValueError:
        print("Please enter a valid number ( integer or a double )")
        return 0

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


def quadeqgui():

    	
    def calculator():

        try:
            test = float(aentry.get()) + float (bentry.get()) + float (centry.get())
        except ValueError:
            output['text']=("Please enter valid numbers ( integers or a doubles )")
            return 1

        a = float(aentry.get())
        b = float(bentry.get())
        c = float(centry.get())
        
        d = (b**2)-(4*a*c)
    

        # id discriminant is less than 0 then we have no solutions for the equation
        if ( d>=0 ) :
            #save solutions then print
            solution1 = ((-b-cmath.sqrt(d))/(2*a)).real
            solution2 = ((-b+cmath.sqrt(d))/(2*a)).real

            if (solution1==solution2) :
                output['text']="we have 1 solution: X = "+str(solution1)
            
            else :
                output['text'] = "Solutions 1 and 2 respectively are: "+ str(solution1) +" & " +str(solution2)
            

        else :
            output['text']="There are no solutions since Discriminant is less than 0"






    window = tk.Tk()
    window.title("Quadeq by saudzi")
    window.geometry('600x600')
    window.configure(background="grey")


    
    hall = tk.Label(window, background="white")
    hall.pack()


    	
    labela = tk.Label(window, background="grey", text=" ( A ) ")
    labela.pack()
    aentry = tk.Entry(window)
    aentry.pack()
    labelb = tk.Label(window, background="grey", text=" ( B ) ")
    labelb.pack()
    bentry = tk.Entry(window)
    bentry.pack()
    labelc = tk.Label(window, background="grey", text=" ( C ) ")
    labelc.pack()
    centry = tk.Entry(window)
    centry.pack()
    ######

    hall = tk.Label(window, background="white")
    hall.pack()

    calculator = tk.Button(window, text="Calculate", command=calculator)
    calculator.pack()


    hall = tk.Label(window, background="white")
    hall.pack()

    output = tk.Label(window, height=100, width=200, background="lightgray")
    output.pack()
    output['text']="Waiting for values a,b,c"


    
    window.mainloop()