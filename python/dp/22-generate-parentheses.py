from typing import List

'''
问题：
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
定义函数:
f(i)=>i对括号的有效组合
边界:
f(0) = 1
f(1) = 1
推导过程:
i=0 => []
i=1 => ["()"]
i=2 => ["(())", "()()"]
i=3 => ["((()))","(()())","(())()","()(())","()()()"]
最优子结构:
f(i) = f(i-1) insert "()"
状态转移方程:
f(i)=
if i=1: ["()"]
if i>1: f(i-1) insert "()"
重叠子问题:
去除重复
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        f = ["()"]
        for i in range(1, n):
            result = set()
            for ele in f:
                for j in range(len(ele)):
                    generate = ele[0:j] + "()" + ele[j:]
                    result.add(generate)
            f = list(result)
        return f

def test1():
    n = 8
    print(Solution().generateParenthesis(n))

if __name__ == '__main__':
    test1()