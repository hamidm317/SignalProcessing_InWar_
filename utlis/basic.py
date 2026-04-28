pi = 3.1415926535897913
e = 2.718281828459045

def factorial(a):

    if a == 1 or a == 0:

        return 1
    
    else:

        return a * factorial(a - 1)
    
def int_power(x, n):

    if n == 0:

        return 1
    
    else:

        return x * int_power(x, n - 1)
    
def sgn(x):

    if x > 0:

        return 1
    
    elif x == 0:

        return 0
    
    else:

        return -1
    
def absv(x):

    return sgn(x) * x

def exp_term_n_(x, n):

    return int_power(x, n) / factorial(n)

def exp_double(x, precision = 15):

    res_by_prec = 0

    for n in range(precision):

        res_by_prec = res_by_prec + exp_term_n_(x, n)

    return res_by_prec

def exp(x, precision = 50):

    if x < 1:

        return exp_double(x, precision = precision)
    
    else:

        e = exp_double(1, precision = 40)

        x_int = int(x)
        rest_of_x = x - x_int

        return int_power(e, x_int) * exp_double(rest_of_x)
    
def mod_ft(a, k = 2):
        
    return a - int(a / k) * k

def sqrt(x, n = 2, precision = 50, bad_est = True):

    if bad_est:

        return exp(ln_(x) / n)

    else:

        import numpy as np

        return np.sqrt(x)

def is_even(x):

    return int(x / 2) == x / 2

def sln_term_n_(x, n):

    if is_even(n):

        coeff = -1

    else:

        coeff = 1

    den = n
    uny = int_power(x, n)

    return coeff * uny / den

def small_ln(x, precision = 150):

    res_by_prec = 0

    for n in range(1, precision):

        res_by_prec = res_by_prec + sln_term_n_(x, n)

    return res_by_prec

def nearest_power_of(n, base = 2, greater = True, return_power = False):

    a = 1
    i = 0

    while a < n:

        a = a * base
        i = i + 1

    if greater:

        if return_power:

            return a, i
        
        else:

            return a

    else:

        if return_power:

            return a / base, i - 1
        
        else:

            return a / base

def ln_(x_, precision = 150):

    # x_b, i_b = nearest_power_of(x_, base = e, greater = False, return_power = True)

    # x = x_ - x_b

    i_b, x = base_analyzer(x_, base = e)

    return i_b + small_ln(x - 1, precision = precision)

def base_analyzer(a, base = 10):

    a_ = a
    i = 0

    if a_ >= base:

        while a_ / base >= 1:

            a_ = a_ / base
            i = i + 1

        return i, a_

    else:

        while a_ * base <= 1:

            a_ = a_ * base
            i = i + 1

        return -1 * i, a_