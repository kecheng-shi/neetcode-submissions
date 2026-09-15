class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    if self.isPrefixAndSuffix(words[i], words[j]):
                        count += 1
        return count


    def isPrefixAndSuffix(self, str1, str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
            if str1[-1 - i] != str2[-1 - i]:
                return False

        return True