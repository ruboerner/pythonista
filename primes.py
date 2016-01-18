# -*- coding: utf-8 -*-
"""
Find prime numbers.
"""

import numpy as np
from datetime import datetime

def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,2,6]
    length, cycle = 11, 3
    f, fs, next = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[next]
        next += 1
        if next == length:
            next = cycle
    if n > 1: fs.append(n)
    return fs

t = datetime.now()
seconds = t.second
minutes = t.minute
hours = (t.hour % 12)

tt = hours * 10000 + minutes * 100 + seconds

pf = factors(tt)

primefactors = np.asarray(pf)

pstr = []
for i in range(0, len(primefactors)):
    pstr.append("%d" % primefactors[i])
primetime = " * ".join(pstr)

print t.strftime("%H:%M:%S")

print primetime
