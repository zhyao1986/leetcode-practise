from typing import List

'''
问题：
给定一个数字，我们按照如下规则把它翻译为字符串:0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
定义函数:
f(i)=>以从左往右数第i位数作为结尾的翻译方法数量
边界:
f(1) = 1
最优子结构:
if num[i-1]*10+num[i] < 26
    f(i) = f(i-2) + f(i-1)
else:
    f(i) = f(i-1)
状态转移方程:
f(i)=
if i=0: 1
if i=1: 1
if i>1:
    if num[i-1]*10+num[i] < 26:
        f(i) = f(i-2) + f(i-1)
    else:
        f(i) = f(i-1)
重叠子问题:
无
'''

class Solution:
    def translateNum(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        lastNumber = int(nums[0])
        a, b = 1, 1
        for i in range(1, n):
            if lastNumber*10 + int(nums[i]) < 26 and lastNumber != 0:
                a, b = b, a + b
            else:
                a, b = b, b
            lastNumber = int(nums[i])
        return b

def test1():
    num = 506
    print(Solution().translateNum(num))

if __name__ == '__main__':
    test1()
    