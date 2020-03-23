class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False
        p1, p2, p3 = 0, 0, 0
        while p1 < l1 or p2 < l2:
            if p1 < l1 and s1[p1] == s3[p3]:
                p1 += 1
                p3 += 1
            elif p2 < l2 and s2[p2] == s3[p3]:
                p2 += 1
                p3 += 1
            print(s1[:p1], s2[:p2], s3[:p3])
            if s3[p3] != s2[p2] and s3[p3] != s1[p1] and p1 < l1 and p2 < l2 and p3 < l3:
                return False
        return True


'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words_list = []
        max_len = 0
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
        for word in words:
            words_list.append([])
            word = list(word)
            for i in range(max_len):
                if i < len(word):
                    words_list[-1].append(order.index(word[i]))
                else:
                    words_list[-1].append(0)
        for j in range(max_len):
            for i in range(1, len(words_list)):
                if words_list[i][j] < words_list[i - 1][j]:
                    return False
        return True
'''

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
