def parse_fold(fold_str):
    fold_data = fold_str.strip().split(' ')[-1]
    print(fold_data)
    fold_dir, fold_axis = fold_data.split('=')

    return fold_dir, int(fold_axis)


with open('sample.txt') as f:
    page = f.read()

dot_list, fold_list = page.strip().split('\n\n')

dots = [tuple(map(int, dot.strip().split(','))) for dot in dot_list.split('\n')]

folds = [parse_fold(fold) for fold in fold_list.split('\n')]

print(dots)
print(folds)
