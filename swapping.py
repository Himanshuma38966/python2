def showtextinsidefile():

    fil = input("enter filename")
    fil2 = input("enter second filename")
    f = open(fil,"r")
    f2= open(fil2,"r")
    fline = f.readlines()
    fline2 = f2.readlines()


    print(fline)
    print(fline2)


showtextinsidefile()


############no. of lines and alphabets and words present inside a file#################
