# -*- coding:UTF-8 -*-
class Game(object):
    def __init__(self):
        # {'white': {1: [4, 7], 2: [0]}, 'black': {}}
        # self.white = {}
        # self.black = {}
        self.chess = {'white': {}, 'black': {}}

    def get_type(self, type):
        return self.chess.get(type)

    def next(self, type, row, column):
        type_value = self.get_type(type)
        exist = type_value.has_key(row)
        if exist:
            type_value[row].append(column)
        else :
            type_value[row] = [column]
        print(self.chess)        
        self.check(type_value, row, column)
    
    def check(self, type_value, row, column):
        # 横向搜索 - 向左搜索
        row_count = 0
        for i in range(0, column):
            if i in type_value.get(row):
                row_count += 1
        # 横向搜索 - 向右搜索
        for i in range(column+1, 15):
            if i in type_value.get(row):
                row_count += 1
        print 'row_count', row_count
        # 纵向搜索 - 向上搜索
        column_count = 0
        for i in range(0, row):
            exist = type_value.get(row, [])
            if column in exist:
                column_count += 1
        # 纵向搜索 - 向下搜索
        for i in range(row, 15):
            exist = type_value.get(row, [])
            if column in exist:
                column_count += 1
        print 'column_count', column_count
                


if __name__ == "__main__":
    game = Game()
    game.next('white', 0, 4)
    game.next('white', 1, 4)
    game.next('white', 3, 4)
    game.next('white', 2, 7)
    # game.next('black', 2, 6)
           

    # def check(self, type, site):
    #     for i in range()