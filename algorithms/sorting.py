def bubble_sort(items: list[int]) -> list[int]:
    while True:
        swapped = False
        for curr in range(len(items)-1):
            if items[curr] > items[curr+1]:
                items[curr], items[curr+1] = items[curr+1], items[curr]
                swapped = True
        
        if not swapped:
            break

    return items

def merge_sort(items: list[int]) -> list[int]:
    if len(items) > 1:
        m = len(items) // 2
        left = merge_sort(items[:m]) + [float('inf')]
        right = merge_sort(items[m:]) + [float('inf')]

        left_idx, right_idx, res = 0, 0, []

        while len(res) != len(items):
            if left[left_idx] < right[right_idx]:
                res.append(left[left_idx])
                left_idx += 1
            else:
                res.append(right[right_idx])
                right_idx += 1
        
        return res
    return items

def insertion_sort(items: list[int]) -> list[int]:
    for i in range(1, len(items)):
        j = i-1
        while j >= 0 and items[i] < items[j]:
            items[i], items[j] = items[j], items[i]
            i -= 1
            j -= 1
    return items
