def quicksort(ar, l, r):
    if l < r:
        p = partition(ar, l, r)
        quicksort(ar, l, p-1)
        quicksort(ar, p+1, r)

    return ar

def partition(ar, l, r):
    pivot = ar[r]

    i = l - 1

    for j in range(l, r):
        if ar[j] <= pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]

    ar[i+1], ar[r] = ar[r], ar[i+1]
    return i + 1

ar = [1, 3, 5, 10, 22, 4, 3, 40, 220, 6, 12, 5]

print(quicksort(ar, 0, len(ar)-1))

