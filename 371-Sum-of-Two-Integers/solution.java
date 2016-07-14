public class Solution {
    public int getSum(int a, int b) {
        if (b==0) return a;
        int A = (a&b)<<1;
        int B = (a^b);
        return getSum(A, B);
    }
}