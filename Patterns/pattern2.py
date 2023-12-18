# Right angled triangle star pattern
'''
For N=3, pattern is
* 
* *
* * *
'''

class Solution:
    def nForest(self, n: int) -> None:
        for i in range(n):
            for j in range(i+1):
                print('*', end=' ')
            print('')

if __name__ == '__main__':
    N = int(input("Enter the number: "))
    sol = Solution()
    sol.nForest(N)