class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        _=str(x)[::-1]
        if s==_:
            return True
        return False
