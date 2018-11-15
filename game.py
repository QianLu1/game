# -*- coding: utf-8 -*-
import random
class Game(object):
    def __init__(self):
        # self.chess = [[0]*16]*16
        self.chesses = [ ["." for n in xrange(15)] for m in xrange(15) ]
        self.top_chessboard = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']
        chessboard = self.draw()
        self.row_count = 0
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
        self.row = row
        self.column = column
        if self.chesses[self.row][self.column] == ".":
            if chess_type == "white":
                self.chesses[self.row][self.column] = "X"
            else:
                self.chesses[self.row][self.column] = "O"
        chessboard = self.draw()
        print chessboard
        re = self.check()
        print "re", re

    def result(self, count):
        if count == 5:
            print("success")
            exit(0)

    def check(self):
        # 横向搜索 - 向左搜索
        row_count = 1
        for each in range(self.column - 1, -1, -1):
            if self.chesses[self.row][each] == self.chesses[self.row][self.column]:
                row_count += 1
                self.result(row_count)
            else:
                break
        # 横向搜索 - 向右搜索
        for each in range(self.column + 1, 15):
            if self.chesses[self.row][each] == self.chesses[self.row][self.column]:
                row_count += 1
                self.result(row_count)
            else:
                break
        # 纵向搜索 - 向上搜索
        column_count = 1
        for each_row in range(self.row - 1, -1, -1):
            if self.chesses[each_row][self.column] == self.chesses[self.row][self.column]:
                column_count += 1
                self.result(column_count)
            else:
                break
        # 纵向搜索 - 向下搜索
        for each_row in range(self.row + 1, 15):
            if self.chesses[each_row][self.column] == self.chesses[self.row][self.column]:
                column_count += 1
                self.result(column_count)
            else:
                break
        # 斜向搜索 - 左上搜索
        left_incline_count = 1
        for each in zip(range(self.row - 1, -1, -1), range(self.column - 1, -1, -1)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[self.row][self.column]:
                left_incline_count += 1
                self.result(left_incline_count)
            else:
                break
        # 斜向搜索 - 右下搜索
        for each in zip(range(self.row + 1, 15), range(self.column + 1, 15)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[self.row][self.column]:
                left_incline_count += 1
                self.result(left_incline_count)
            else:
                break
        # 斜向搜索 - 右上搜索
        right_incline_count = 1
        for each in zip(range(self.row - 1, -1, -1), range(self.column + 1, 15)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[self.row][self.column]:
                right_incline_count += 1
                self.result(right_incline_count)
            else:
                break
        # 斜向搜索 - 左下搜索
        for each in zip(range(self.row + 1, 15), range(self.column - 1, -1, -1)):
            each_row = each[0]
            each_column = each[1]
            if self.chesses[each_row][each_column] == self.chesses[self.row][self.column]:
                right_incline_count += 1
                self.result(right_incline_count)
            else:
                break

if __name__ == "__main__":
    print("Game start: ")
    try:
        game = Game()
        while True:
            for color in ["white", "black"]:
                value = raw_input("%s: " % color)
                site = value.split(" ")
                if (len(site) != 2):
                    print("Again: ")
                    value = raw_input("%s: " % color)
                row = site[0]
                column = site[1]
                if row.isdigit() or column.isdigit():
                    row = int(site[0])
                    column = int(site[1])
                else: 
                    print("Again: ")
                    value = raw_input("%s: " % color)
                if (row in range(0, 16) and column in range(0, 16)):
                    game.next(color, row, column)
                else: 
                    print("Again: ")
                    value = raw_input("%s: " % color)
    except Exception as e:
        print e
        exit(1)


    # game = Game()

    # game.next('white', 6, 7)
    # game.next('white', 6, 6)
    # game.next('white', 6, 8)
    # game.next('white', 6, 2)
    # game.next('white', 7, 7)
    # game.next('white', 7, 10)
    # game.next('white', 5, 7)
    # game.next('white', 8, 7)
    # # game.next('white', 9, 7)
    # # game.next('white', 7, 9)
    # game.next('white', 4, 6)
    # game.next('white', 3, 5)
    # game.next('white', 7, 5)
    # game.next('white', 4, 8)
    # game.next('white', 9, 3)
    # game.next('white', 8, 4)
    # game.next('white', 9, 0)




