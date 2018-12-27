#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.checkrow(board) and self.checkcolumn(board) and self.checkbox(board):
            return True
        else:
            return False
        pass

    def checkrow(self, board):
        for i in range(9):
            checkset = set()
            for j in range(9):
                if board[i][j] in checkset:
                    return False
                else:
                    if board[i][j] != '.':
                        checkset.add(board[i][j])
        return True

    def checkcolumn(self, board):
        for i in range(9):
            checkset = set()
            for j in range(9):
                if board[j][i] in checkset:
                    return False
                else:
                    if board[j][i] != '.':
                        checkset.add(board[j][i])
        return True

    def checkbox(self, board):
        boxpos_list = [
                [0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6],
                ]
        boxplace_list = [
                [0,0],[0,1],[0,2],
                [1,0],[1,1],[1,2],
                [2,0],[2,1],[2,2],
                ]
        for boxpos in boxpos_list:
            checkset = set()
            for boxplace in boxplace_list:
                x = boxpos[0]+boxplace[0]
                y = boxpos[1]+boxplace[1]
                if board[x][y] in checkset:
                    return False
                else:
                    if board[x][y] != '.':
                        checkset.add(board[x][y])
        return True


if __name__ == '__main__':
    abc =   [
              ["9","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ]
    print Solution().isValidSudoku(abc)




