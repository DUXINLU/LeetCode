class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split(" ")
        for i in range(s.count('')):
            s.remove('')
        s.reverse()
        return ' '.join(s)