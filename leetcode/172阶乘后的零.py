'''给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.'''


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n >= 1:
            n //= 5
            total += n
        return total


if __name__ == '__main__':
    a = Solution()
    n = 50
    p = a.trailingZeroes(n)
    print(p)
