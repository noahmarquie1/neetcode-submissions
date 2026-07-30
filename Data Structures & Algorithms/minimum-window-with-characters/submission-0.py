from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep a set of all the letters in t (1)
        # keep a set of all letters in the current window (2)
        # expand sliding window until all elements from t are in window
        #  - track this by seeing if an element if in set (1) but not set (2),
        #    and increment a count (3) of 't' elements in window
        #  - we know that window is 'valid' if count (3) matches the number of
        #   items in the set (1)
        # if window is valid, retract sliding window until it is not anymore
        # keep a variable (4) representing min length of a valid window seen

        # Actually, use a map with amount of occurences in the string for both 
        # (1) and (2)

        t_map = defaultdict(int)
        for letter in t:
            t_map[letter] += 1

        window_map = defaultdict(int)
        window_t_amt = 0

        # initialize sliding window
        window_start = 0
        window_end = -1


        min_valid_substr = ""

        while window_end < len(s): # window end should be an index in s
            # update min_valid_substr as necessary
            if (window_t_amt == len(t) and
                (min_valid_substr == "" or 
                len(min_valid_substr) > window_end - window_start + 1)):
                min_valid_substr = s[window_start:window_end+1]
            
            # expand or contract window as necessary
            if window_t_amt < len(t) or window_start >= window_end:
                window_end += 1
                if window_end < len(s): # handle t count 
                    new_let = s[window_end]
                    if window_map[new_let] < t_map[new_let]:
                        window_t_amt += 1
                    window_map[new_let] += 1

            else:
                old_let = s[window_start]
                if (window_map[old_let] <= t_map[old_let]):
                    window_t_amt -= 1
                window_map[old_let] -= 1
                window_start += 1

        return min_valid_substr
                

                    





        