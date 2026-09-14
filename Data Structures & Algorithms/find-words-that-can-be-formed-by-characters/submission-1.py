class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for char in chars:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        
        length = 0

        for word in words:
            dic2 = dic.copy()
            valid = True
            for char in word:
                if char in dic2 and dic2[char] >= 1:
                    dic2[char] -= 1
                else:
                    valid = False
                    break
            if valid:
                length += len(word)
            
        return length
