from typing import List

'''
问题：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
定义函数:
f(i,j)=>走到i,j位置时的不同路径数
边界:
f(0,0) = 1
推导过程:
最优子结构:
f(i,j) = f(i-1,j)+f(i,j-1)
状态转移方程:
f(i,j)=
if i,j=0,0: 1
if i,j!=0,0: f(i-1,j)+f(i,j-1)
重叠子问题:
无
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 1
        return grid[-1][-1]


def test1():
    m, n = 3, 7
    print(Solution().uniquePaths(m, n))

if __name__ == '__main__':
    test1()