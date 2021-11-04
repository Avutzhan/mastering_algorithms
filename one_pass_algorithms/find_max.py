def maximum(nums: list) -> int:
    max_value = None

    for num in nums:
        if max_value is None or num > max_value:
            max_value = num
    return max_value
