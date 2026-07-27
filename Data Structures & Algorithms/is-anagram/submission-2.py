class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [char for char in s]
        for char in t:
            if char not in s_list:
                return False
            else:
                s_list.remove(char)

        return len(s_list) == 0
        