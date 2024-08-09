class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = s.split()
        res = len(lis[-1])
        return res
a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))
