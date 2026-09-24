class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) > len(words[j]):
                    continue

                for x in range(len(words[i])):
                    if words[i][x] != words[j][x] or words[i][x] != words[j][-len(words[i]) + x]:
                        break
                else:
                    count += 1

        return count
