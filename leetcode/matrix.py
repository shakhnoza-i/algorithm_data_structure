class Solution:
    def setZeroes(self, matrix):
        # O(1) - space, O(n*m) - time complexity
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):# make zero most cols and rows
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0: # make zero first col if we need to
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero: # make zero first row if we need to
            for c in range(COLS):
                matrix[0][c] = 0


    def spiralOrder(self, matrix):
        # O(m*n) - time, O(1) - space complexity
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right): # the right value is not inclusive
                res.append(matrix[top][i]) #[row][column]
            top += 1

            # get every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right-1, left-1, -1): # (start, end, step)
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # get every i in the left column
            for i in range(bottom-1, top-1, -1): 
                res.append(matrix[i][left])
            left +=1
        return res

    
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # save the top left
                topleft = matrix[top][l + i]
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right
                matrix[top + i][r] = topleft
            r -= 1
            l += 1

    
    def wordSearch(self, board, word): # O(n*m*4*n)
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        