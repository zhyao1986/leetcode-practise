from typing import List

'''
定义函数:
f(i)=>以第i个数为结尾的连续子数组最大和
边界:
f(1) = array[0]
最优子结构:
f(i) = max(f(i-1)+nums[i],nums[i])
状态转移方程:
f(n)=
if n=1: nums[0]
if n>1: max(f(n-1)+nums[n], nums[n])
重叠子问题:
无
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0]*n
        f[0] = nums[0]
        result = f[0]
        for i in range(1, n):
            f[i] = max(f[i-1]+nums[i], nums[i])
            result = f[i] if f[i] > result else result
        return result

def test1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))

if __name__ == '__main__':
    test1()