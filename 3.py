# coding=UTF-8
'''
version 1
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
'''
'''
version 2
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slide = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in slide:
                slide.append(s[i])
                if len(slide) > max_len:
                    max_len = len(slide)
            else:
                slide[:] = slide[slide.index(s[i])+1:]
                slide.append(s[i])
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
