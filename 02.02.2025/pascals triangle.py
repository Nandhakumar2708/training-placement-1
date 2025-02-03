class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        all_rows = []  
        current_row = [1] 

        for i in range(numRows):
            all_rows.append(current_row) 

            shifted = [0] + current_row
            current_row = current_row + [0]
            current_row = [shifted[j] + current_row[j] for j in range(len(current_row))]

        return all_rows
