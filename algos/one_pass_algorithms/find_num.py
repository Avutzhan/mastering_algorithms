from typing import List


def finder(nums: List[int], num: int) -> bool:
    """
    Find num in list
    :param nums: List[int]
    :param num: int
    :return: bool
    """
    if num in nums:
        return True
    return False
