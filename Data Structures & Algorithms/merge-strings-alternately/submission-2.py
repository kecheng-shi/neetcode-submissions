class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        k = 0
        res = ""

        while i < len(word1) or k < len(word2):
            if i < len(word1):
                res += word1[i] 
            if k < len(word2):
                res += word2[k]
            i += 1
            k += 1
        
        return res
