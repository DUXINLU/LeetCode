#
# 根据顾客属性计算出顾客排队顺序
# @param a int整型一维数组 顾客a属性
# @param b int整型一维数组 顾客b属性
# @return int整型一维数组
#
class Solution:
    def WaitInLine(self , a , b ):
        c = []
        ans = []

        for i in range(len(a)):
            c.append(a[i] - b[i])

        for _ in range(len(c)):
            index = c.index(max(c))
            ans.append(index+1)
            c[index] = -99999999

        return ans