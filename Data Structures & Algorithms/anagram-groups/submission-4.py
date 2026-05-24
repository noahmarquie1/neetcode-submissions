class Solution:
    def isAnagram(self, str1: str, str2: str):
        if sorted(str1) == sorted(str2):
            return True
        return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        while len(strs) > 0:
            curr = strs[0]
            group = [curr]
            strs = strs[1:]
            i = 0
            while i <= len(strs) - 1:
                if self.isAnagram(strs[i], curr):
                    group.append(strs[i])
                    strs.remove(strs[i]) # Index stays the same
                else:
                    i += 1

            anagrams.append(group)
        return anagrams


        