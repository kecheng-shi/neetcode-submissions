class Solution:
    def reorganizeString(self, s: str) -> str:
        hash_map = defaultdict(int)
        for char in s:
            hash_map[char] += 1

        max_heap= []
        for key, val in hash_map.items():
            max_heap.append([-val, key])

        heapq.heapify(max_heap)

        prev = None
        res = ""

        while max_heap or prev:
            if prev and not max_heap:
                return ""

            cnt, char = heapq.heappop(max_heap)
            cnt += 1
            res += char

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


                