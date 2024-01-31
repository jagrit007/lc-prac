class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ptr_one = 0
        ptr_two = len(numbers) -1
        sum = 0
        while True:
            sum = numbers[ptr_one] + numbers[ptr_two]
            if sum == target:
                return [ptr_one+1, ptr_two+1]
            if sum>target:
                if ptr_one < ptr_two:
                    ptr_two -= 1
            else:
                if ptr_two > ptr_one:
                    ptr_one +=1