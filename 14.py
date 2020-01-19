class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans=""
        _=""
        flag=True
        for i in range(len(min(strs))):
            _=strs[0][i]
            for j in strs:
                if j[i]!=_:
                    flag=False
            if flag:
                ans+=_
            else:
                return ans
        return ans