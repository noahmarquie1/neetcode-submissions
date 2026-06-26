from collections import defaultdict

class Solution:
    def __init__(self):
        self.window_letters = defaultdict(int)
    
    
    def to_replace(self):
        return sum(self.window_letters.values()) - max(self.window_letters.values())


    def characterReplacement(self, s: str, k: int) -> int:
        # initialize window with index 0 included
        start = 0
        end = 0
        max_len = 1
        self.window_letters[s[0]] += 1

        while end < len(s) - 1:
            # step the sliding window
            end += 1
            self.window_letters[s[end]] += 1

            # contract however much is necessary
            while self.to_replace() > k:
                self.window_letters[s[start]] -=1
                start += 1

            max_len = max(max_len, (end - start) + 1)

        return max_len

            
            

    