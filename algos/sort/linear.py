def counting_sort(array: list) -> list:
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    return array


# проверка отсортированности массива по возрастанию и убыванию за O(len(A))
# int(True) = 1 must be +1 with s
# int(False) = 1 must be -1 with s
def check_sorted(A, ascending=True):
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag
