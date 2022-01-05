from folding import fold_page, parse_fold, print_page

with open('input.txt') as f:
    page = f.read()

dot_list, fold_list = page.strip().split('\n\n')

dots = set([tuple(map(int, dot.strip().split(','))) for dot in dot_list.split('\n')])

folds = [parse_fold(fold) for fold in fold_list.split('\n')]

for fold in folds:
    dots = fold_page(dots, fold[0], fold[1])

print_page(dots)
