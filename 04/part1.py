from game import chunks, run_game, sum_unmarked_on_board

with open('sample.txt') as f:
    call_order = list(map(int, f.readline().strip().split(',')))

    boards = chunks(
        list(map(int, f.read().split())),
        25
    )

winning_board, calls = run_game(call_order, boards)

print(sum_unmarked_on_board(winning_board, calls) * calls[-1])
