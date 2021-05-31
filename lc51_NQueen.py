class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for i in range(n)] for j in range(n)]
        row = 0
        op = []
        def findNQ(board, row):
            if row == n:
                output = []
                for i in range(n):
                    output.append(''.join(board[i]))
                    
                op.append(output)
                #return

            for i in range(n):
                if is_valid(board, row, i):
                    #new_bd = [x[:] for x in board]
                    #new_bd[row][i] = 'Q'
                    #findNQ(new_bd, row+1)
                    board[row][i] = 'Q'
                    findNQ(board, row+1)
                    board[row][i] = '.'

        def is_valid(board, r, q):
            for i in range(r):
                if board[i][q] == 'Q':
                    return 0
                if -1<q-(r-i)<n and board[i][q-(r-i)] == 'Q':
                    return 0
                if -1<q+(r-i)<n and board[i][q+(r-i)] == 'Q':
                    return 0
            return 1

        findNQ(board, row)
        return op

n = 4
print(Solution.solveNQueens(Solution, n))
