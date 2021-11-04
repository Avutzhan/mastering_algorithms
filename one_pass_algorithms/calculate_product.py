def product(nums: list) -> int:
    result: int = 1
    for i in nums:
        result *= i
    return result
