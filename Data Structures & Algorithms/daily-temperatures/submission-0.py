class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        peaks: list[tuple[int]] = [] # (temp, idx)
        forecast = [0 for _ in temperatures]

        for i in range(len(temperatures)):
            i = len(temperatures) - 1 - i
            if len(peaks) == 0:
                forecast[i] = 0
            else: # go through peaks to find closest higher
                done = False
                while not done:
                    if len(peaks) == 0:
                        forecast[i] = 0
                        done = True
                    elif temperatures[i] < peaks[-1][0]:
                        forecast[i] = peaks[-1][1] - i
                        done = True
                    else:
                        peaks.pop()

            peaks.append((temperatures[i], i))

        return forecast



            
        



        