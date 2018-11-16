from game import Game
import random
import re

if __name__ == "__main__":
    try:
        print("Game start: ")
        color = random.choice(["white", "black"])
        game = Game()
        while True:
            input_value = raw_input("%s: " % color).strip()
            pattern = re.compile("^(0?[0-9]|1[0-4])\\s+(0?[0-9]|1[0-4])$")
            input_number = pattern.search(input_value)
            if input_number:
                row = input_number.group(1)
                column = input_number.group(2)
                if row.isdigit() and column.isdigit():
                    row = int(row)
                    column = int(column)
                    result = game.next(color, row, column)
                    if not result:
                        print("This position is occupied, input again.")
                        continue
                else:
                    print("Input number please.")
                    continue
            else:
                print("Input two numbers separated by spaces.")
                continue
            color = "black" if color == "white" else "white"
    except Exception as e:
        print 'error', e
        exit(1)

