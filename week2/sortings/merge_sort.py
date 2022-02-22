def merge_sort(nums: list):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        to_ret = [*nums]
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        if i < len(left):
            nums[k:] = left[i:]
            k+=len(left[i:])

        if j < len(right):
            nums[k:] = right[j:]
            k += len(right[j:])
        to_ret, nums = nums, to_ret
        return to_ret


if __name__ == '__main__':
    print(merge_sort([3, 73, 1, 8, 4, 8, 3, 34, 87, 3, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
    print(merge_sort([3, 73, 1, 8, 4, 8, 6, -1, 3, 3, 34, 87, 3, 0, 51, -10, 5, 11, 6, 1, 7, 4, 6, 2, 464, 9]))
