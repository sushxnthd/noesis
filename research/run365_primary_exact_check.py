#!/usr/bin/env python3
"""Dependency-free exact tests for the frozen NOESIS R363–R365 primary tables.
The contingency tables are independently archived; this script is not a raw-data evaluator.
"""
from math import comb

def fisher_greater(a,b,c,d):
    row=a+b;events=a+c;total=a+b+c+d
    return sum(comb(events,k)*comb(total-events,row-k)/comb(total,row)
               for k in range(a,min(row,events)+1)
               if 0<=row-k<=total-events)

def discordant_greater(a,b):
    n=a+b
    return sum(comb(n,k) for k in range(a,n+1))/2**n

p363=fisher_greater(8,1,25,39)
p364=discordant_greater(16,0)
p365=discordant_greater(18,0)
assert abs(p363-0.006117850978351585)<1e-14
assert p364==1/65536
assert p365==1/262144
print(f'R363 Fisher one-sided: {p363:.12g}')
print(f'R364 paired exact one-sided: {p364:.12g}')
print(f'R365 paired exact one-sided: {p365:.12g}')
