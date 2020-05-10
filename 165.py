class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        l1 = len(v1)
        for i in range(l1):
            v1[i] = int(v1[i])
        v2 = version2.split('.')
        l2 = len(v2)
        for i in range(l2):
            v2[i] = int(v2[i])

        if l1 < l2:
            for i in range(l2 - l1):
                v1.append(0)
        if l1 > l2:
            for i in range(l1 - l2):
                v2.append(0)

        # print(v1,v2)
        for i in range(max(l1, l2)):
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1
        return 0
