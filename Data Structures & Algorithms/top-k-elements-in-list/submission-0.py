class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        import heapq
        for num in nums:
            map[num] = map.get(num, 0) + 1
        # print(map)
        heap = []

        for num in map.keys():
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # print([num for freq, v in heap)
        print(heap)
        res = [v for freq, v in heap]
        print(res)
        return res