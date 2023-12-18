# Rectangular Star pattern
'''
For N=3, pattern is
* * *
* * *
* * *
'''
class Solution:
    def printSquare(self, n):
        for i in range(n):
            for j in range(n):
                print('*', end=' ')
            print('')


if __name__ == '__main__':
    N = int(input('Enter a number for which you want to create a rectangular star pattern: '))
    sol = Solution()
    sol.printSquare(N)