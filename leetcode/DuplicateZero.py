def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    original = {idx: el for idx, el in enumerate(arr)}
    p_orig = 0
    cur = 0
    while cur < len(arr) and p_orig < len(original):
        if original[p_orig] == 0 and cur + 1 < len(arr):
            arr[cur + 1] = 0
            arr[cur] = 0
            cur += 1
        else:
            arr[cur] = original[p_orig]
        p_orig += 1
        cur+=1


hah = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(hah)

print(hah)
