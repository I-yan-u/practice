# Binary search of a sorted array

arr = [5,12,15,19,30,37]

def binary_search(lst: list[int], num: int) -> int|None:
    l, r = 0, len(lst) - 1
    while l <= r:
        mid = (l + r) // 2
        print(f'list: {lst}, Mid: {mid}, left: {l}, right: {r}')
        if lst[mid] == num: return mid
        elif lst[mid] < num: l = mid + 1
        elif lst[mid] > num: r = mid - 1
    return None

print(binary_search(arr, 16)) # None
print(binary_search(arr, 19)) # 3
print(binary_search(arr, 37)) # 5
