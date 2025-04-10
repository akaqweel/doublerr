arr = [1, 2, 3, 4, 5, 6, 7]

min_val = float('inf')
second_min = float('inf')

for x in arr:
    if x < min_val:
        second_min = min_val
        min_val = x
    elif x < second_min and x != min_val:
        second_min = x

print(second_min)
