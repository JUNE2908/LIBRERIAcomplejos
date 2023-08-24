import math
def sumac(a,b):

    d1 = a[0]
    d2 = a[1]
    d3 = b[0]
    d4 = b[1]

    par1 = (d1 + d3)
    par2 = (d2 + d4)

    return (par1, par2)

def producc(a,b):

    d1 = a[0]
    d2 = a[1]
    d3 = b[0]
    d4 = b[1]

    par1 = (d1 * d3) - (d2 * d4)
    par2 = (d1 * d4) + (d2 * d3)

    return (par1,par2)
    
def restc(a,b):

    d1 = a[0]
    d2 = a[1]
    d3 = b[0]
    d4 = b[1]

    par1 = (d1 - d3)
    par2 = (d2 - d4)

    return (par1, par2)

def divic(a,b):

    d1 = a[0]
    d2 = a[1]
    d3 = b[0]
    d4 = b[1]    

    par1 = (d1 * d2) + (d3 * d4)
    par2 = (d2 * d3) - (d1 * d4)
    par3 = (d2 ** 2) + (d4 ** 2)
    solu1 = (par1 / par3)
    solu2 = (par2 / par3)

    return(solu1, solu2)

def moduloc (a):

    t1 = (a[0]** 2)
    t2 = (a[1]** 2)

    solu = math.sqrt(t1 + t2)

    return solu

def conjuc(a):

    tt  = (a[1] * -1)

    return (a[0], tt)


def cartc (a):



    dat1 = moduloc(a)
    dat2 = fasec(a)
    dat3 = math.cos(dat2)
    dat4 = math.sin(dat2)

    solu1 = (dat1 * dat3)
    solu2 = (dat1 * dat4)
    
    return (solu1, solu2)
    
    

def fasec (a):

    x1 = (a[1] / a[0])
    solu = math.atan(x1)

    return solu

def main():

    print(sumac((6,5),(7,5)))
    print(producc((12,6),(-5,1)))
    print(restc ((1,4),(7,9)))
    print(divic((2,5),(2,-4.6)))
    print(moduloc((5,12)))
    print(conjuc ((-4,-9)))
    print(fasec ((18,2)))
    print(cartc ((3,6)))

main()
    
    
