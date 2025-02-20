# two pointer approach because it is sorted
def twoSum(numbers: [int], target: int) -> [int]:
    l, r  = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1,r+1] # 1 indexed