def maximum(nums: list) -> int:
    max_value = None

    for num in nums:
        if max_value is None or num > max_value:
            max_value = num
    return max_value


def minimum(nums: list) -> int:
    """
    Find minimum number in array
    :return:
    """
    min_value = None

    for num in nums:
        if min_value is None or num < min_value:
            min_value = num
    return min_value
