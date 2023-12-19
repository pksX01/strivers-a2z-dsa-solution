# Right angled inverted triangle star pattern
'''
For N=3, pattern is
* * * 
* *  
*
'''

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N, i, -1):
                print('*', end=' ')
            print('')

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    sol = Solution()
    sol.printTriangle(n)