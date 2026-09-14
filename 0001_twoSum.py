from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        len_num = len(nums)
        ans = []
        mark = 0
        for i in range(len_num - 1):
            for j in range(i + 1, len_num):
                if nums[i] + nums[j] == target:
                    mark = 1
                    ans.append(i)
                    ans.append(j)
                    print(ans)
                    break
            if mark == 1:
                break

twoSum([2,7,11,15], 9)