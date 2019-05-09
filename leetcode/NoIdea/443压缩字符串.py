'''给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。



进阶：
你能否仅使用O(1) 空间解决问题？



示例 1：

输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
示例 2：

输入：
["a"]

输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。
示例 3：

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。'''


# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """
#         if len(chars) < 2:
#             return len(chars)
#         count = 1
#         first = 0
#         for i in range(len(chars)-1):
#             if chars[i] == chars[i+1]:
#                 count += 1
#             else:
#                 chars[first] = chars[i]
#                 if count > 1:
#                     count = list(str(count))
#                     for _ in count:
#                         first += 1
#                         chars[first] = _
#                 first += 1
#                 count = 1
#         if count != 1:
#             chars[first] = chars[-1]
#             count = list(str(count))
#             for _ in count:
#                 first += 1
#                 chars[first] = _
#             return first+1
#         else:
#             chars[first] = chars[-1]
#             return first+1
# if __name__ == '__main__':
#     l=["a", "a", "b", "b", "c", "c", "c"]
#     a=Solution()
#     p=a.compress(l)
#     print(p)
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        j = 1
        for i in range(n):
            c = chars.pop(0)
            if i == 0:
                chars.append(c)
            else:
                if c == chars[-1]:
                    j += 1
                else:
                    if j > 1:
                        chars.extend(list(str(j)))
                    else:
                        pass
                    chars.append(c)
                    j = 1
        if j > 1:
            chars.extend(list(str(j)))