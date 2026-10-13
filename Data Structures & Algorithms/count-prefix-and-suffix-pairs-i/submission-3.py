class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) > len(words[j]):
                    continue
                isPrefixAndSuffix = True

                for k, char in enumerate(words[i]):
                    if not char == words[j][k] or not char == words[j][len(words[j]) - len(words[i]) + k]:
                        isPrefixAndSuffix = False
                
                cnt += isPrefixAndSuffix

        return cnt


                        