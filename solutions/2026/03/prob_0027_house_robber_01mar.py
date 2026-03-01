def houseRobber(nums: List[int]) -> int:
    """
    Approach: Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    nums = [1,2,3,1]
    print(houseRobber(nums))  # Expected: 4
    nums = [2,7,9,3,1]
    print(houseRobber(nums))  # Expected: 12
    nums = [2,7,9]
    print(houseRobber(nums))  # Expected: 12
    nums = [1,7,1,5,9,2]
    print(houseRobber(nums))  # Expected: 16