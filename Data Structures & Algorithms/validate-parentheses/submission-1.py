class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_dict = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for letter in s:
            if letter in parenthesis_dict.keys():
                if len(stack) > 0 and stack[-1] == parenthesis_dict[letter]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(letter)


        return len(stack) == 0
        