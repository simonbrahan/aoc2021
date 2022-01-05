from folding import fold_page, parse_fold

with open('input.txt') as f:
    page = f.read()

dot_list, fold_list = page.strip().split('\n\n')

dots = set([tuple(map(int, dot.strip().split(','))) for dot in dot_list.split('\n')])

folds = [parse_fold(fold) for fold in fold_list.split('\n')]

new_dots = fold_page(dots, folds[0][0], folds[0][1])

print(len(new_dots))
