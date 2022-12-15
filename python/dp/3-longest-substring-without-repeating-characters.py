from typing import List

'''
题目:
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
定义函数:
f(i)=>以第i个字符为结尾的不重复的最长子串
边界:
f(0) = s[0]
最优子结构:
index = f(i-1).find(s[i])
f(i) = f(i-1)[index:] + s[i]
状态转移方程:
f(n)=
if n=0: s[0]
if n>1: f(n-1)[index:] + s[n]
重叠子问题:
无
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        f = [""]*n
        f[0] = s[0]
        result = 1
        for i in range(1, n):
            index = f[i-1].find(s[i])
            if index == -1:
                f[i] = f[i-1] + s[i]
            else:
                f[i] = f[i-1][index+1:] + s[i]
            result = len(f[i]) if len(f[i]) > result else result
        return result

def test1():
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

def test2():
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))

def test3():
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
