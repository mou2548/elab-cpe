def nb_year(p0, percent, aug, p):
    days = 0
    while p0 < p:
        days += 1
        p0 += round(p0 * percent/100 + aug)
    return days
