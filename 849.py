class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        s="".join(str(x) for x in seats).split('1')
        print(s)
        max_len=0
        for i in range(len(s)):
            if i==0 or i==len(s)-1:
                if len(s[i]) > max_len:
                    max_len = len(s[i])
            elif (len(s[i])+1)//2>max_len:
                max_len=(len(s[i])+1)//2
        print(max_len)
        return max_len