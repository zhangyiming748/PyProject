'''自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]'''


# class Solution:
#     def selfDividingNumbers(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: List[int]
#         """
#         res = []
#         for i in range(left, right + 1):
#             flag = True
#             tmp = i
#             while tmp > 0:
#                 num = tmp % 10
#                 tmp //= 10
#                 if not num or i % num:
#                     flag = False
#                     break
#
#             if flag:
#                 res.append(i)
#
#         return res
if __name__ == '__main__':
    start =1
    end = 22
    alllist =[]
    for i in range(start,end+1):
        alllist.append(i)
    #创建列表
    ablelist=[]
    for i in alllist:
        if i%10==0：
            pass