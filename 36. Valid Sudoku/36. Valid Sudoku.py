class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row
        
        for i in range(9):
            row_dic = {}
            for j in range(9):
                    if board[i][j] in row_dic.keys() and board[i][j] != ".":
                        print("colums")
                        print(row_dic,board[i][j])
                        return False
                    else:
                        row_dic[board[i][j]] = 0
                        
######################
# col

        for i in range(9):
            col_dic = {}
            for j in range(9):
                    if board[j][i] in col_dic.keys() and board[j][i] != ".":
                        print("rows")
                        print(col_dic,board[j][i], i)
                        return False
                    else:
                        col_dic[board[j][i]] = 0

###############
# boxes


        # for i in range(0,9,3):
        #      for j in range(3):
        #         if j == 0:    
        #             box_dic = {}
        #             if board[i][j] in box_dic.keys() and board[i][j] != ".":
        #                  return False
        #             if board[i][j+1] in box_dic.keys() and board[i][j + 1] != ".":
        #                  return False
        #             if board[i][j+2] in box_dic.keys() and board[i][j + 2] != ".":
        #                 return False
        #             else:
        #                 box_dic[board[i][j]] = 0
        #                 box_dic[board[i][j + 1]] = 0
        #                 box_dic[board[i][j + 2]] = 0
        #         elif j == 1:
        #                 box_dic = {}
        #                 if board[i][j+2] in box_dic.keys() and board[i][j+2] != ".":
        #                      return False
        #                 if board[i][j+3] in box_dic.keys() and board[i][j+3] != ".":
        #                      return False
        #                 if board[i][j+4] in box_dic.keys() and board[i][j+4] != ".":
        #                     return False
        #                 else:
        #                     box_dic[board[i][j+2]] = 0
        #                     box_dic[board[i][j+3]] = 0
        #                     box_dic[board[i][j+4]] = 0
        #         elif j == 2:
        #                 box_dic = {}
        #                 if board[i][j+4] in box_dic.keys() and board[i][j+4] != ".":
        #                      return False
        #                 if board[i][j+5] in box_dic.keys() and board[i][j+5] != ".":
        #                      return False
        #                 if board[i][j+6] in box_dic.keys() and board[i][j+6] != ".":
        #                     return False
        #                 else:
        #                     box_dic[board[i][j+4]] = 0
        #                     box_dic[board[i][j+5]] = 0
        #                     box_dic[board[i][j+6]] = 0
        # return True
                  

        for i in range(0,9,3):
             for j in range(i,i+3):
                if j == i:    
                    box_dic1 = {}
                    if board[i][j] in box_dic1.keys() and board[i][j] != ".":
                         return False
                    if board[i][j+1] in box_dic1.keys() and board[i][j + 1] != ".":
                         return False
                    if board[i][j+2] in box_dic1.keys() and board[i][j + 2] != ".":
                        return False
                    else:
                        box_dic1[board[i][j]] = 0
                        box_dic1[board[i][j + 1]] = 0
                        box_dic1[board[i][j + 2]] = 0
                elif j == i + 1:
                        box_dic2 = {}
                        if board[i][j] in box_dic2.keys() and board[i][j] != ".":
                             return False
                        if board[i][j+1] in box_dic2.keys() and board[i][j+1] != ".":
                             return False
                        if board[i][j+2] in box_dic2.keys() and board[i][j+2] != ".":
                            return False
                        else:
                            box_dic2[board[i][j]] = 0
                            box_dic2[board[i][j+2]] = 0
                            box_dic2[board[i][j+3]] = 0
                elif j == i + 2:
                        box_dic3 = {}
                        if board[i][j] in box_dic3.keys() and board[i][j] != ".":
                             return False
                        if board[i][j+1] in box_dic3.keys() and board[i][j+1] != ".":
                             return False
                        if board[i][j+2] in box_dic3.keys() and board[i][j+2] != ".":
                            return False
                        else:
                            box_dic3[board[i][j]] = 0
                            box_dic3[board[i][j+1]] = 0
                            box_dic3[board[i][j+2]] = 0
        return True
                  
board = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
x = Solution()
y = x.isValidSudoku(board)
print(y)
