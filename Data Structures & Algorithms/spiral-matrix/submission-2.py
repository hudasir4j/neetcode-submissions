class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top_row, right_col = 0, len(matrix[0]) - 1
        bot_row, left_col = len(matrix) - 1, 0
        

        while (left_col <= right_col and bot_row >= top_row):
            
            #left to right in top row
            for col in range(left_col, right_col + 1):
                output.append(matrix[top_row][col])
            print('step 1:', output)
            
            top_row += 1
            
            #top to bottom in right_col
            for row in range(top_row, bot_row + 1):
                output.append(matrix[row][right_col])
            print('step 2:', output)
            
            right_col -= 1

            
            if(top_row <= bot_row):
                #right to left in bot_row
                for col in range(right_col, left_col - 1, -1):
                    output.append(matrix[bot_row][col])
            print('step 3:', output)

            bot_row -= 1
        
            if (left_col <= right_col):
                #bottom to top in left_col
                for row in range(bot_row, top_row - 1, -1):
                    output.append(matrix[row][left_col])
            
            print('step 4:', output)
            left_col += 1

        return output