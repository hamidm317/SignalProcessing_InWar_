def cplxer(x):

    if is_cmplx_els(x):

        return x
    
    elif type(x) in [int, float]:

        return (x, 0)
    
    else:

        print('NoneType Warning', x, type(x))

        return None

def is_all_cmplx(nmbr_list, assert_error = True):

    if assert_error:

        for nmbr in nmbr_list:

            if not is_cmplx(nmbr):

                return False
            
        return True
    
    else:

        for nmbr in nmbr_list:

            if not is_cmplx_els(nmbr):

                return False
            
        return True
    
def is_cmplx_els(nmbr):

    return type(nmbr) is tuple and len(nmbr) == 2 and type(nmbr[0]) in [float, int] and type(nmbr[1]) in [float, int]
 
def is_cmplx(nmbr):

    assert type(nmbr) is tuple, "complex number (real + 1i * imag) must be a (real, imag) tuple"
    assert len(nmbr) == 2, "complex number must be exactly length of 2!"

    assert type(nmbr[0]) in [float, int] and type(nmbr[1]) in [float, int], "tuple elements must be integer"

    return True

def add(x_, y_):

    x = cplxer(x_)
    y = cplxer(y_)

    return (x[0] + y[0], x[1] + y[1])

def mul(x_, y_):

    x = cplxer(x_)
    y = cplxer(y_)

    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    
def real(x):

    if type(x) in [int, float]:

        return x
    
    else:

        if is_cmplx(x):

            return x[0]
        
        else:

            return None
    
def imag(x):

    if type(x) in [int, float]:

        return 0
    
    else:

        if is_cmplx(x):

            return x[1]
        
        else:

            return None
    
def abs(xlist):

    import utlis.basic as bsx

    x_abs = []

    if type(xlist) is not list:

        xlist = [xlist]

    for x in xlist:

        x_ = cplxer(x)

        x_abs.append(bsx.sqrt(sum([x__ ** 2 for x__ in x_]), bad_est=False))

    return x_abs
    
def angle(x):

    import utlis.trigon as tri

    if type(x) in [int, float]:

        return 0
    
    else:

        if is_cmplx(x):

            return tri.atan(x[1] / x[0])
        
        else:

            return None
    
def exp(x):

    if type(x) in [int, float]:

        return bsx.exp(x)
    
    else:

        if is_cmplx(x):

            import utlis.basic as bsx
            import utlis.trigon as tri

            m = bsx.exp(x[0])

            an_r = tri.cos(x[1])
            an_i = tri.sin(x[1])

            return (m * an_r, m * an_i)
        
        else:

            return None