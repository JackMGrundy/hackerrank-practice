"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
# 196ms. 98 percentile
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [0]*(len(matrix[0]) + 1)
        longestSide = 0
        for i in range(len(matrix)):
            prevSquare =0
            for j in range(len(matrix[0])):
                temp = dp[j]
                if matrix[i][j] == '1':
                    dp[j] = 1 + min(dp[j], dp[j-1], prevSquare)
                    longestSide = max(longestSide, dp[j])
                else:
                    dp[j] = 0
                
                prevSquare = temp
        
        return longestSide*longestSide


"""
Notes:

Two hard things in this problem. The first is the logic for the dp, although after the fact 
it seems pretty straightforward imo.
At any element you can check if you have a 2 by 2 square by looking at its neighbors. So anywhere you see
1 1
1 1
you're going to replace the bottom right corner with a 2. Note we're going top down and left to right...
So if you see
2 2
2 1 
...then you know that you actually have
1 1 1
1 2 2
1 2 1
meaning you can actually put 3 in the corner. 

On the other hand, if any of the neighbors are 1's, then you won't have the full cube. Implying that
at each spot, if it's a 1, you take the min of the three neighbors + 1. 


The second hard thing is just dealing with the fact the input is characters not ints...annoying imo. The second
solution up there just uses a standard 1d dp array to keep track of the last row processed in terms of ints...which
is all we need. So we can avoid casting anything. 

The first solution only casts the first first row and the first column. 

Most of it is straightforwards. The one thing I want to note is that temp variable switch. Basically because our dp is
a single array, when we're processing element i, we've already replaced element i-1 with an updated value. That's a problem
because the i-1 value represents the j-1,i-1 value for the ith element in the dp. So we use that little temp switch to 
skirt the issue. 
"""