import day13put
import numpy as np
input_used = day13put.input1
coords = input_used[0]
folds = input_used[1]

xmax, ymax = max([tup[0] for tup in coords]) +1, max([tup[1] for tup in coords]) +1
array1 = np.zeros((xmax, ymax))
print(array1.shape)
for coord in coords:
    array1[(coord)] = 1

def fold_in_half(array, axis):
    halves = np.array_split(array, 2, axis=fold_axis)
    dotsonhalve2 = np.where(np.flip(halves[1], axis=fold_axis) == 1)
    for dot in np.nditer(dotsonhalve2):
        halves[0][dot] = 1
    result =  np.delete(halves[0], (-1), axis=fold_axis)
    return result

folded_array = array1
print(f'{folded_array.T}\n')
print(folded_array.shape)

# for fold in folds:
for i in range(1):
    fold = folds[0]

    fold_axis = 0 if not fold[1] else 1
    folded_array = fold_in_half(folded_array, fold_axis)
    print(f'{folded_array.T}\n')
    print(folded_array.shape)
    print(f'number of dots = {len(np.where(folded_array == 1)[0])}')

