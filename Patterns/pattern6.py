# Right angled inverted triangle number pattern
'''
For N=3, pattern is
1 2 3
1 2
1
'''

class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            for j in range(i):
                print(j+1, end=' ')
            print('')

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    sol = Solution()
    sol.printTriangle(n)