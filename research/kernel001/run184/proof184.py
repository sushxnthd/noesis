from research.kernel001.run184.clock184 import clock
WORD='1110001001'
def prove():
 out=[clock(WORD[i:]+WORD[:i]) for i in range(10)]
 assert out==[None,186,87,57,87,186,None,186,None,148]
 return out
if __name__=='__main__':print('EXACT RATIONAL PASS',prove())
