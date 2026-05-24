class Solution:

    def isPalindrome(self, s: str) -> bool:
        alphanum = "qwertyuiopasdfghjklzxcvbnm1234567890"
        s = s.lower()
        s = [letter for letter in s if letter in alphanum]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
        