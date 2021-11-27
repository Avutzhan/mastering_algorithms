def simple_sum(nums: list) -> int:
    summary: int = 0
    for i in nums:
        summary += i
    return summary


def simple_sum_short(nums: list) -> int:
    return sum(nums)
