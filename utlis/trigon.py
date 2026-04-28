import utlis.basic as bsc

def sin(x_, precision = 50):

    x = bsc.mod_ft(x_, k = bsc.pi)

    est_by_prec = 0

    for n in range(precision):

        est_by_prec = est_by_prec + sin_term_n_(x, n)

    return est_by_prec

def cos(x_, precision = 50):

    x = bsc.mod_ft(x_, k = bsc.pi)

    est_by_prec = 0

    for n in range(precision):

        est_by_prec = est_by_prec + cos_term_n_(x, n)

    return est_by_prec

def sin_term_n_(x, n):

    coef = bsc.int_power(-1, n)
    den = bsc.factorial(2 * n + 1)
    uny = bsc.int_power(x, 2 * n + 1)

    return coef * uny / den

def cos_term_n_(x, n):

    coef = bsc.int_power(-1, n)
    den = bsc.factorial(2 * n)
    uny = bsc.int_power(x, 2 * n)

    return coef * uny / den

def tan(x, precision = 50):

    return sin(x, precision = precision) / (cos(x, precision = precision) + 1e-20)

def atan_term_n_(x, n):

    coef = bsc.int_power(-1, n)
    den = 2 * n + 1
    uny = bsc.int_power(x, 2 * n + 1)

    return coef * uny / den

def atan(x, precision = 60):

    if bsc.absv(x) < 1:

        f_c = 0
        s_c = 1
        u = x

    else:

        f_c = bsc.sgn(x)
        s_c = -1
        u = 1 / x

    est_by_prec = 0

    for n in range(precision):

        est_by_prec = est_by_prec + atan_term_n_(u, n)

    return f_c * bsc.pi / 2 + s_c * est_by_prec