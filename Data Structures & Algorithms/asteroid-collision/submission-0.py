class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            elif asteroid < 0:
                done = False
                while not done:
                    # Mapping out new asteroid collision course
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(asteroid)
                        done = True
                    elif stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                    elif stack[-1] == -asteroid:
                        stack.pop()
                        done = True
                    else:
                        done = True

        return stack


        