class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = len(s) - 1
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        while i < j:
            if s_list[i] not in vowels:
                i += 1
            if s_list[j] not in vowels:
                j -= 1
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        return "".join(s_list)