class Solution {
public:
    long long countCommas(long long n) {
        long long ans = 0;
        long long start = 1000;
        long long comma = 1;
        
        while (start <= n) {
            ans += (n - start + 1) * comma;
            start *= 1000; 
        }
        
        return ans;
    }
};
