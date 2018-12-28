#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.boxpos_list = [
                [0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6],
                ]
        self.boxplace_list = [
                [0,0],[0,1],[0,2],
                [1,0],[1,1],[1,2],
                [2,0],[2,1],[2,2],
                ]

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        boardstack = [[ set([1,2,3,4,5,6,7,8,9]) for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.filterboard(board, boardstack, i, j)
        self.travelboard(board, boardstack)
        print board

    def filterboard(self, board, boardstack, i, j):
        if board[i][j] == '.':
            return
        num = int(board[i][j])
        for k in range(9):
            if num in boardstack[i][k]:
                boardstack[i][k].remove(num)
            if num in boardstack[k][j]:
                boardstack[k][j].remove(num)
        boxhead = (i / 3)*3, (j / 3)*3
        for boxplace in self.boxplace_list:
            x = boxhead[0]+boxplace[0]
            y = boxhead[1]+boxplace[1]
            if num in boardstack[x][y]:
                boardstack[x][y].remove(num)

    def checkboard(self, board, c, i, j):
        if c == '.':
            return True
        boxhead = (i/3)*3, (j/3)*3
        for k in range(9):
            if board[i][k] == c: return False
            if board[k][j] == c: return False
            x = boxhead[0] + self.boxplace_list[k][0]
            y = boxhead[1] + self.boxplace_list[k][1]
            if board[x][y] == c: return False
        return True

    def travelboard(self, board, boardstack):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for s in boardstack[i][j]:
                        cand = str(s)
                        if self.checkboard(board, cand, i, j):
                            board[i][j] = cand
                            if self.travelboard(board, boardstack):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True





if __name__ == '__main__':
    abc =   [
              ["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ]
    abc = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(abc)
