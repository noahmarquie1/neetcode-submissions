class Solution:
    def __init__(self):
        self.memory = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            self.memory[n] = 1
        elif n == 2:
            self.memory[n] = 2
        elif n not in self.memory.keys():
            self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memory[n]
        