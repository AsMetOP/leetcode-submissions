class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        return merge_sort(nums)



        # Bubble Sort(0^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0, n - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # return nums

        #Selection Sort(0^2)
        # n = len(nums)
        # for i in range(n):
        #     minimum = i
        #     for j in range(i+1, n):
        #         if nums[j] < nums[minimum]:
        #             minimum = j
        #     nums[i], nums[minimum]= nums[minimum], nums[i]
        # return nums
