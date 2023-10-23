class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                r += i[0]
            else:
                return r
        return r