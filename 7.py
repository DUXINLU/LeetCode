from typing import *
class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            l=list(str(x))
            l.reverse()
            r=int("".join(l))
            if r>2147483647 or r<-2147483648:
                return 0
            return r
        elif x==0:
            return 0
        else:
            l=list(str(x)[1:])
            l.reverse()
            r=int("-"+"".join(l))
            if r>2147483647 or r<-2147483648:
                return 0
            return r

if __name__=='__main__':
    s=Solution()
    s.reverse(123)
