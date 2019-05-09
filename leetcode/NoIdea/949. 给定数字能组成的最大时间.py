'''给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
示例 1：
输入：[1,2,3,4]
输出："23:41"
示例 2：
输入：[5,5,5,5]
输出：""'''


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        A = A[::-1]
        # 排列组合，且小于23:59
        from itertools import permutations
        for i in permutations(A, 4):
            part1 = int(str(i[0]) + str(i[1]))
            part2 = int(str(i[2]) + str(i[3]))
            if part1 < 24 and part2 < 60:
                return str(i[0]) + str(i[1]) + ':' + str(i[2]) + str(i[3])
        return ""
