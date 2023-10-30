class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr_sum = 0
        diff = float('inf')
        final = 0

        for i in range(len(nums) - 2):
            first = nums[i]
            j = i+1
            k = len(nums) - 1

            while j<k:
                second = nums[j]
                third = nums[k]

                curr_sum = first + second + third

                if abs(target - curr_sum) < diff:
                    diff = abs(target - curr_sum)
                    final = curr_sum

                if curr_sum < target:
                    j += 1

                else:
                    k -= 1
        return final