/*
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
*/
// 1st attempt: 48th percentile in speed
import java.util.*;

class Solution {
    
    HashSet<Integer> bloomed = new HashSet<Integer>();
    
    public boolean check(int start, int end, int l) {
        if (start < 1 || end > l) {
            return false;
        }
        if ( !bloomed.contains(start) || !bloomed.contains(end) ) {
            return false;
        }
        for (int i = start+1; i < end; i++) {
            if (bloomed.contains(i)) {
                return false;
            }
        }
        return(true);
    }
    
    public int kEmptySlots(int[] flowers, int k) {
        int l = flowers.length;
        for (int day = 0; day < l; day++) {
            int flower = flowers[day];
            bloomed.add(flower);
            if ( check(flower, flower+k+1, l) || check(flower-k-1, flower, l) ) {
                return day+1;
            }
        }
        return -1;
    }
}