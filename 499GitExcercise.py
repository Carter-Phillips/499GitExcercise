# 499GitExcercise
#
#
# Carter Phillips   - Print a line
# Rickson Reichmann - Print a cross
# Erik Johnston     - Print a square
# Matthew Borle     - Print a triangle
#
# LIMS(1)
#
# September 21, 2021


# Ask for input forever
while True:
    # Which type to print 
    shape_type = input("Line, Cross, Square, or Triangle? (Ll/Cc/Ss/Tt): ")


    # LINE - Carter
    if shape_type == "L" or shape_type == "l":
        print ("Line:\n")


    # Cross - Rickson
    elif shape_type == "C" or shape_type == "c":
        print ("Cross:\n")


    # Square - Erik
    elif shape_type == "S" or shape_type == "s":
        print ("Square:\n")
        print (' ________')
        for x in range(5):
            print ('|        |')
        print (' ‾‾‾‾‾‾‾‾\n')
    

    # Triangle - Matthew
    elif shape_type == "T" or shape_type == "t":
        print ("Triangle:\n")
        print ("     /\\")
        print ("    /  \\")
        print ("   /    \\")
        print ("  /______\\\n")


    # Invalid
    else:
        print ("Invalid input type. Try again.\nInterrupt to quit\n")
