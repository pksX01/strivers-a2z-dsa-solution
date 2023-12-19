# Right angled triangle number pattern type 2
'''
For N=3, pattern is
1
2 2 
3 3 3
'''

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(i+1, end=' ')
            print('')

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    sol = Solution()
    sol.printTriangle(n)