# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """This function asks for input, places the input in memory (a, b), and returns a,b."""
    # the return shown below is a placeholder to make sure this runs

    aString = input("give me x: ")
    a = int(aString)
    bString = input("give me y: ")
    b = int(bString)
    return a,b

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """this mutiplies a and b and prints the result"""
    mult = (a*b)
    print("mult result:",mult)
    
    add = (a+b)
    print("add result:",add)
    
    ab_multadd = mult/add

    return ab_multadd

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
        """This is where we make things fancy"""
        print("****************")
        print("RESULTS:")
        print("first number:", a)
        print("second number:",b)
        print("multadd result:",round(ab_multadd, 1))
        print("================")
        
def main ():
    
    
    
    
    """This is where I call my functions"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x,y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
  

    xy_multadd = compute_multadd(x,y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy (x,y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
