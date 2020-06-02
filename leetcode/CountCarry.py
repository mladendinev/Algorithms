def countCarryOperations(a, b):
    astr = str(a)
    bstr = str(b)

    left = len(astr) - 1
    right = len(bstr) - 1
    acc = 0
    count = 0
    while (left >= 0 and right >= 0):
        sum = int(astr[left]) + int(bstr[right]) + acc
        if sum >= 10:
            count += 1
            acc = sum % 10
        else:
            acc = 0
        left -= 1
        right -= 1
    return count


print(countCarryOperations(123, 594))
