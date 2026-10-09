class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx = 0
        n = len(abbr)
        i = 0
        while i < n:
            char = abbr[i]
            if char.isdigit():
                if i < len(abbr) - 1 and abbr[i + 1].isdigit():
                    num = int(abbr[i + 1]) + 10 * int(char)
                    i += 1
                else:
                    num = int(char)
                idx += num
                i += 1
            else:
                if idx > len(word) - 1:
                    return False
                else:
                    if char != word[idx]:
                        return False
                idx += 1
                i += 1
        return idx == len(word)