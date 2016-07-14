public class Solution {
    public int getSum(int a, int b) {
        if (b==0) return a;
        if (a==0) return b;
        int A = (a&b)<<1;
        int B = (a^b);
        return getSum(A, B);
    }
}