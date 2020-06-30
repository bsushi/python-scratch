#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

# Copyright (c) 2020 Steve Chappell
# SPDX-License-Identifier: MIT

# Generate all the unique combinations of "anagramming" a string
#  All letters are used, and no, they aren't checked against a dictionary

import sys


class PermU:
    def __init__(self, inStr, isSorted = True):
        self.letterlist = list(inStr)
        if not isSorted:
            self.letterlist.sort()

    def got_one(self, val):
        self.count += 1
        print(val)    # or add it to a list or whatever

    def permute(self, prefix, lst):
        if len(lst) == 0:
            return 
        if len(lst) == 1:
            self.got_one(prefix+lst[0])
            return
            
        last = ''
        for i in range(len(lst)):
            val = lst.pop(i)
            if val != last:
                self.permute(prefix+val,lst)
            lst.insert(i, val)
            last = val

    def gen(self):
        self.count = 0
        self.permute("",self.letterlist)
        print(str(self.count)+" unique permutations")

def main():
    pu = PermU("aabc")
    pu.gen()
    pu = PermU("caba")
    pu.gen()
    pu = PermU("caba", False)
    pu.gen()

if __name__ == '__main__':
    main()