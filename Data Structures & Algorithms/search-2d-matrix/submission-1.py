class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First search rows, split halfway until we only have one row
        while len(matrix) > 1:
            split = int(len(matrix) / 2)
            if matrix[split][0] > target:
                matrix = matrix[:split]
            else:
                matrix = matrix[split:]

        target_row = matrix[0]
        # Finally search column, and pay attention to special case of not contained
        if target < target_row[0] or target > target_row[-1]:
            return False

        while len(target_row) > 1:
            split = int(len(target_row) / 2)
            if target_row[split] > target:
                target_row = target_row[:split]
            else:
                target_row = target_row[split:]

        
        return target == target_row[0]
        