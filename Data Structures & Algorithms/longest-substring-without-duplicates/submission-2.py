class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        last = 0 
        longest = 0

        chars: dict[char, list[int]] = {}

        while last < len(s):
            # first extend condition (no duplicates)
            if not s[last] in chars.keys():
                chars[s[last]] = [last]
                longest = max(longest, last - first + 1)
                last += 1
            elif chars[s[last]][-1] < first:
                chars[s[last]].append(last)
                longest = max(longest, last - first + 1)
                last += 1

            # collapse condition
            elif first < last:
                first += 1
            
            # extend by default - first == last
            else: 
                last += 1
                chars[s[last]].append[last]

        return longest

        