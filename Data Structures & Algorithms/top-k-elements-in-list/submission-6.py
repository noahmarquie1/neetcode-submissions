from collections import defaultdict

class Solution:
    def min_freq_element(self, elements, freq_map):
        # returns index and frequency of element with least frequency
        if len(elements) == 0:
            return None
        
        min_freq = freq_map[elements[0]]
        min_idx = 0
        for i in range(len(elements)):
            if freq_map[elements[i]] < min_freq:
                min_idx = i
                min_freq = freq_map[elements[i]]

        return min_idx, min_freq

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int) 
        top_k = []
        
        for i, num in enumerate(nums):
            freq_map[num] += 1
            if num not in top_k and len(top_k) < k:
                top_k.append(num)
            elif num not in top_k:
                min_idx, min_freq = self.min_freq_element(top_k, freq_map)
                if freq_map[num] > min_freq:
                    top_k[min_idx] = num

        return top_k
        