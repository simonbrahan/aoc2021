def chunks(items, chunksize):
    return [items[i:i+chunksize] for i in range(0, len(items), chunksize)]


def line_wins(line, called_numbers):
    return all(num in called_numbers for num in line)


def row_from_board(board, row):
    return board[5*row:5*row+5]


def column_from_board(board, column):
    return board[column::5]


def sum_unmarked_on_board(board, called_numbers):
    return sum(set(board).difference(set(called_numbers)))


def run_game(call_order, boards):
    for num_calls in range(5, len(call_order) + 1):
        calls = call_order[:num_calls]

        for board in boards:
            for i in range(0, 5):
                row = row_from_board(board, i)
                if line_wins(row, calls):
                    return board, calls

                column = column_from_board(board, i)
                if line_wins(column, calls):
                    return board, calls
