import lists


def partition(nums, start, end):
    center = start + (end - start) // 2
    pivot = nums[center]

    while start <= end:
        while nums[start] < pivot:
            start += 1
        while nums[end] > pivot:
            end -= 1
        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    return start


def quicksort(nums):
    start = 0
    end = len(nums) - 1
    stack = [start, end]

    while len(stack) > 0:
        end = stack.pop()
        start = stack.pop()

        pivot_idx = partition(nums, start, end)

        if pivot_idx - 1 > start:
            stack.append(start)
            stack.append(pivot_idx - 1)

        if pivot_idx < end:
            stack.append(pivot_idx)
            stack.append(end)


L = lists.randlist(20)
print("lista przed sortowaniem : \n" + str(L))
quicksort(L)
print("lista po sortowaniu : \n" + str(L))
