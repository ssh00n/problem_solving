N = int(input())

layer = 1
number = 1

while number < N:
    layer += 1
    number += 6 * (layer-1)

print(layer)