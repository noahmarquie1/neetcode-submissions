class Solution:

    def encode(self, strs: List[str]) -> str:
        # '\n' is not a valid ascii character in python (seen as special function)
        # '\s' at start (if nonempty) and '\e' at end (if nonempty)
        encoded_str = ""
        for i, string in enumerate(strs):
            if i == 0:
                encoded_str += '\\s'

            encoded_str += string
            if i < len(strs) - 1:
                encoded_str += '\n'
            else:
                encoded_str += '\\e'

        return encoded_str


    def decode(self, s: str) -> List[str]:
        if '\\s' in s and '\\e' in s:
            str_content = s.split('\\s')[1].split('\\e')[0]
            return str_content.split('\n')

        return []
