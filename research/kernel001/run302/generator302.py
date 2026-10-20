def patterns(n):
 k=n//2
 d=[('zero_run','0'*n),('one_then_zeros','1'+'0'*(n-1)),('one_run','1'*n),('zero_then_ones','0'+'1'*(n-1)),('alternate_01',('01'*((n+1)//2))[:n]),('alternate_10',('10'*((n+1)//2))[:n]),('two_zero_then_one','001'+'0'*(n-3)),('two_ones','1'+'0'*(k-1)+'1'+'0'*(n-k-1))]
 return list(dict((w,(name,w)) for name,w in d).values())
