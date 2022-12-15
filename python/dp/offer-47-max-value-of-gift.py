from typing import List

'''
问题：
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值(价值大于 0)。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
定义函数:
f(i,j)=>到达(i,j)位置时的最大价值
边界:
f(0，0) = grid[0][0]
最优子结构:
f(i,j) = max(f(i-1,j), f(i,j-1))+grid[i][j])
状态转移方程:
f(i,j)=
if i,j=0,0: grid[0][0]
if i,j>0,0: max(f(i-1,j), f(i,j-1))+grid[i][j])
重叠子问题:
无
'''

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i != 0 or j != 0:
                    if i == 0:
                        grid[i][j] += grid[i][j-1]
                    elif j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

def test1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().maxValue(grid))

if __name__ == '__main__':
    test1()