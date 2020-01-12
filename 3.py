class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            _=0
            _l=[]
            for j in range(i,len(s)):
                if s[j] in _l:
                    break
                else:
                    _l.append(s[j])
                    _=_+1
            if _>res:
                res=_
        return res
