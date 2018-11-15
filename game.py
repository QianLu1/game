# -*- coding:UTF-8 -*-
class Game(object):
    def __init__(self):
        # self.chess = [[0]*16]*16
        self.chesses = [ ["." for n in xrange(15)] for m in xrange(15) ]
        self.top_chessboard = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']
        chessboard = self.draw()
        print chessboard

    def draw(self):
        chessboard = '   ' + ' '.join(self.top_chessboard) + '\n'
        for index, value in enumerate(self.chesses):
            chessboard += self.top_chessboard[index] + "  "  
            chessboard += "  ".join(value)
            if index < 14:
               chessboard += "\n"
        return chessboard
        
    def next(self, chess_type, row, column):
        if self.chesses[row][column] == ".":
            if chess_type == "white":
                self.chesses[row][column] = "X"
            else:
                self.chesses[row][column] = "O"
        chessboard = self.draw()
        print chessboard
        self.check(row, column)

    def result(self, count):
        if count == 5:
            print("success")
            return "SUCCESS"

    def check(self, row, column):
        # 横向搜索 - 向左搜索
        row_count = 1
        for each in range(column - 1, -1, -1):
            if self.chesses[row][each] == self.chesses[row][column]:
                row_count += 1
                self.result(row_count)
            else:
                break
        # 横向搜索 - 向右搜索
        for each in range(column + 1, 15):
            if self.chesses[row][each] == self.chesses[row][column]:
                row_count += 1
                self.result(row_count)
            else:
                break
        print row, column, row_count
        # 纵向搜索 - 向上搜索
        column_count = 1
        for each_row in range(row - 1, -1, -1):
            if self.chesses[each_row][column] == self.chesses[row][column]:
                column_count += 1
                self.result(column_count)
            else:
                break
        # 纵向搜索 - 向下搜索
        for each_row in range(row + 1, 15):
            if self.chesses[each_row][column] == self.chesses[row][column]:
                column_count += 1
                self.result(column_count)
            else:
                break
        # 斜向搜索 - 左上搜索
        left_incline_count = 1
        for each in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[row][column]:
                left_incline_count += 1
                self.result(left_incline_count)
            else:
                break
        # 斜向搜索 - 右下搜索
        for each in zip(range(row + 1, 15), range(column + 1, 15)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[row][column]:
                left_incline_count += 1
                self.result(left_incline_count)
            else:
                break
                

    def compare(self, before_row, before_column, row, column, count):
        pass
if __name__ == "__main__":
    game = Game()
    game.next('white', 6, 7)
    game.next('white', 6, 6)
    game.next('white', 6, 8)
    game.next('white', 6, 2)
    game.next('white', 7, 7)
    game.next('white', 7, 10)
    game.next('white', 5, 7)
    game.next('white', 8, 7)
    # game.next('white', 9, 7)
    game.next('white', 7, 9)
    game.next('white', 4, 6)
    game.next('white', 3, 5)
