# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:01:42 2016

@author: rub
"""

from datetime import datetime
from scene import *


class Clock(Scene):
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
        
    def setup(self):
        self.background_color = '#262b30'
        self.instructions = LabelNode('The Prime Time Clock',
                                      ('HelveticaNeue-Light', 24),
                                      position = self.size/2,
                                      parent=self)
     def did_change_size(self):
        self.instructions.position = self.size / 2

     def touch_began(self, touch):
        if self.instructions:
            self.instructions = None

    def update(self)
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
        self.instructions = "x".join(pstr)                        
                                    
if __name__ == '__main__':
    run(Clock())
       