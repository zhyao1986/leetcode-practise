from typing import List

'''
问题：
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7]是数组[0,3,1,6,2,2,7]的子序列。
定义函数:
f(i)=>以第i个数字结束的最长递增子序列
边界:
f(0) = nums[0]
推导过程:
nums=[10,9,2,5,3,7,101,18]
i=0 => [10]
i=1 => [9]
i=2 => [2]
i=3 => [2,5]
i=4 => [2,3]
i=5 => [2,3,7]
i=6 => [2,3,7,101]
i=7 => [2,3,7,18]
[4,10,4,3,8,9]
[4]
[4,10]


最优子结构:
f(i) = f(i-1)+1 if nums[i] > nums[i-1] else f(i-1)
状态转移方程:
f(i)=
if i=0: 1
if i>0: f(i-1)+1 if nums[i] > nums[i-1] else f(i-1)
重叠子问题:
无
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

def test1():
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))

def test2():
    nums = [0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums))

def test3():
    nums = [7,7,7,7,7,7,7]
    print(Solution().lengthOfLIS(nums))

if __name__ == '__main__':
    test1()
    test2()
    test3()