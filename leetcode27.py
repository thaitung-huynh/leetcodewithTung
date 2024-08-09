class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # print("Hallo")
        for i in range(len(nums)):
            if nums[i] != val:
                continue
            for j in range(i + 1, len(nums)):
                if nums[j] != val:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    break
        print(nums)
        nums.append(val)
        for i in range(len(nums)):
            if nums[i] == val:
                return i

a = Solution()
print(a.removeElement([5, 5, 4, 5, 5, 5, 5], 5))