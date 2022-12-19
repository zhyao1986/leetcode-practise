from typing import List

'''
问题：
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
定义函数:
f(i,j)=>到i,j位置的最小路径值
边界:
f(0,0) = grid[0][0]
推导过程:
s="11106"
i=1 => ['A']
i=2 => ['AA', 'K']
i=3 => ['AAA', 'KA', 'AK']
i=4 => ['AAJ', 'KJ']
i=5 => ['AAJF', 'KJF']
最优子结构:
f(i,j) = min(f(i-1,j),f(i,j-1))+grid[i][j]
状态转移方程:
f(i,j)=
if i=0,j=0: grid[0][0]
elif i=0,j>0: f(i,j-1)+grid[i][j]
elif i>0,j=0: f(i-1,j)+grid[i][j]
else: min(f(i-1,j),f(i,j-1))+grid[i][j]
重叠子问题:
无
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

def test1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))

def test2():
    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(grid))

if __name__ == '__main__':
    test1()
    test2()