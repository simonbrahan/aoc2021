from game import chunks, run_game, sum_unmarked_on_board

with open('input.txt') as f:
    call_order = list(map(int, f.readline().strip().split(',')))

    boards = chunks(
        list(map(int, f.read().split())),
        25
    )

while len(boards) > 0:
    winning_board, calls = run_game(call_order, boards)
    last_board = winning_board
    boards.remove(winning_board)

print(sum_unmarked_on_board(last_board, calls) * calls[-1])
