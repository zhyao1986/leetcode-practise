from typing import List

'''
问题：
一条包含字母 A-Z 的消息通过以下映射进行了 编码:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
要解码已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
定义函数:
f(i)=>前i个数字映射的有效组合数量
边界:
f(0) = 1
f(1) = 1 or 0
推导过程:
s="11106"
i=1 => ['A']
i=2 => ['AA', 'K']
i=3 => ['AAA', 'KA', 'AK']
i=4 => ['AAJ', 'KJ']
i=5 => ['AAJF', 'KJF']
最优子结构:
f(i) = f(i-1) insert "()"
状态转移方程:
f(i)=
if i=0: 1
if i=1: 1
if i>1: 
    if 0 < lastNum*10+s[i] < 10:
        f(i-1)
    elif lastNum*10+s[i] == 10 or 20:
        f(i-2)
    elif 10 < lastNum*10+s[i] < 27:
        f(i-2)+f(i-1)
    elif lastNum*10+s[i] >= 27:
        f(i-1)
    else:
        return 0
重叠子问题:
去除重复
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        nums = list(map(int, list(s)))
        a, b = 1, 1
        lastNum = nums[0]
        if lastNum == 0:
            return 0
        for i in range(1, len(nums)):
            check = lastNum*10+nums[i]
            if 0 < check < 10:
                a, b = a, a
            elif check == 10 or check == 20:
                a, b = b, a
            elif 10 < check < 27:
                a, b = a+b, a
            elif check >= 27:
                if check % 10 == 0:
                    return 0
                else:
                    a, b = a, a
            else:
                return 0
            lastNum = nums[i]
        return a

def test1():
    s = "2101"
    print(Solution().numDecodings(s))

def test2():
    s = "230"
    print(Solution().numDecodings(s))

def test3():
    s = "06"
    print(Solution().numDecodings(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()