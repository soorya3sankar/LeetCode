class Solution {
public:
    int maxProduct(int n) {
        int maxD=0, maxD2=0;
        for( ;n>0; n/=10){
            int D=n%10;
            bool d1=D>=maxD, d2=(!d1)&(D>=maxD2);
            maxD2+=(-d1&(maxD-maxD2))+(-d2 & (D-maxD2));
            maxD+=(-d1 & (D-maxD));
        }
        return maxD*maxD2;
    }
};
